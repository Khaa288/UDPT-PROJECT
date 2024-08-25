from dataclasses import dataclass
from src.models import db_wfh_request
from src.utils import RequestStatus, WfhTypeEnum
from datetime import datetime
from flask import jsonify
import uuid

@dataclass
class WfhRequest():
    RequestId: uuid
    EmployeeId: int
    Date: str
    WfhType: WfhTypeEnum
    Note: str
    Status: RequestStatus
    CreatedDate: str
    
    def __init__(self, employeeId, date, wfhType, note = None):
        self.RequestId = uuid.uuid4()
        self.EmployeeId = employeeId
        self.Date = date
        self.WfhType = wfhType
        self.Note = note
        self.Status = RequestStatus.PENDING
        self.CreatedDate = datetime.now()

    def get_pages(page_size = 5):
        if db_wfh_request.count_documents({}) <= page_size:
            return 1

        return round(db_wfh_request.count_documents({}) / page_size)

    def get_all(params):
        page = int(params['page'])
        pageSize = int(params['pageSize'])

        leave_requests = db_wfh_request.find().limit(pageSize)
        leave_requests = leave_requests.skip(pageSize*(page - 1))

        return leave_requests

    def get_by_id(request_id):
        return db_wfh_request.find_one({'RequestId': request_id})

    def create(wfh):
        request = WfhRequest(
            employeeId = wfh["EmployeeId"], 
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
