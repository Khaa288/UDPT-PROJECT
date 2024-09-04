from datetime import datetime
from flask import jsonify, request, Response, json, Blueprint
from marshmallow import ValidationError
from sqlalchemy import null
from src.models.participant_model import Participant

participant = Blueprint("participant", __name__)

@participant.route('',methods =["GET"])
def list():
    participants = Participant.get_all_ParticiPant()
    return jsonify(participants)

# Route to get participants by ActivityId (GET)
@participant.route('/activity/<activity_id>', methods=["GET"])
def get_participants_by_activity_id(activity_id):
    try:
        participants = Participant.get_Participant_by_ActivityId(activity_id)
        return jsonify(participants), 200 if participants else 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get participants by EmployeeId (GET)
@participant.route('/employee/<int:employee_id>', methods=["GET"])
def get_participants_by_employee_id(employee_id):
    try:
        participants = Participant.get_Participant_by_EmployeeId(employee_id)
        return jsonify(participants), 200 if participants else 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to participate in an activity (POST)
@participant.route('/participate', methods=["POST"])
def participate_activity():
    try:
        # Parse JSON data from the request
        data = request.get_json()

        # Validate the required fields
        activity_name = data.get("ActivityName")
        end_date = data.get("EndDate")
        employee_id = data.get("EmployeeId")
        strava_id = data.get("StravaId")

        if not all([activity_name, end_date, employee_id, strava_id]):
            return jsonify({"error": "Missing required fields."}), 400

        # Convert EndDate to datetime object
        end_date = datetime.fromisoformat(end_date)

        # Create a new participant
        new_participant = Participant.participate_Activity(
            activity_name=activity_name,
            end_date=end_date,
            employee_id=employee_id,
            strava_id=strava_id
        )

        if new_participant:
            return jsonify(new_participant), 201
        else:
            return jsonify({"error": "Failed to create participant."}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500