from dataclasses import dataclass
import math
from src.models.employee_model import Employee
from src.models import db_leave_request
from src.utils import RequestStatus
from datetime import datetime
from flask import jsonify
import uuid

@dataclass
class LeaveRequest():
    RequestId: uuid
    Employee: Employee # type: ignore
    FromDate: str
    ToDate: str
    Duration: int
    Note: str
    Status: RequestStatus
    CreatedDate: datetime
    
    def __init__(self, employee, fromDate, toDate, note = None):
        self.RequestId = uuid.uuid4()
        self.Employee = employee
        self.FromDate = fromDate
        self.ToDate = toDate
        self.Duration = (datetime.strptime(toDate, '%d-%m-%Y') - datetime.strptime(fromDate, '%d-%m-%Y')).days
        self.Note = note
        self.Status = RequestStatus.PENDING
        self.CreatedDate = datetime.now()

    def get_pages(page_size = 5):
        document_nums = db_leave_request.count_documents({ 'Status': RequestStatus.PENDING.value })

        if  document_nums <= page_size:
            return 1

        return math.ceil(document_nums / page_size)

    def get_all(params):
        page = int(params['page'])
        pageSize = int(params['pageSize'])

        leave_requests = db_leave_request.find({'Status': RequestStatus.PENDING}).limit(pageSize)
        leave_requests = leave_requests.skip(pageSize*(page - 1))

        return leave_requests
    
    def get_by_id(request_id):
        return db_leave_request.find_one({'RequestId': request_id})

    def create(leave):
        request = LeaveRequest(
            leave["Employee"], 
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
