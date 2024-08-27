from dataclasses import dataclass
from json import dumps
import math
from flask import jsonify
from src.models import db_timesheet
from src.models.employee_model import Employee
from datetime import datetime
import uuid

@dataclass
class Timesheet():
    TimesheetId: uuid
    Employee: Employee   # type: ignore
    WorkDates: [] # type: ignore
    Month: int
    Year: int
    
    def __init__(self, employee, month, year):
        self.TimesheetId = uuid.uuid4()
        self.Employee = employee
        self.WorkDates = []
        self.Month = month
        self.Year = year

    def get_pages(page_size = 5):
        if db_timesheet.count_documents({}) <= page_size:
            return 1

        return  math.ceil(db_timesheet.count_documents({}) / page_size)

    def get_all(params):
        page = int(params['page'])
        pageSize = int(params['pageSize'])

        timesheets = db_timesheet.find().limit(pageSize)
        timesheets = timesheets.skip(pageSize*(page - 1))

        return timesheets
    
    def get_by_id(timesheet_id):
        return db_timesheet.find_one({'TimesheetId': timesheet_id})

    def upsert_workhour(timesheet_id, update_info):
        date = update_info["Date"]
        new_work_hour = update_info["NewWorkHour"]

        timesheet_date = db_timesheet.find_one({ 
            'TimesheetId': timesheet_id,
            'WorkDates.Date': date
        })

        if timesheet_date: # check if dates exists ?
            db_timesheet.update_one(
                { 'TimesheetId': timesheet_id, 'WorkDates.Date': date },
                { '$set':  {'WorkDates.$.WorkHour': new_work_hour}},
            )
        else: # if date doesnt exists -> append new
            db_timesheet.update_one(
                { 'TimesheetId': timesheet_id },
                { '$push': { 'WorkDates': { 'Date': date, 'WorkHour': new_work_hour }} }
            )

        return True


    def upsert(employee, date, new_work_hour):
        updated_month = datetime.now().strptime(date, '%d-%m-%Y').date().month
        updated_year = datetime.now().strptime(date, '%d-%m-%Y').date().year

        timesheet = db_timesheet.find_one({
            'Employee': jsonify(employee).json, 
            'Month': updated_month, 
            'Year': updated_year
        })

        if timesheet: # update only
            timesheet_date = db_timesheet.find_one({ 
                'TimesheetId': timesheet["TimesheetId"],
                'WorkDates.Date': date
            })

            if timesheet_date: # check if dates exists ?
                db_timesheet.update_one(
                    { 'TimesheetId': timesheet["TimesheetId"], 'WorkDates.Date': date },
                    { '$set':  {'WorkDates.$.WorkHour': new_work_hour}},
                )
            else: # if date doesnt exists -> append new
                db_timesheet.update_one(
                    { 'TimesheetId': timesheet["TimesheetId"] },
                    { '$push': { 'WorkDates': { 'Date': date, 'WorkHour': new_work_hour }} }
                )
        
        else: # insert new timesheet
            new_timesheet = Timesheet(
                employee=employee,
                month=updated_month,
                year=updated_year
            )

            new_timesheet.WorkDates.append({ 'Date': date, 'WorkHour': new_work_hour })

            db_timesheet.insert_one(jsonify(new_timesheet).json)
        
        return True
