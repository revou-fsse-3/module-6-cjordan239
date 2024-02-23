
def test_get_animal(test_app):  
    response = test_app.get("/animals/")
    assert len(response.json['data']) == 3


def test_post_animal(test_app):
    data = {
        
        "user_id": "1",
        "name": "lilo",
        "gender": "female",
        "age": "25",
        "diet": "herbivore"
    }

    response = test_app.put("/animals/1", json= data)
    assert response.status_code == 200

def test_post_animal_400(test_app):
    data = {}
    response = test_app.put("/animals/1", json= data)
    assert response.status_code == 400

def test_delete_animal(test_app):
    data = {}
    response = test_app.put("/animals/1", json=data)
    assert response.status_code == 200

def test_put_animal(test_app):
    data = {
        
        "name": "bongo",
        "gender": "Male",
        "age": 3,
        "diet": "Herbivore"
    }
    response = test_app.put("/animals/1", json=data)
    assert response.status_code == 200
