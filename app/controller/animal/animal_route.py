from flask import Blueprint, jsonify, request
from ...utils.database import db
from ...models.animal import Animal
from ...utils.api_response import api_response
from ...services import animals_services


animal_blueprint = Blueprint('animal_endpoint', __name__)

@animal_blueprint.route("/", methods=["GET"])
def get_list_animals():
    try:
        animals = animals_services.get_animal()
        
        return api_response(
            status_code=200,
            message="succes",
            data=[animal.as_dict() for animal in animals]
        )
    
    except Exception as e:
        return str(e), 500

@animal_blueprint.route("/<int:animal_id>", methods=["PUT"])
def update_animal(animal_id):
    try:
        animal = Animal.query.get(animal_id)

        if not animal:
            return "Animal not found", 404

        data = request.json

        if not data:
            return "data not found", 400

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

@animal_blueprint.route('/', methods=["POST"])
def create_animal():
    try: 
        data = request.json
        created_animal = animals_services.post_animal(data)
        return api_response(
            status_code=200,
            message="animal created",
            data=created_animal.as_dict()
        )
    except Exception as e:
        return str(e), 500


