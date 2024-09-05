from flask import Blueprint, request, jsonify
from app.models import Outbuilding, db

outbuildings_bp = Blueprint('outbuildings', __name__)

@outbuildings_bp.route('/', methods=['GET'])
def get_outbuildings():
    outbuildings = Outbuilding.query.all()
    return jsonify([building.to_dict() for building in outbuildings])

@outbuildings_bp.route('/<int:item_id>', methods=['GET'])
def get_outbuilding(item_id):
    building = Outbuilding.query.get_or_404(item_id)
    return jsonify(building.to_dict())

@outbuildings_bp.route('/', methods=['POST'])
def add_outbuilding():
    data = request.json
    outbuilding = Outbuilding(
        name=data['name'],
        structure_type=data['structure_type'],
        construction_date=data.get('construction_date'),
        dimensions=data.get('dimensions')
    )
    db.session.add(outbuilding)
    db.session.commit()
    return jsonify(outbuilding.to_dict()), 201

@outbuildings_bp.route('/<int:item_id>', methods=['PUT'])
def update_outbuilding(item_id):
    data = request.json
    outbuilding = Outbuilding.query.get_or_404(item_id)
    outbuilding.structure_type = data.get('structure_type', outbuilding.structure_type)
    outbuilding.construction_date = data.get('construction_date', outbuilding.construction_date)
    outbuilding.dimensions = data.get('dimensions', outbuilding.dimensions)
    db.session.commit()
    return jsonify(outbuilding.to_dict())

@outbuildings_bp.route('/<int:item_id>', methods=['DELETE'])
def delete_outbuilding(item_id):
    outbuilding = Outbuilding.query.get_or_404(item_id)
    db.session.delete(outbuilding)
    db.session.commit()
    return jsonify({'message': 'Outbuilding deleted'})
