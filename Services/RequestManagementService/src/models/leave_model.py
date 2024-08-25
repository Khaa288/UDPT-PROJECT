from dataclasses import dataclass
from flask import jsonify
from src.models import db_leave
from datetime import datetime
import uuid

@dataclass
class Leave():
    LeaveId: uuid
    RequestId: uuid
    EmployeeId: int
    FromDate: str
    ToDate: str
    Duration: int
    Note: str
    
    def __init__(self, requestId, employeeId, fromDate, toDate, note = None):
        self.RequestId = requestId
        self.LeaveId = uuid.uuid4()
        self.EmployeeId = employeeId
        self.FromDate = fromDate
        self.ToDate = toDate
        self.Duration = datetime.strptime(toDate, '%d-%m-%Y').date().day - datetime.strptime(fromDate, '%d-%m-%Y').date().day
        self.Note = note

    def create(leave):
        new_leave = Leave(
            leave["RequestId"],
            leave["EmployeeId"], 
            leave["FromDate"], 
            leave["ToDate"], 
            leave["Note"]
        )
        
        created_leave = db_leave.insert_one(jsonify(new_leave).json)
        return True

    def get_pages(page_size = 5):
        if db_leave.count_documents({}) <= page_size:
            return 1

        return round(db_leave.count_documents({}) / page_size)

    def get_all(params):
        page = int(params['page'])
        pageSize = int(params['pageSize'])

        leave = db_leave.find().limit(pageSize)
        leave = leave.skip(pageSize*(page - 1))

        return leave
    
    def get_by_id(leave_id):
        return db_leave.find_one({'LeaveId': leave_id})