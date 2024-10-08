from dataclasses import dataclass
import math
from src.models.employee_model import Employee
from flask import jsonify
from src.models import db_wfh
import uuid

@dataclass
class WFH():
    WfhId: uuid
    RequestId: uuid
    Employee: Employee # type: ignore
    Date: str
    WfhType: int
    Note: str
    
    def __init__(self, requestId, employee, date, WfhType, note = None):
        self.RequestId = requestId
        self.WfhId = uuid.uuid4()
        self.Employee = employee
        self.Date = date
        self.WfhType = WfhType
        self.Note = note

    def create(wfh):
        new_wfh = WFH(
            requestId = wfh["RequestId"],
            employee = wfh["Employee"], 
            date = wfh["Date"], 
            WfhType = wfh["WfhType"], 
            note = wfh["Note"]
        )
        
        created_wfh = db_wfh.insert_one(jsonify(new_wfh).json)
        return True

    def get_pages(page_size = 5):
        if db_wfh.count_documents({}) <= page_size:
            return 1

        return  math.ceil(db_wfh.count_documents({}) / page_size)

    def get_all(params):
        page = int(params['page'])
        pageSize = int(params['pageSize'])

        wfh_requests = db_wfh.find().limit(pageSize)
        wfh_requests = wfh_requests.skip(pageSize*(page - 1))

        return wfh_requests
    
    def get_by_id(wfh_id):
        return db_wfh.find_one({'WfhId': wfh_id})