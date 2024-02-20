from app.models.animal import Animal

def get_list_animals():
    animals = Animal.query.all()
    return animals