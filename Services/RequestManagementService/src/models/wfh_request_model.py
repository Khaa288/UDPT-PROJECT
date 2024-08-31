from dataclasses import dataclass
import math
from src.models import db_wfh_request
from src.models.employee_model import Employee
from src.utils import RequestStatus, WfhTypeEnum
from datetime import datetime
from flask import jsonify
import uuid

@dataclass
class WfhRequest():
    RequestId: uuid
    Employee: Employee # type: ignore
    Date: str
    WfhType: WfhTypeEnum
    Note: str
    Status: RequestStatus
    CreatedDate: datetime
    
    def __init__(self, employee, date, wfhType, note = None):
        self.RequestId = uuid.uuid4()
        self.Employee = employee
        self.Date = date
        self.WfhType = wfhType
        self.Note = note
        self.Status = RequestStatus.PENDING
        self.CreatedDate = datetime.now()

    def get_pages(page_size = 5):
        document_nums = db_wfh_request.count_documents({ 'Status': RequestStatus.PENDING.value })

        if  document_nums <= page_size:
            return 1

        return math.ceil(document_nums / page_size)

    def get_all(params):
        page = int(params['page'])
        pageSize = int(params['pageSize'])

        wfh_filter = {'Status': RequestStatus.PENDING}

        if params['employeeId'] is not None and params['employeeId'] != 'None':
            wfh_filter['Employee.EmployeeId'] = int(params['employeeId'])

        leave_requests = db_wfh_request.find(wfh_filter).limit(pageSize)
        leave_requests = leave_requests.skip(pageSize*(page - 1))

        return leave_requests

    def get_by_id(request_id):
        return db_wfh_request.find_one({'RequestId': request_id})

    def create(wfh):
        request = WfhRequest(
            employee = wfh["Employee"], 
            date = wfh["Date"], 
            wfhType = wfh["WfhType"], 
            note = wfh["Note"]
        )
        
        created_request = db_wfh_request.insert_one(jsonify(request).json)
        return True
    
    def update_status(request_id, status):
        updated_request = db_wfh_request.update_one(
            {'RequestId': request_id},
            {'$set': { 'Status': status }}
        )

        return 1
