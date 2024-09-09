from flask import Blueprint, jsonify, request
import py_eureka_client.eureka_client as eureka_client
import urllib.parse

reward = Blueprint("reward", __name__)

@reward.route('/gift', methods = ["GET"])
def get_gift_list():
    res = eureka_client.do_service(
        app_name = "reward_service", 
        service = f"/api/reward/gift"
    )
    
    return res

@reward.route('/send-point', methods = ["POST"])
def send_point():
    request_body = request.get_json()

    res = eureka_client.do_service(
        app_name = "reward_service", 
        service = f"/api/reward/send-point", 
        method="POST", 
        headers=({"Content-Type": "application/json"}),
        data=request_body
    )

    return res

@reward.route('exchange', methods=["POST"])
def exchange_gift():
    request_body = request.get_json()

    res = eureka_client.do_service(
        app_name = "reward_service", 
        service = f"/api/reward/exchange", 
        method="POST", 
        headers=({"Content-Type": "application/json"}),
        data=request_body
    )

    return res
    
@reward.route('/employee/<employee_id>/gift', methods=["GET"])
def list_employee_gifts(employee_id):
    res = eureka_client.do_service(
        app_name = "reward_service", 
        service = f"/api/reward/employee/{employee_id}/gift"
    )
    
    return res

@reward.route('/employee')
def get_all_reward_employee():
    res = eureka_client.do_service(
        app_name = "reward_service", 
        service = f"/api/reward/employee"
    )
    
    return res