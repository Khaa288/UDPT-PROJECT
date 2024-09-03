from flask import Blueprint
from src.controllers.reward_controller import reward

# main blueprint to be registered with application
api = Blueprint('api', __name__)

# register user with api blueprint
api.register_blueprint(reward, url_prefix="/reward")