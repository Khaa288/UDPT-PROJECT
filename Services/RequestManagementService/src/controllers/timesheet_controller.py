from flask import jsonify, request, json, Blueprint
from marshmallow import ValidationError
from src.utils import RequestStatus
from src.models.timesheet_model import Timesheet
from src.models.timesheet_update_request_model import TimesheetUpdateRequest
from src.dtos.update_timesheet_workhour_dto import UpdateTimesheetWorkHourtDto 
from src.dtos.update_timesheet_request_dto import UpdateTimesheetRequestDto
from bson import json_util

# user controller blueprint to be registered with api blueprint
timesheet = Blueprint("timesheet", __name__)

@timesheet.route('/page', methods = ["GET"])
def get_timesheet_pages():
    return jsonify(Timesheet.get_pages())

@timesheet.route('', methods = ["GET"])
def list_timesheets():
    params = {
        "page": request.args.get('page'),
        "pageSize": request.args.get('pageSize')
    }

    timesheets = Timesheet.get_all(params)

    if timesheets:
        return json.loads(json_util.dumps(timesheets))
    
    return []

@timesheet.route('/request/page', methods = ["GET"])
def get_timehsheet_update_request_pages():
    return jsonify(TimesheetUpdateRequest.get_pages())

@timesheet.route('/request', methods = ["GET"])
def list_timesheet_update_request():
    params = {
        "page": request.args.get('page'),
        "pageSize": request.args.get('pageSize')
    }

    timesheet_update_requests = TimesheetUpdateRequest.get_all(params)

    if timesheet_update_requests:
        return json.loads(json_util.dumps(timesheet_update_requests))
      
    return []

@timesheet.route('/<timesheet_id>', methods = ["GET"])
def get_timesheet(timesheet_id):
    return json.loads(json_util.dumps(Timesheet.get_by_id(timesheet_id)))

@timesheet.route('/request', methods=["POST"])
def request_update_timesheet():
    dto = UpdateTimesheetRequestDto()
    request_body = request.get_json()

    try:
        validated_body = dto.load(request_body)
        timesheet_update_request = TimesheetUpdateRequest.create(validated_body)
        return jsonify(timesheet_update_request)
       
    except ValidationError as err:
        return 'Invalid input!'

@timesheet.route('/<timesheet_id>', methods = ["POST"])
def update_timesheet_workHour(timesheet_id):
    dto = UpdateTimesheetWorkHourtDto()
    request_body = request.get_json()

    try:
        validated_body = dto.load(request_body)
        timesheet_update_request = Timesheet.upsert_workhour(timesheet_id, validated_body)
        return jsonify(timesheet_update_request)
       
    except ValidationError as err:
        return 'Invalid input!'
    
@timesheet.route('/request/<request_id>/accept', methods=["POST"])
def accept_update_timesheet_request(request_id):
    # Change update timesheet request status
    isCreated = json.loads(json_util.dumps(TimesheetUpdateRequest.update_status(request_id, RequestStatus.ACCEPTED)))
  
    # Get accepted_timesheet_update_request and upsert to timesheet collection
    if isCreated:
        accepted_timesheet_update_request = TimesheetUpdateRequest.get_by_id(request_id)
        upserted_timesheet = Timesheet.upsert(
            accepted_timesheet_update_request["Employee"],
            accepted_timesheet_update_request["Date"],
            accepted_timesheet_update_request["NewWorkHour"]
        )
    
    return json.loads(json_util.dumps(accepted_timesheet_update_request))

@timesheet.route('/request/<request_id>/deny', methods=["POST"])
def deny_update_timesheet_request(request_id):
    isDenied = TimesheetUpdateRequest.update_status(request_id, RequestStatus.DENIED)

    if isDenied:
        denied_leave_request = TimesheetUpdateRequest.get_by_id(request_id)

    return json.loads(json_util.dumps(denied_leave_request))