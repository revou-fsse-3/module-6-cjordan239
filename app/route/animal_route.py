from flask import Blueprint, jsonify, request
from ..utils.database import db
from ..models.animal import Animal

animal_blueprint = Blueprint('animal_endpoint', __name__)

@animal_blueprint.route("/", methods=["GET"])
def get_animals():
    try:
        animals = Animal.query.all()
        animal_dicts = [animal.as_dict() for animal in animals]
        return jsonify(animal_dicts), 200
    except Exception as e:
        return jsonify({'error': 'Something went wrong'}), 500


@animal_blueprint.route("/<int:animal_id>", methods=["PUT"])
def update_animal(animal_id):
    try:
        animal = Animal.query.get(animal_id)

        if not animal:
            return "Animal not found", 404

        data = request.json

        animal.name = data.get("name", animal.name)
        animal.gender = data.get("gender", animal.gender)
        animal.age = data.get("age", animal.age)
        animal.diet = data.get("diet", animal.diet)

        db.session.commit()

        return 'Update successful', 200
    except Exception as e:
        return str(e), 500


@animal_blueprint.route("/<int:animal_id>", methods=["DELETE"])
def delete_animal(animal_id):
    try:
        animal = Animal.query.get(animal_id)

        if not animal:
            return "Animal not found", 404

        db.session.delete(animal)
        db.session.commit()

        return 'Delete successful', 200
    except Exception as e:
        return str(e), 500
    
@animal_blueprint.route('/animals', methods=["POST"])
def create_animal():
    try:
        data = request.json
        new_animal = Animal(
            name=data.get("name"),
            gender=data.get("gender"),
            age=data.get("age"),
            diet=data.get("diet")
        )
        db.session.add(new_animal)
        db.session.commit()
        return 'animal created'
    except Exception as e:
        return str(e), 500

