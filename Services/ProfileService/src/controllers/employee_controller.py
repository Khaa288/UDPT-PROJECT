from flask import jsonify, request, Response, json, Blueprint
from marshmallow import ValidationError
from src.models.employee_model import Employee
from src.models.dtos.employee_request_dto import EmployeeUpdateRequestDto

# user controller blueprint to be registered with api blueprint
employee = Blueprint("employee", __name__)

@employee.route('/', methods = ["GET"])
def list():
    employees = Employee.get_all()
    return jsonify(employees)

@employee.route('/<employee_id>', methods = ["GET"])
def get(employee_id):
    employee = Employee.get_by_id(employee_id)
    return jsonify(employee)

@employee.route('/<employee_id>', methods = ["PUT"])
def update(employee_id):
    # employee = Employee.get_by_id(employee_id)

    # if employee is None:
    #     return 'thua'
    
    dto = EmployeeUpdateRequestDto()
    result = request.get_json()

    try:
        validate = dto.load(result)
        print(result.get('employeeId'))
        print(result.get('firstName'))
        
        a = Employee.update(result.get('employeeId'))

        print(validate)
       
    except ValidationError as err:
        print(err.messages)
        return 'Invalid input!'
    
    return 'Success'

@employee.route('/<employee_id>/deactivate', methods = ["POST"])
def deactivate(employee_id):
    return