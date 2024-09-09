from flask import jsonify, request, json, Blueprint
from marshmallow import ValidationError
from src.services.urbox_service import UrboxService
from src.dtos.reward_request_dto import SendPointRequestDto, ExchangeGiftRequestDto
from src.models.reward_model import Reward
from bson import json_util

# user controller blueprint to be registered with api blueprint
reward = Blueprint("reward", __name__)

@reward.route('/gift', methods = ["GET"])
def get_gift_list():
    return UrboxService.list_gifts()

@reward.route('/send-point', methods = ["POST"])
def send_point():
    dto = SendPointRequestDto()
    request_body = request.get_json()

    try:
        validated_body = dto.load(request_body)
        send_point_request = Reward.send_point(validated_body)
        return jsonify(send_point_request)
       
    except ValidationError as err:
        return 'Invalid input!'

@reward.route('exchange', methods=["POST"])
def exchange_gift():
    dto = ExchangeGiftRequestDto()
    request_body = request.get_json()

    try:
        validated_body = dto.load(request_body)
        send_point_request = Reward.exchange_gift(validated_body)
        return jsonify(send_point_request)
       
    except ValidationError as err:
        return 'Invalid input!'
    
@reward.route('/employee/<employee_id>/gift', methods=["GET"])
def list_employee_gifts(employee_id):
    return jsonify(Reward.list_employee_gifts(employee_id))

@reward.route('/employee')
def get_all_reward_employee():
    return json.loads(json_util.dumps(Reward.list_employees()))

@reward.route('/employee/<employee_id>')
def get_reward_employee(employee_id):
    return json.loads(json_util.dumps(Reward.get_reward_employee(employee_id)))