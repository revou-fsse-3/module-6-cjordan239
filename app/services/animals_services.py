from app.repositories import animals_repo
from app.models.animal import Animal



class animal_services:
    def __init__(self):
      self.customer_repo = animals_repo()

    def get_animal():
        animals = animals_repo.get_list_animals()
        return animals

    def create_animal(self, animal_data_dto):
        animals = Animal()
     
        animals.name = animal_data_dto.name
        animals.gender = animal_data_dto.gender
        animals.age = animal_data_dto.age
        animals.diet = animal_data_dto.diet

        created_animal = self.animals_repo.create_animals(animals)
        return created_animal.as_dict()