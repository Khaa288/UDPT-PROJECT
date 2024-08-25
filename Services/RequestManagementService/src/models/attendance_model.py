from dataclasses import dataclass
from json import dumps
from flask import jsonify
from src.models import db_attendance
from datetime import datetime
import uuid

@dataclass
class Attendance():
    EmployeeId: int
    CheckInTime: str
    CheckInNote: str
    CheckOutTime: str
    CheckOutNote: str
    AttendanceDate: datetime
    Duration: float
    
    def __init__(self, employeeId, checkInNote):
        self.EmployeeId = employeeId
        self.CheckInTime = str(datetime.now().time())
        self.CheckInNote = checkInNote
        self.CheckOutTime = None
        self.CheckOutNote = None
        self.AttendanceDate = str(datetime.now().date())
        self.Duration = None

    def get_current_attendance(employeeId):
        # Check if attendance exists
        isExist = db_attendance.find_one({ 
            "EmployeeId": int(employeeId), 
            "AttendanceDate": str(datetime.now().date()) 
        })
    
        if isExist :
            print(isExist)
            return isExist
        
        else:
            return 'No attendance yet!'
        

    def check_in(check_in):
        attendance = Attendance(
            check_in["EmployeeId"],
            check_in["CheckInNote"]
        )

        db_attendance.insert_one(jsonify(attendance).json)

        return attendance
    
    def check_out(check_out):
        check_in_time = db_attendance.find_one({
            'EmployeeId': int(check_out["EmployeeId"]),
            'AttendanceDate': str(datetime.now().date()) 
        })['CheckInTime']

        attedance = db_attendance.update_one(
            {
                'EmployeeId': int(check_out["EmployeeId"]), 
                'AttendanceDate': str(datetime.now().date()) 
            },
            {
                '$set': 
                { 
                    'CheckOutTime': str(datetime.now().time()),
                    'CheckOutNote': check_out["CheckOutNote"],
                    'Duration':  datetime.now().time().hour - datetime.strptime(check_in_time, "%H:%M:%S.%f").time().hour
                }
            }
        )

        return True
    