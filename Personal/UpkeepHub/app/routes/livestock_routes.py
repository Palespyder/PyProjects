from flask import Blueprint, request, jsonify
from app.models import Livestock, db

livestock_bp = Blueprint('livestock', __name__)

@livestock_bp.route('/', methods=['GET'])
def get_livestock():
    livestock_items = Livestock.query.all()
    return jsonify([item.to_dict() for item in livestock_items])

@livestock_bp.route('/<int:item_id>', methods=['GET'])
def get_livestock_item(item_id):
    item = Livestock.query.get_or_404(item_id)
    return jsonify(item.to_dict())

@livestock_bp.route('/', methods=['POST'])
def add_livestock():
    data = request.json
    livestock = Livestock(
        name=data['name'],
        species=data['species'],
        breed=data['breed'],
        purchase_date=data['purchase_date'],
        birth_year=data.get('birth_year'),
        health_status=data.get('health_status')
    )
    db.session.add(livestock)
    db.session.commit()
    return jsonify(livestock.to_dict()), 201

@livestock_bp.route('/<int:item_id>', methods=['PUT'])
def update_livestock(item_id):
    data = request.json
    livestock = Livestock.query.get_or_404(item_id)
    livestock.species = data.get('species', livestock.species)
    livestock.breed = data.get('breed', livestock.breed)
    livestock.purchase_date = data.get('purchase_date', livestock.purchase_date)
    livestock.birth_year = data.get('birth_year', livestock.birth_year)
    livestock.health_status = data.get('health_status', livestock.health_status)
    db.session.commit()
    return jsonify(livestock.to_dict())

@livestock_bp.route('/<int:item_id>', methods=['DELETE'])
def delete_livestock(item_id):
    livestock = Livestock.query.get_or_404(item_id)
    db.session.delete(livestock)
    db.session.commit()
    return jsonify({'message': 'Livestock deleted'})
