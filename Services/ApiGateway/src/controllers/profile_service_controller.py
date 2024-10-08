from flask import Blueprint, jsonify, request
import py_eureka_client.eureka_client as eureka_client
import urllib.parse

auth = Blueprint("auth", __name__)
employee = Blueprint("employee", __name__)

@auth.route('/login', methods = ["POST"])
def handle_login():
    request_body = request.get_json()

    res = eureka_client.do_service(
        app_name = "profile_service", 
        service = f"/api/auth/login", 
        method="POST", 
        headers=({"Content-Type": "application/json"}),
        data=request_body
    )

    return res

@employee.route('/page', methods=["GET"])
def get_employee_pages():
    res = eureka_client.do_service(
        app_name = "profile_service", 
        service = f"/api/employee/page"
    )
    
    return res

@employee.route('', methods = ["GET"])
def list():
    params = {
        "firstName": request.args.get('firstName'),
        "idCardNum": request.args.get('idCardNum'),
        "jobTitle": request.args.get('jobTitle'),
        "page": request.args.get('page'),
        "pageSize": request.args.get('pageSize')
    }

    # delete null params
    keys_to_remove = [key for key, value in params.items() if value is None]
    for key in keys_to_remove:
        del params[key]
    
    query_string = urllib.parse.urlencode(params)

    res = eureka_client.do_service(
        app_name = "profile_service", 
        service = f"/api/employee?{query_string}"
    )
    
    return res

@employee.route('/<employee_id>', methods = ["GET"])
def get(employee_id):
    res = eureka_client.do_service("profile_service", f"/api/employee/{employee_id}")
    return res

@employee.route('/<employee_id>', methods = ["PUT"])
def update(employee_id):
    request_body = request.get_json()

    res = eureka_client.do_service(
        app_name = "profile_service", 
        service = f"/api/employee/{employee_id}", 
        method="PUT", 
        headers=({"Content-Type": "application/json"}),
        data=request_body
    )  
    return res
    
@employee.route('/<employee_id>/deactivate', methods = ["POST"])
def deactivate(employee_id):
    res = eureka_client.do_service("profile_service", f"/api/employee/{employee_id}/deactivate", method="POST")
    return res