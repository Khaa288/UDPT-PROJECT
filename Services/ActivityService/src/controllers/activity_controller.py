from datetime import datetime
from flask import jsonify, request, Response, json, Blueprint
from marshmallow import ValidationError
from src.models.activity_model import Activity

# user controller blueprint to be registered with api blueprint
activity = Blueprint("activity", __name__)
@activity.route('', methods = ["GET"])
def list():
    activities = Activity.get_all_Activity()
    return jsonify(activities)
@activity.route('/<activity_id>')
def get_activity_id(activity_id):
    activity = Activity.get_activity_byId(activity_id)
    return jsonify(activity)

@activity.route('/add', methods=["POST"])
def create():
    try:
        # Parse JSON data from the request
        data = request.get_json()

        # Validate the required fields
        ActivityName = data.get("ActivityName")
        StartTime = data.get("StartTime")
        EndTime = data.get("EndTime")

        if not all([ActivityName, StartTime, EndTime]):
            return jsonify({"error": "Missing required fields."}), 400

        # Convert start_time and end_time to datetime objects
        StartTime = datetime.fromisoformat(StartTime)
        EndTime = datetime.fromisoformat(EndTime)


        # Create a new activity
        new_activity = Activity.create_Activity(ActivityName, StartTime, EndTime)

        if new_activity:
            return jsonify(new_activity), 201
        else:
            return jsonify({"error": "Failed to create activity."}), 500

    except ValidationError as e:
        return jsonify({"error": e.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@activity.route('/update/<activity_id>', methods=["PUT"])
def update_activity(activity_id):
    try:
        # Parse JSON data from the request
        data = request.get_json()

        # Validate the required fields
        updated_activity = {
            "ActivityName": data.get("ActivityName"),
            "StartTime": data.get("StartTime"),
            "EndTime": data.get("EndTime")
        }

        if not all(updated_activity.values()):
            return jsonify({"error": "Missing required fields."}), 400

        # Convert StartTime and EndTime to datetime objects
        updated_activity["StartTime"] = datetime.fromisoformat(updated_activity["StartTime"])
        updated_activity["EndTime"] = datetime.fromisoformat(updated_activity["EndTime"])

        # Update the activity
        result = Activity.update_Activity(activity_id, updated_activity)

        if result:
            return jsonify({"message": "Activity updated successfully."}), 200
        else:
            return jsonify({"error": "Activity not found or failed to update."}), 404

    except ValidationError as e:
        return jsonify({"error": e.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500