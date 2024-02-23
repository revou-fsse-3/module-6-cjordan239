from app.models.animal import Animal
from flask import request
from app.utils.database import db

def get_list_animals():
    animals = Animal.query.all()
    return animals

def post_list_animals(data):
    new_animal = Animal(
        name=data["name"],
        gender=data["gender"],
        age=data["age"],
        diet=data["diet"]
    )
    db.session.add(new_animal)
    db.session.commit()

    return new_animal

    