from dataclasses import dataclass
import math
from flask import jsonify
from src.models import db_leave
from src.models.employee_model import Employee 
from src.utils import RequestStatus
from datetime import datetime
import uuid

@dataclass
class Leave():
    LeaveId: uuid
    RequestId: uuid
    Employee: Employee # type: ignore
    FromDate: str
    ToDate: str
    Duration: int
    Note: str
    
    def __init__(self, requestId, employee, fromDate, toDate, note = None):
        self.RequestId = requestId
        self.LeaveId = uuid.uuid4()
        self.Employee = employee
        self.FromDate = fromDate
        self.ToDate = toDate
        self.Duration = (datetime.strptime(toDate, '%d-%m-%Y') - datetime.strptime(fromDate, '%d-%m-%Y')).days
        self.Note = note

    def create(leave):
        new_leave = Leave(
            leave["RequestId"],
            leave["Employee"], 
            leave["FromDate"], 
            leave["ToDate"], 
            leave["Note"]
        )
        
        created_leave = db_leave.insert_one(jsonify(new_leave).json)
        return True

    def get_pages(page_size = 5):
        if db_leave.count_documents({}) <= page_size:
            return 1

        return  math.ceil(db_leave.count_documents({}) / page_size)

    def get_all(params):
        page = int(params['page'])
        pageSize = int(params['pageSize'])

        leave = db_leave.find().limit(pageSize)
        leave = leave.skip(pageSize*(page - 1))

        return leave
    
    def get_by_id(leave_id):
        return db_leave.find_one({'LeaveId': leave_id})