from flask import Blueprint, request, jsonify
from app.models import Equipment, db

equipment_bp = Blueprint('equipment', __name__)

@equipment_bp.route('/', methods=['GET'])
def get_equipment():
    equipment_items = Equipment.query.all()
    return jsonify([item.to_dict() for item in equipment_items])

@equipment_bp.route('/<int:item_id>', methods=['GET'])
def get_equipment_item(item_id):
    item = Equipment.query.get_or_404(item_id)
    return jsonify(item.to_dict())

@equipment_bp.route('/', methods=['POST'])
def add_equipment():
    data = request.json
    equipment = Equipment(
        name=data['name'],
        serial_number=data['serial_number'],
        purchase_date=data['purchase_date'],
        warranty_expiry=data.get('warranty_expiry'),
        manufacturer=data.get('manufacturer'),
        model_number=data.get('model_number')
    )
    db.session.add(equipment)
    db.session.commit()
    return jsonify(equipment.to_dict()), 201

@equipment_bp.route('/<int:item_id>', methods=['PUT'])
def update_equipment(item_id):
    data = request.json
    equipment = Equipment.query.get_or_404(item_id)
    equipment.serial_number = data.get('serial_number', equipment.serial_number)
    equipment.purchase_date = data.get('purchase_date', equipment.purchase_date)
    equipment.warranty_expiry = data.get('warranty_expiry', equipment.warranty_expiry)
    equipment.manufacturer = data.get('manufacturer', equipment.manufacturer)
    equipment.model_number = data.get('model_number', equipment.model_number)
    db.session.commit()
    return jsonify(equipment.to_dict())

@equipment_bp.route('/<int:item_id>', methods=['DELETE'])
def delete_equipment(item_id):
    equipment = Equipment.query.get_or_404(item_id)
    db.session.delete(equipment)
    db.session.commit()
    return jsonify({'message': 'Equipment deleted'})
