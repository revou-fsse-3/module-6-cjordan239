# def test_get_employee(test_app):  
#     response = test_app.get("/employee/")
#     assert len(response.json['data']) == 3


# def test_post_employee(test_app):
#     data = {
#         "name": "John Doe",
#         "phone": "123456789",
#         "gender": "Male",
#         "birthday": "1990-01-01",
#         "shift": "Day"
#     }

#     response = test_app.post("/employee/", json=data)
#     assert response.status_code == 201


# def test_post_employee_400(test_app):
#     data = {}
#     response = test_app.post("/employee/", json=data)
#     assert response.status_code == 400


# def test_delete_employee(test_app):
#     data = {}
#     response = test_app.delete("/employee/1", json=data)
#     assert response.status_code == 200


# def test_put_employee(test_app):
#     data = {
#         "name": "Jane Doe",
#         "phone": "987654321",
#         "gender": "Female",
#         "birthday": "1995-01-01",
#         "shift": "Night"
#     }
#     response = test_app.put("/employee/1", json=data)
#     assert response.status_code == 200
