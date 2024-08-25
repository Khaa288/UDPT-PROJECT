from flask import Blueprint
from src.controllers.leave_controller import leave
from src.controllers.wfh_controller import wfh
from src.controllers.attendance_controller import attendance

# main blueprint to be registered with application
api = Blueprint('api', __name__)

# register user with api blueprint
api.register_blueprint(leave, url_prefix="/leave")
api.register_blueprint(wfh, url_prefix="/wfh")
api.register_blueprint(attendance, url_prefix="attendance")