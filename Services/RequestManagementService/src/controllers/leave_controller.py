from flask import jsonify, request, json, Blueprint
from marshmallow import ValidationError
from src.dtos.leave_request_dto import LeaveRequestDto
from src.models.leave_model import Leave
from src.models.timesheet_model import Timesheet
from src.models.leave_request_model import LeaveRequest
from src.utils import RequestStatus
from bson import json_util

# user controller blueprint to be registered with api blueprint
leave = Blueprint("leave", __name__)

@leave.route('/page', methods = ["GET"])
def get_leave_pages():
    return jsonify(Leave.get_pages())

@leave.route('', methods = ["GET"])
def list_leaves():
    params = {
        "page": request.args.get('page'),
        "pageSize": request.args.get('pageSize')
    }

    leaves = Leave.get_all(params)

    if leaves:
        return json.loads(json_util.dumps(leaves))
    
    return []

@leave.route('/request/page', methods = ["GET"])
def get_leave_request_pages():
    params = {
        "employeeId": request.args.get('employeeId')
    }

    return jsonify(LeaveRequest.get_pages(params))

@leave.route('/request', methods = ["GET"])
def list_leave_requests():
    params = {
        "page": request.args.get('page'),
        "pageSize": request.args.get('pageSize'),
        "employeeId": request.args.get('employeeId')
    }

    leave_requests = LeaveRequest.get_all(params)

    if leave_requests:
        return json.loads(json_util.dumps(leave_requests))
    
    return []

@leave.route('/request', methods = ["POST"])
def request_leave():
    dto = LeaveRequestDto()
    request_body = request.get_json()

    try:
        validated_body = dto.load(request_body)
        leave_request = LeaveRequest.create(validated_body)
        return jsonify(leave_request)
       
    except ValidationError as err:
        return 'Invalid input!'
    
@leave.route('/request/<request_id>/accept', methods = ["POST"])
def accept_leave(request_id):
    # Change leave request status
    isCreated = json.loads(json_util.dumps(LeaveRequest.update_status(request_id, RequestStatus.ACCEPTED)))
  
    # Get accepted_leave_request and insert to leave collection then update timesheet
    if isCreated:
        accepted_leave_request = LeaveRequest.get_by_id(request_id)
        update_timesheet = Timesheet.upsert_leave_days(
            accepted_leave_request["Employee"], 
            accepted_leave_request["FromDate"], 
            accepted_leave_request["ToDate"]
        )
        created_leave = Leave.create(accepted_leave_request)
    
    return json.loads(json_util.dumps(accepted_leave_request))

@leave.route('/request/<request_id>/deny', methods = ["POST"])
def deny_leave(request_id):
    isDenied = LeaveRequest.update_status(request_id, RequestStatus.DENIED)

    if isDenied:
        denied_leave_request = LeaveRequest.get_by_id(request_id)

    return json.loads(json_util.dumps(denied_leave_request))