from flask import Blueprint
from src.controllers.activity_controller import activity
from src.controllers.participant_controller import participant
# main blueprint to be registered with application
api = Blueprint('api', __name__)

# register user with api blueprint

api.register_blueprint(activity, url_prefix="/activity")
api.register_blueprint(participant, url_prefix="/participant")
