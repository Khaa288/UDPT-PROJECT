from flask import Blueprint
from src.controllers.profile_service_controller import auth, employee

# main blueprint to be registered with application
api = Blueprint('api', __name__)

# register user with api blueprint
api.register_blueprint(auth, url_prefix="/auth")
api.register_blueprint(employee, url_prefix="/employee")