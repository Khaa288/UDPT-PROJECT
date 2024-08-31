from flask import jsonify, request, json, Blueprint
from marshmallow import ValidationError
from src.models.wfh_model import WFH
from src.models.wfh_request_model import WfhRequest
from src.dtos.wfh_request_dto import WfhRequestDto
from src.utils import RequestStatus
from bson import json_util

# user controller blueprint to be registered with api blueprint
wfh = Blueprint("wfh", __name__)

@wfh.route('/page', methods = ["GET"])
def get_wfh_pages():
    return jsonify(WFH.get_pages())

@wfh.route('', methods = ["GET"])
def list_wfhs():
    params = {
        "page": request.args.get('page'),
        "pageSize": request.args.get('pageSize')
    }

    return json.loads(json_util.dumps(WFH.get_all(params)))

@wfh.route('/request/page', methods = ["GET"])
def get_wfh_request_pages():
    return jsonify(WfhRequest.get_pages())

@wfh.route('/request', methods = ["GET"])
def list_wfh_requests():
    params = {
        "page": request.args.get('page'),
        "pageSize": request.args.get('pageSize'),
        "employeeId": request.args.get('employeeId')
    }

    return json.loads(json_util.dumps(WfhRequest.get_all(params)))

@wfh.route('/request', methods = ["POST"])
def request_wfh():
    dto = WfhRequestDto()
    request_body = request.get_json()

    try:
        validated_body = dto.load(request_body)
        wfh_request = WfhRequest.create(validated_body)
        return jsonify(wfh_request)
       
    except ValidationError as err:
        return 'Invalid input!'
    
@wfh.route('/request/<request_id>/accept', methods = ["POST"])
def accept_wfh(request_id):
    # Change wfh request status
    isCreated = json.loads(json_util.dumps(WfhRequest.update_status(request_id, RequestStatus.ACCEPTED)))
  
    # Get accepted_wfh_request and insert to leave collection
    if isCreated:
        accepted_wfh_request = WfhRequest.get_by_id(request_id)
        created_wfh = WFH.create(accepted_wfh_request)
    
    return json.loads(json_util.dumps(accepted_wfh_request))

@wfh.route('/request/<request_id>/deny', methods = ["POST"])
def deny_wfh(request_id):
    isDenied = WfhRequest.update_status(request_id, RequestStatus.DENIED)

    if isDenied:
        denied_leave_request = WfhRequest.get_by_id(request_id)

    return json.loads(json_util.dumps(denied_leave_request))