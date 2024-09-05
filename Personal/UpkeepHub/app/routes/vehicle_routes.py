from flask import Blueprint, request, jsonify
from app.models import Vehicle, db

vehicles_bp = Blueprint('vehicles', __name__)

@vehicles_bp.route('/', methods=['GET'])
def get_vehicles():
    vehicles = Vehicle.query.all()
    return jsonify([vehicle.to_dict() for vehicle in vehicles])

@vehicles_bp.route('/<int:item_id>', methods=['GET'])
def get_vehicle(item_id):
    vehicle = Vehicle.query.get_or_404(item_id)
    return jsonify(vehicle.to_dict())

@vehicles_bp.route('/', methods=['POST'])
def add_vehicle():
    data = request.json
    vehicle = Vehicle(
        name=data['name'],
        make=data['make'],
        model=data['model'],
        year=data['year'],
        color=data['color'],
        year_purchased=data['year_purchased'],
        vin=data.get('vin'),
        mileage=data.get('mileage')
    )
    db.session.add(vehicle)
    db.session.commit()
    return jsonify(vehicle.to_dict()), 201

@vehicles_bp.route('/<int:item_id>', methods=['PUT'])
def update_vehicle(item_id):
    data = request.json
    vehicle = Vehicle.query.get_or_404(item_id)
    
    vehicle.name = data.get('name', vehicle.name)
    vehicle.make = data.get('make', vehicle.make)
    vehicle.model = data.get('model', vehicle.model)
    vehicle.year = data.get('year', vehicle.year)
    vehicle.color = data.get('color', vehicle.color)
    vehicle.year_purchased = data.get('year_purchased', vehicle.year_purchased)
    vehicle.vin = data.get('vin', vehicle.vin)
    vehicle.mileage = data.get('mileage', vehicle.mileage)
    
    db.session.commit()
    return jsonify(vehicle.to_dict())

@vehicles_bp.route('/<int:item_id>', methods=['DELETE'])
def delete_vehicle(item_id):
    vehicle = Vehicle.query.get_or_404(item_id)
    db.session.delete(vehicle)
    db.session.commit()
    return jsonify({'message': 'Vehicle deleted successfully'})
