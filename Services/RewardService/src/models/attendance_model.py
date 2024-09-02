from dataclasses import dataclass
from json import dumps
from flask import jsonify
from src.models import db_attendance
from src.models.timesheet_model import Timesheet
from src.models.employee_model import Employee
from datetime import datetime
import uuid

@dataclass
class Attendance():
    Employee: Employee # type: ignore
    CheckInTime: str
    CheckInNote: str
    CheckOutTime: str
    CheckOutNote: str
    AttendanceDate: datetime
    Duration: float
    
    def __init__(self, employee, checkInNote):
        self.Employee = employee
        self.CheckInTime = str(datetime.now().time())
        self.CheckInNote = checkInNote
        self.CheckOutTime = None
        self.CheckOutNote = None
        self.AttendanceDate = str(datetime.now().date())
        self.Duration = None

    def get_current_attendance(employee_id):
        # Check if attendance exists
        isExist = db_attendance.find_one({ 
            "Employee.EmployeeId": int(employee_id), 
            "AttendanceDate": str(datetime.now().date()) 
        })
    
        if isExist :
            print(isExist)
            return isExist
        
        else:
            return 'No attendance yet!'

    def check_in(check_in):
        attendance = Attendance(
            check_in["Employee"],
            check_in["CheckInNote"]
        )

        db_attendance.insert_one(jsonify(attendance).json)

        return True
    
    def check_out(check_out):
        # Get check in time to process 'Duration'
        
        check_in_time = db_attendance.find_one({
            'Employee': jsonify(check_out["Employee"]).json,
            'AttendanceDate': str(datetime.now().date()) 
        })['CheckInTime']
        
        now = datetime.now()
        
        check_out_time = now.time()
        check_in_time = datetime.strptime(check_in_time, "%H:%M:%S.%f").time()

        duration = check_out_time.hour - check_in_time.hour

        # Update check out time
        attedance = db_attendance.update_one(
            {
                'Employee': jsonify(check_out["Employee"]).json,
                'AttendanceDate': str(now.date()) 
            },
            {
                '$set': 
                { 
                    'CheckOutTime': str(check_out_time),
                    'CheckOutNote': check_out["CheckOutNote"],
                    'Duration': duration
                }
            }
        )

        # Update timesheet
        timesheet = Timesheet.upsert(check_out["Employee"], str(now.date().strftime('%d-%m-%Y')), duration)

        return True
    