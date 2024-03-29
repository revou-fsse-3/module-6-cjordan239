from ...utils.database import db
from flask import Blueprint, jsonify, request
from ...models.employees import Employee
from ...utils.api_response import api_response
from ...services import employees_services

employee_blueprint = Blueprint('employee_endpoint', __name__)

@employee_blueprint.route("/", methods=["GET"])
def get_employees():
    try:
        employees = employees_services.get_employee()
        
        return api_response(
            status_code=200,
            message="succes",
            data=[employee.as_dict() for employee in employees]
        )
    
    except Exception as e:
        return str(e), 500

@employee_blueprint.route("/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):
    try:
        employee = Employee.query.get(employee_id)

        if not employee:
            return "Employee not found", 404

        data = request.json
        employee.name = data.get("name", employee.name)
        employee.phone = data.get("phone", employee.phone)
        employee.gender = data.get("gender", employee.gender)
        employee.birthday = data.get("birthday", employee.birthday)
        employee.shift = data.get("shift", employee.shift)

        db.session.commit()

        return 'Update successful', 200
    except Exception as e:
        return str(e), 500

@employee_blueprint.route("/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    try:
        employee = Employee.query.get(employee_id)

        if not employee:
            return "Employee not found", 404

        db.session.delete(employee)
        db.session.commit()

        return 'Delete successful', 200
    except Exception as e:
        return str(e), 500
    
@employee_blueprint.route('/', methods=["POST"])
def create_employee():
    try:
        data = request.json
        new_employee = Employee()
        new_employee.name = data["name"]
        new_employee.phone = data["phone"]
        new_employee.gender = data["gender"]
        new_employee.birthday = data["birthday"]
        new_employee.shift = data["shift"]
        db.session.add(new_employee)
        db.session.commit()
        return 'Employee created successfully', 201
    except Exception as e:
        return str(e), 500

