from ..repositories import animals_repo

def get_animal():
    animals = animals_repo.get_list_animals()
    return animals

def post_animal(data):
    created_animal = animals_repo.create_animals(data)
    return created_animal