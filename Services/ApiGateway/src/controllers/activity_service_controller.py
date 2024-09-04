from datetime import datetime
from flask import jsonify, request, Response, json, Blueprint
from marshmallow import ValidationError
import py_eureka_client.eureka_client as eureka_client
import urllib.parse
activity = Blueprint("activity", __name__)
participant = Blueprint("participant", __name__)
### Activity API
@activity.route('', methods = ["GET"])
def list():
    activities = eureka_client.do_service('activity_service',f"/api/activity")
    return activities
@activity.route('/<activity_id>')
def get_activity_id(activity_id):
    activity = eureka_client.do_service('activity_service',f"/api/activity/{activity_id}")
    return activity
@activity.route('/add', methods=["POST"])
def create():
    request_body = request.get_json()

    res = eureka_client.do_service(
        app_name = "activity_service", 
        service = f"/api/activity/add", 
        method="POST",
        headers=({"Content-Type": "application/json"}),
        data=request_body
    )

    return res

@activity.route('/update/<activity_id>', methods=["PUT"])
def update_activity(activity_id):
    request_body = request.get_json()

    res = eureka_client.do_service(
        app_name = "activity_service", 
        service = f"/api/activity/update/{activity_id}", 
        method="PUT",
        headers=({"Content-Type": "application/json"}),
        data=request_body
    )

    return res

### Participant API
# Route to get participants by ActivityId (GET)
@participant.route('',methods =["GET"])
def list():
    participants = eureka_client.do_service('activity_service',f"/api/participant")
    return participants
@participant.route('/activity/<activity_id>', methods=["GET"])
def get_participants_by_activity_id(activity_id):
    try:
        participants = eureka_client.do_service('activity_service', f"/api/participant/activity/{activity_id}")
        return participants, 200 if participants else 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get participants by EmployeeId (GET)
@participant.route('/employee/<int:employee_id>', methods=["GET"])
def get_participants_by_employee_id(employee_id):
    try:
        participants = eureka_client.do_service('activity_service',f"/api/participant/employee/{employee_id}")
        return participants , 200 if participants else 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
