from app.models.employees import Employee

def get_list_employees():
    employee = Employee.query.all()
    return employee