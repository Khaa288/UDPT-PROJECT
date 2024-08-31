from flask import Blueprint, jsonify, request
import py_eureka_client.eureka_client as eureka_client
import urllib.parse

leave = Blueprint("leave", __name__)
wfh = Blueprint("wfh", __name__)
timesheet = Blueprint("timesheet", __name__)
attendance = Blueprint("attendance", __name__)

# LEAVE ROUTE
@leave.route('/page', methods = ["GET"])
def get_leave_pages():
    res = eureka_client.do_service(
        app_name = "request_management_service", 
        service = f"/api/leave/page", 
        method="GET",
        headers=({"Content-Type": "application/json"})
    )
    
    return res

@leave.route('', methods = ["GET"])
def list_leaves():
    params = {
        "page": request.args.get('page'),
        "pageSize": request.args.get('pageSize')
    }

    params = urllib.parse.urlencode(params)

    res = eureka_client.do_service(
        app_name = "request_management_service", 
        service = f"/api/leave?{params}", 
        method="GET",
        headers=({"Content-Type": "application/json"})
    )
    
    return res

@leave.route('/request/page', methods = ["GET"])
def get_leave_request_pages():
    params = {
        "employeeId": request.args.get('employeeId')
    }

    params = urllib.parse.urlencode(params)

    res = eureka_client.do_service(
        app_name = "request_management_service", 
        service = f"/api/leave/request/page?{params}", 
        method="GET",
        headers=({"Content-Type": "application/json"})
    )
    
    return res

@leave.route('/request', methods = ["GET"])
def list_leave_requests():
    params = {
        "page": request.args.get('page'),
        "pageSize": request.args.get('pageSize'),
        "employeeId": request.args.get('employeeId')
    }

    params = urllib.parse.urlencode(params)

    res = eureka_client.do_service(
        app_name = "request_management_service", 
        service = f"/api/leave/request?{params}", 
        method="GET",
        headers=({"Content-Type": "application/json"})
    )
    
    return res

@leave.route('/request', methods = ["POST"])
def request_leave():
    request_body = request.get_json()

    res = eureka_client.do_service(
        app_name = "request_management_service", 
        service = f"/api/leave/request", 
        method="POST",
        headers=({"Content-Type": "application/json"}),
        data=request_body
    )

    return res
    
@leave.route('/request/<request_id>/accept', methods = ["POST"])
def accept_leave(request_id):
    res = eureka_client.do_service(
        app_name = "request_management_service", 
        service = f"/api/leave/request/{request_id}/accept", 
        method="POST",
        headers=({"Content-Type": "application/json"})
    )

    return res

@leave.route('/request/<request_id>/deny', methods = ["POST"])
def deny_leave(request_id):
    res = eureka_client.do_service(
        app_name = "request_management_service", 
        service = f"/api/leave/request/{request_id}/deny", 
        method="POST",
        headers=({"Content-Type": "application/json"})
    )

    return res

# WFH ROUTE
@wfh.route('/page', methods = ["GET"])
def get_wfh_pages():
    res = eureka_client.do_service(
        app_name = "request_management_service", 
        service = f"/api/wfh/page", 
        method="GET",
        headers=({"Content-Type": "application/json"})
    )
    
    return res

@wfh.route('', methods = ["GET"])
def list_wfhs():
    params = {
        "page": request.args.get('page'),
        "pageSize": request.args.get('pageSize')
    }

    params = urllib.parse.urlencode(params)

    res = eureka_client.do_service(
        app_name = "request_management_service", 
        service = f"/api/wfh?{params}", 
        method="GET",
        headers=({"Content-Type": "application/json"})
    )
    
    return res

@wfh.route('/request/page', methods = ["GET"])
def get_wfh_request_pages():
    params = {
        "employeeId": request.args.get('employeeId')
    }

    params = urllib.parse.urlencode(params)

    res = eureka_client.do_service(
        app_name = "request_management_service", 
        service = f"/api/wfh/request/page?{params}", 
        method="GET",
        headers=({"Content-Type": "application/json"})
    )
    
    return res

@wfh.route('/request', methods = ["GET"])
def list_wfh_requests():
    params = {
        "page": request.args.get('page'),
        "pageSize": request.args.get('pageSize'),
        "employeeId": request.args.get('employeeId')
    }

    params = urllib.parse.urlencode(params)

    res = eureka_client.do_service(
        app_name = "request_management_service", 
        service = f"/api/wfh/request?{params}", 
        method="GET",
        headers=({"Content-Type": "application/json"})
    )
    
    return res

@wfh.route('/request', methods = ["POST"])
def request_wfh():
    request_body = request.get_json()

    res = eureka_client.do_service(
        app_name = "request_management_service", 
        service = f"/api/wfh/request", 
        method="POST",
        headers=({"Content-Type": "application/json"}),
        data=request_body
    )

    return res
    
@wfh.route('/request/<request_id>/accept', methods = ["POST"])
def accept_wfh(request_id):
    res = eureka_client.do_service(
        app_name = "request_management_service", 
        service = f"/api/wfh/request/{request_id}/accept", 
        method="POST",
        headers=({"Content-Type": "application/json"})
    )

    return res

@wfh.route('/request/<request_id>/deny', methods = ["POST"])
def deny_wfh(request_id):
    res = eureka_client.do_service(
        app_name = "request_management_service", 
        service = f"/api/wfh/request/{request_id}/deny", 
        method="POST",
        headers=({"Content-Type": "application/json"})
    )

    return res

# TIMESHEET ROUTE
@timesheet.route('/page', methods = ["GET"])
def get_timesheet_pages():
    res = eureka_client.do_service(
        app_name = "request_management_service", 
        service = f"/api/timesheet/page", 
        method="GET",
        headers=({"Content-Type": "application/json"})
    )
    
    return res

@timesheet.route('', methods = ["GET"])
def list_timesheets():
    params = {
        "page": request.args.get('page'),
        "pageSize": request.args.get('pageSize')
    }

    params = urllib.parse.urlencode(params)

    res = eureka_client.do_service(
        app_name = "request_management_service", 
        service = f"/api/timesheet?{params}", 
        method="GET",
        headers=({"Content-Type": "application/json"})
    )
    
    return res

@timesheet.route('/request/page', methods = ["GET"])
def get_timehsheet_update_request_pages():
    res = eureka_client.do_service(
        app_name = "request_management_service", 
        service = f"/api/timesheet/request/page", 
        method="GET",
        headers=({"Content-Type": "application/json"})
    )
    
    return res

@timesheet.route('/request', methods = ["GET"])
def list_timesheet_update_request():
    params = {
        "page": request.args.get('page'),
        "pageSize": request.args.get('pageSize')
    }

    params = urllib.parse.urlencode(params)

    res = eureka_client.do_service(
        app_name = "request_management_service", 
        service = f"/api/timesheet/request?{params}", 
        method="GET",
        headers=({"Content-Type": "application/json"})
    )
    
    return res

@timesheet.route('/<timesheet_id>', methods = ["GET"])
def get_timesheet(timesheet_id):
    res = eureka_client.do_service(
        app_name = "request_management_service", 
        service = f"/api/timesheet/{timesheet_id}", 
        method="GET",
        headers=({"Content-Type": "application/json"})
    )
    
    return res

@timesheet.route('/request', methods=["POST"])
def request_update_timesheet():
    request_body = request.get_json()

    res = eureka_client.do_service(
        app_name = "request_management_service", 
        service = f"/api/timesheet/request", 
        method="POST",
        headers=({"Content-Type": "application/json"}),
        data=request_body
    )

    return res

@timesheet.route('/<timesheet_id>', methods = ["POST"])
def update_timesheet_workHour(timesheet_id):
    request_body = request.get_json()

    res = eureka_client.do_service(
        app_name = "request_management_service", 
        service = f"/api/timesheet/{timesheet_id}", 
        method="POST",
        headers=({"Content-Type": "application/json"}),
        data=request_body
    )

    return res
    
@timesheet.route('/request/<request_id>/accept', methods=["POST"])
def accept_update_timesheet_request(request_id):
    res = eureka_client.do_service(
        app_name = "request_management_service", 
        service = f"/api/timesheet/request/{request_id}/accept", 
        method="POST",
        headers=({"Content-Type": "application/json"})
    )

    return res

@timesheet.route('/request/<request_id>/deny', methods=["POST"])
def deny_update_timesheet_request(request_id):
    res = eureka_client.do_service(
        app_name = "request_management_service", 
        service = f"/api/timesheet/request/{request_id}/deny", 
        method="POST",
        headers=({"Content-Type": "application/json"})
    )

    return res

@attendance.route('/employee/<employee_id>/current', methods = ["GET"])
def getCurrentAttendance(employee_id):
    res = eureka_client.do_service(
        app_name = "request_management_service", 
        service = f"/api/attendance/employee/{employee_id}/current", 
        method="GET",
        headers=({"Content-Type": "application/json"})
    )
    
    return res

@attendance.route('/check-in', methods = ["POST"])
def checkIn():
    request_body = request.get_json()

    res = eureka_client.do_service(
        app_name = "request_management_service", 
        service = f"/api/attendance/check-in", 
        method="POST",
        headers=({"Content-Type": "application/json"}),
        data=request_body
    )

    return res
    
@attendance.route('/check-out', methods = ["POST"])
def checkOut():
    request_body = request.get_json()

    res = eureka_client.do_service(
        app_name = "request_management_service", 
        service = f"/api/attendance/check-out", 
        method="POST",
        headers=({"Content-Type": "application/json"}),
        data=request_body
    )

    return res