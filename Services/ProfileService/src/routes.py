from flask import Blueprint
from src.controllers.auth_controller import auth
from src.controllers.employee_controller import employee

# main blueprint to be registered with application
api = Blueprint('api', __name__)

# register user with api blueprint
api.register_blueprint(auth, url_prefix="/auth")
api.register_blueprint(employee, url_prefix="/employee")