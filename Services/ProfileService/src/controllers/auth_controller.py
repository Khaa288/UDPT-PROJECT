from flask import request, Response, json, Blueprint, jsonify
from marshmallow import ValidationError
from src.dtos.login_request_dto import LoginRequestDto 
from src.models.user_model import User
from src.models.employee_model import Employee

# user controller blueprint to be registered with api blueprint
auth = Blueprint("auth", __name__)

# route for login api/users/signin
@auth.route('/login', methods = ["POST"])
def handle_login():
    dto = LoginRequestDto()
    request_body = request.get_json()

    try:
        validated_body = dto.load(request_body)
        user = User.getUser(validated_body)
        employee = Employee.get_by_user_id(user.UserId)
        return jsonify(employee)
       
    except ValidationError as err:
        return 'Invalid input!'