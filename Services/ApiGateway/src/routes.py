from flask import Blueprint
from src.controllers.profile_service_controller import auth, employee
from src.controllers.request_management_service_controller import attendance, wfh, leave, timesheet
from src.controllers.activity_service_controller import activity ,participant
# main blueprint to be registered with application
api = Blueprint('api', __name__)

# ACTIVITY SERVICE API
api.register_blueprint(activity, url_prefix="/activity")
api.register_blueprint(participant, url_prefix="/participant")
# PROFILE SERVICE API 
api.register_blueprint(auth, url_prefix="/auth")
api.register_blueprint(employee, url_prefix="/employee")

# REQUEST MANAGEMENT SERVICE API
api.register_blueprint(attendance, url_prefix="/attendance")
api.register_blueprint(wfh, url_prefix="/wfh")
api.register_blueprint(leave, url_prefix="/leave")
api.register_blueprint(timesheet, url_prefix="/timesheet")