from dataclasses import dataclass
from json import dumps
import math
from flask import jsonify
from src.models import db_timesheet_update_request
from src.models.employee_model import Employee
from src.utils import RequestStatus
from datetime import datetime
import uuid

@dataclass
class TimesheetUpdateRequest():
    RequestId: uuid
    Employee: Employee   # type: ignore
    Date: str
    NewWorkHour: int
    Note: int
    Status: RequestStatus
    CreatedDate: datetime
    
    def __init__(self, employee, date, newWorkHour, note = None):
        self.RequestId = uuid.uuid4()
        self.Employee = employee
        self.Date = date
        self.NewWorkHour = newWorkHour
        self.Note = note
        self.Status = RequestStatus.PENDING
        self.CreatedDate = datetime.now()

    def get_pages(page_size = 5):
        document_nums = db_timesheet_update_request.count_documents({ 'Status': RequestStatus.PENDING.value })

        if  document_nums <= page_size:
            return 1

        return math.ceil(document_nums / page_size)

    def get_all(params):
        page = int(params['page'])
        pageSize = int(params['pageSize'])

        timesheets = db_timesheet_update_request.find({'Status': RequestStatus.PENDING}).limit(pageSize)
        timesheets = timesheets.skip(pageSize*(page - 1))

    def get_by_id(request_id):
        return db_timesheet_update_request.find_one({'RequestId': request_id})

    def create(update_request):
        request = TimesheetUpdateRequest(
            employee=update_request["Employee"],
            date=update_request["Date"],
            newWorkHour=update_request["NewWorkHour"],
            note=update_request["Note"]
        )

        db_timesheet_update_request.insert_one(jsonify(request).json)

        return True
    
    def update_status(request_id, status):
        updated_request = db_timesheet_update_request.update_one(
            {'RequestId': request_id},
            {'$set': { 'Status': status }}
        )

        return True
