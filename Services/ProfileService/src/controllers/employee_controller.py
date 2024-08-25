from flask import jsonify, request, Response, json, Blueprint
from marshmallow import ValidationError
from src.models.employee_model import Employee
from src.dtos.employee_request_dto import EmployeeUpdateRequestDto

# user controller blueprint to be registered with api blueprint
employee = Blueprint("employee", __name__)

@employee.route('/page', methods = ["GET"])
def get_employee_pages():
    return jsonify(Employee.get_pages())

@employee.route('', methods = ["GET"])
def list():
    params = {
        "firstName": request.args.get('firstName'),
        "idCardNum": request.args.get('idCardNum'),
        "jobTitle": request.args.get('jobTitle'),
        "page": request.args.get('page'),
        "pageSize": request.args.get('pageSize')
    }

    employees = Employee.get_all(params)
    return jsonify(employees)

@employee.route('/<employee_id>', methods = ["GET"])
def get(employee_id):
    employee = Employee.get_by_id(employee_id)
    return jsonify(employee)

@employee.route('/<employee_id>', methods = ["PUT"])
def update(employee_id):
    dto = EmployeeUpdateRequestDto()
    request_body = request.get_json()
    
    try:
        validated_body = dto.load(request_body)
        Employee.update(employee_id, validated_body)
       
    except ValidationError as err:
        return 'Invalid input!'
    
    return 'Success'

@employee.route('/<employee_id>/deactivate', methods = ["POST"])
def deactivate(employee_id):
    return jsonify(Employee.deactivate(employee_id))