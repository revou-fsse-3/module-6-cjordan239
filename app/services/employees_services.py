from ..repositories import employees_repo

def get_employee():
    employee = employees_repo.get_list_employees()
    return employee