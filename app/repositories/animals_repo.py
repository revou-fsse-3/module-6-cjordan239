from app.models.animal import Animal
from flask import request
from app.utils.database import db

class animals_repo():

    def get_list_animals():
        animals = Animal.query.all()
        return animals

    def create_animals(self, animals):
        db.session.add(animals)
        db.session.commit()
        return animals

    