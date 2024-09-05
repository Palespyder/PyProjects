from flask import Blueprint, request, jsonify
from app.models import Pet, db

pets_bp = Blueprint('pets', __name__)

@pets_bp.route('/', methods=['GET'])
def get_pets():
    pets = Pet.query.all()
    return jsonify([pet.to_dict() for pet in pets])

@pets_bp.route('/<int:item_id>', methods=['GET'])
def get_pet(item_id):
    pet = Pet.query.get_or_404(item_id)
    return jsonify(pet.to_dict())

@pets_bp.route('/', methods=['POST'])
def add_pet():
    data = request.json
    pet = Pet(
        name=data['name'],
        species=data['species'],
        breed=data['breed'],
        birth_year=data.get('birth_year'),
        weight=data.get('weight'),
        microchip_number=data.get('microchip_number')
    )
    db.session.add(pet)
    db.session.commit()
    return jsonify(pet.to_dict()), 201

@pets_bp.route('/<int:item_id>', methods=['PUT'])
def update_pet(item_id):
    data = request.json
    pet = Pet.query.get_or_404(item_id)
    pet.species = data.get('species', pet.species)
    pet.breed = data.get('breed', pet.breed)
    pet.birth_year = data.get('birth_year', pet.birth_year)
    pet.weight = data.get('weight', pet.weight)
    pet.microchip_number = data.get('microchip_number', pet.microchip_number)
    db.session.commit()
    return jsonify(pet.to_dict())

@pets_bp.route('/<int:item_id>', methods=['DELETE'])
def delete_pet(item_id):
    pet = Pet.query.get_or_404(item_id)
    db.session.delete(pet)
    db.session.commit()
    return jsonify({'message': 'Pet deleted'})
