from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50))  # Can be 'Vehicle', 'Pet', etc.
    maintenance_history = db.relationship('MaintenanceRecord', backref='item', lazy=True)
    documents = db.relationship('Document', backref='item', lazy=True)
    expenses = db.relationship('Expense', backref='item', lazy=True)
    images = db.relationship('Image', backref='item', lazy=True)
    notes = db.relationship('Note', backref='item', lazy=True)  # Added notes relationship

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def add_maintenance_record(self, record):
        self.maintenance_history.append(record)
        db.session.commit()

    def add_document(self, document):
        self.documents.append(document)
        db.session.commit()

    def add_expense(self, expense):
        self.expenses.append(expense)
        db.session.commit()

    def add_image(self, image):
        self.images.append(image)
        db.session.commit()

    def add_note(self, note):
        self.notes.append(note)
        db.session.commit()

class Vehicle(Item):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, db.ForeignKey('items.id'), primary_key=True)
    make = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(100), nullable=False)
    year_purchased = db.Column(db.Integer, nullable=False)
    vin = db.Column(db.String(100))  # Vehicle Identification Number
    mileage = db.Column(db.Integer)  # Current mileage

    def __init__(self, name, make, model, year, color, year_purchased, vin=None, mileage=None):
        super().__init__(name, 'Vehicle')
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.year_purchased = year_purchased
        self.vin = vin
        self.mileage = mileage

class Pet(Item):
    __tablename__ = 'pets'
    id = db.Column(db.Integer, db.ForeignKey('items.id'), primary_key=True)
    species = db.Column(db.String(100), nullable=False)
    breed = db.Column(db.String(100), nullable=False)
    birth_year = db.Column(db.Integer)  # Birth year of the pet
    weight = db.Column(db.Float)  # Weight of the pet
    microchip_number = db.Column(db.String(100))  # Microchip number

    def __init__(self, name, species, breed, birth_year=None, weight=None, microchip_number=None):
        super().__init__(name, 'Pet')
        self.species = species
        self.breed = breed
        self.birth_year = birth_year
        self.weight = weight
        self.microchip_number = microchip_number

class Equipment(Item):
    __tablename__ = 'equipment'
    id = db.Column(db.Integer, db.ForeignKey('items.id'), primary_key=True)
    serial_number = db.Column(db.String(100))
    purchase_date = db.Column(db.Date)
    warranty_expiry = db.Column(db.Date)  # Warranty expiry date
    manufacturer = db.Column(db.String(100))  # Manufacturer name
    model_number = db.Column(db.String(100))  # Model number

    def __init__(self, name, serial_number, purchase_date, warranty_expiry=None, manufacturer=None, model_number=None):
        super().__init__(name, 'Equipment')
        self.serial_number = serial_number
        self.purchase_date = purchase_date
        self.warranty_expiry = warranty_expiry
        self.manufacturer = manufacturer
        self.model_number = model_number

class Outbuilding(Item):
    __tablename__ = 'outbuildings'
    id = db.Column(db.Integer, db.ForeignKey('items.id'), primary_key=True)
    structure_type = db.Column(db.String(100))  # e.g., Barn, Shed
    construction_date = db.Column(db.Date)  # Date of construction
    dimensions = db.Column(db.String(100))  # Dimensions (e.g., 20x30 ft)

    def __init__(self, name, structure_type, construction_date=None, dimensions=None):
        super().__init__(name, 'Outbuilding')
        self.structure_type = structure_type
        self.construction_date = construction_date
        self.dimensions = dimensions

class Livestock(Item):
    __tablename__ = 'livestock'
    id = db.Column(db.Integer, db.ForeignKey('items.id'), primary_key=True)
    species = db.Column(db.String(100))
    breed = db.Column(db.String(100))
    purchase_date = db.Column(db.Date)
    birth_year = db.Column(db.Integer)  # Birth year of the livestock
    health_status = db.Column(db.String(100))  # Health status (e.g., Healthy, Ill)

    def __init__(self, name, species, breed, purchase_date, birth_year=None, health_status=None):
        super().__init__(name, 'Livestock')
        self.species = species
        self.breed = breed
        self.purchase_date = purchase_date
        self.birth_year = birth_year
        self.health_status = health_status

class MaintenanceRecord(db.Model):
    __tablename__ = 'maintenance_records'
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date, nullable=False)
    cost = db.Column(db.Float)
    technician = db.Column(db.String(100))  # Technician name or company

    def __init__(self, item_id, description, date, cost=None, technician=None):
        self.item_id = item_id
        self.description = description
        self.date = date
        self.cost = cost
        self.technician = technician

class Document(db.Model):
    __tablename__ = 'documents'
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    filename = db.Column(db.String(255), nullable=False)
    file_url = db.Column(db.String(255), nullable=False)
    upload_date = db.Column(db.Date, nullable=False)

    def __init__(self, item_id, filename, file_url, upload_date):
        self.item_id = item_id
        self.filename = filename
        self.file_url = file_url
        self.upload_date = upload_date

class Expense(db.Model):
    __tablename__ = 'expenses'
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
    receipt_url = db.Column(db.String(255))  # URL to a receipt or proof of purchase

    def __init__(self, item_id, description, amount, date, receipt_url=None):
        self.item_id = item_id
        self.description = description
        self.amount = amount
        self.date = date
        self.receipt_url = receipt_url

class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    filename = db.Column(db.String(255), nullable=False)
    file_url = db.Column(db.String(255), nullable=False)
    upload_date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(255))  # Optional description of the image

    def __init__(self, item_id, filename, file_url, upload_date, description=None):
        self.item_id = item_id
        self.filename = filename
        self.file_url = file_url
        self.upload_date = upload_date
        self.description = description

class Note(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_date = db.Column(db.Date, nullable=False, default=date.today)

    def __init__(self, item_id, content, created_date=None):
        self.item_id = item_id
        self.content = content
        self.created_date = created_date or date.today()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    
    def __init__(self, username, email, password_hash):
        self.username = username
        self.email = email
        self.password_hash = password_hash