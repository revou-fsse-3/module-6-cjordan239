from app.models.animal import Animal
from app.repositories import animals_repo
from app.services import animals_services
from app.controller.schema.create_animal_request import Create_animal_request



def test_get_list_animmal_success(test_app, mocker):
   """service get animal success"""
   # Arrange
   mock_animal_data = [
      Animal(
         id=1, 
         name='miki', 
         age=12,
         gender='laki laki',
         diet="herbivore"),
      Animal(
         id=2, 
         name='miko', 
         age=5, 
         gender='laki laki',
         diet="herbivore"),
      Animal(
         id=3,   
         name='mika', 
         age=16, 
         gender='laki laki', 
         diet="carnivore"),
      
   ]
   mocker.patch.object(animals_repo, 'get_list_animals',
                     return_value=mock_animal_data)
   
   # Act
   with test_app.test_request_context():
      animal_service = animals_services().get_animal()

   # Assert
   assert len(animal_service) == 2
   assert animal_service[0]['name'] == 'miki'
   assert animal_service[1]['gender'] == 'laki laki'



def test_create_animal_success(test_app, mocker):
    """Test creation of animal successfully"""

    # Arrange
    mock_animal_data = Animal(
        id=1, 
        name='karina', 
        age=16,
        gender='perempuan',
        diet="herbivore"
    )
    mocker.patch.object(animals_repo, 'create_animals', return_value=mock_animal_data)
    
    create_dto = Create_animal_request(
        id=3, 
        name='mikasa', 
        age=14, 
        gender='laki laki', 
        diet="carnivore"
    )
    
    # Act
    with test_app.test_request_context():
        animal_service_create = animals_services.create_animal(create_dto)
    
    # Assert
    assert animal_service_create.id == 1
    assert animal_service_create.name == 'karina'
    assert animal_service_create.gender == 'perempuan'
    assert animal_service_create.age == 16
    assert animal_service_create.diet == 'herbivore'
