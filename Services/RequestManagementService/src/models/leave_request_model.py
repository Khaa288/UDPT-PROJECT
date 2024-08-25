from dataclasses import dataclass
from src.models import db_leave_request
from src.utils import RequestStatus
from datetime import datetime
from flask import jsonify
import uuid

@dataclass
class LeaveRequest():
    RequestId: uuid
    EmployeeId: int
    FromDate: str
    ToDate: str
    Duration: int
    Note: str
    Status: RequestStatus
    CreatedDate: datetime
    
    def __init__(self, employeeId, fromDate, toDate, note = None):
        self.RequestId = uuid.uuid4()
        self.EmployeeId = employeeId
        self.FromDate = fromDate
        self.ToDate = toDate
        self.Duration = datetime.strptime(toDate, '%d-%m-%Y').date().day - datetime.strptime(fromDate, '%d-%m-%Y').date().day
        self.Note = note
        self.Status = RequestStatus.PENDING
        self.CreatedDate = datetime.now()

    def get_pages(page_size = 5):
        if db_leave_request.count_documents({}) <= page_size:
            return 1

        return round(db_leave_request.count_documents({}) / page_size)

    def get_all(params):
        page = int(params['page'])
        pageSize = int(params['pageSize'])

        leave_requests = db_leave_request.find().limit(pageSize)
        leave_requests = leave_requests.skip(pageSize*(page - 1))

        return leave_requests
    
    def get_by_id(request_id):
        return db_leave_request.find_one({'RequestId': request_id})


    def create(leave):
        request = LeaveRequest(
            leave["EmployeeId"], 
            leave["FromDate"], 
            leave["ToDate"], 
            leave["Note"]
        )
        
        created_request = db_leave_request.insert_one(jsonify(request).json)
        return True
    
    def update_status(request_id, status):
        updated_request = db_leave_request.update_one(
            {'RequestId': request_id},
            {'$set': { 'Status': status }}
        )

        return True
