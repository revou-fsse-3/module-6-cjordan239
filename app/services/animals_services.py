from ..repositories import animals_repo

def get_animal():
    animals = animals_repo.get_list_animals()
    return animals