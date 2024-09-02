from flask import jsonify, request, json, Blueprint
from marshmallow import ValidationError
from src.models.attendance_model import Attendance
from src.dtos.attendance_request_dto import CheckInRequestDto, CheckOutRequestDto 
from bson import json_util

# user controller blueprint to be registered with api blueprint
attendance = Blueprint("attendance", __name__)

@attendance.route('/employee/<employee_id>/current', methods = ["GET"])
def getCurrentAttendance(employee_id):
    return json.loads(json_util.dumps(Attendance.get_current_attendance(employee_id)))

@attendance.route('/check-in', methods = ["POST"])
def checkIn():
    dto = CheckInRequestDto()
    request_body = request.get_json()

    try:
        validated_body = dto.load(request_body)
        check_in_request = Attendance.check_in(validated_body)
        return jsonify(check_in_request)
       
    except ValidationError as err:
        return 'Invalid input!'
    
@attendance.route('/check-out', methods = ["POST"])
def checkOut():
    dto = CheckOutRequestDto()
    request_body = request.get_json()

    try:
        validated_body = dto.load(request_body)
        check_out_request = Attendance.check_out(validated_body)
        return jsonify(check_out_request)
       
    except ValidationError as err:
        return 'Invalid input!'