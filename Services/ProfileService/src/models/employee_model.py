from dataclasses import dataclass
from sqlalchemy import ForeignKey, String, Enum, or_
from src.models import db
from sqlalchemy.orm import Mapped, mapped_column
from src.models.user_model import User
from src.utils import EmployeeStatus

@dataclass
class Employee(db.Model):
    __tablename__ = "Employee"

    EmployeeId: Mapped[int] = mapped_column(primary_key=True)
    UserId: Mapped[int] = mapped_column(ForeignKey(User.UserId))
    FirstName: Mapped[str] = mapped_column(String(128))
    MiddleName: Mapped[str] = mapped_column(String(128))
    LastName: Mapped[str] = mapped_column(String(128))
    IdCardNum: Mapped[str] = mapped_column(String(128))
    TaxNum: Mapped[str] = mapped_column(String(128))
    Address: Mapped[str] = mapped_column(String(128))
    PhoneNum: Mapped[str] = mapped_column(String(128))
    BankAccountNum: Mapped[str] = mapped_column(String(128))
    Gender: Mapped[str] = mapped_column(String(128))
    Role: Mapped[str] = mapped_column(String(128))
    JobTitle: Mapped[str] = mapped_column(String(128))
    Status: Mapped[EmployeeStatus] = mapped_column(Enum(EmployeeStatus))

    def get_pages(page_size = 5):
        if Employee.query.count() <= page_size:
            return 1

        return round(Employee.query.count() / page_size)

    def get_all(params):
        # All filter are null -> return all records
        if params['firstName'] is None and params['firstName'] is None and params['firstName'] is None:
            employees = db.session.query(Employee)

        else:
            employees = db.session.query(Employee).filter(
                or_(
                    Employee.FirstName == params['firstName'], 
                    Employee.IdCardNum == params['idCardNum'], 
                    Employee.JobTitle == params['jobTitle']
                )
            )
        
        employees = employees.order_by(Employee.EmployeeId)

        page = int(params['page'])
        pageSize = int(params['pageSize'])
        employees = employees.offset(pageSize*(page - 1))
        employees = employees.limit(pageSize)

        return employees.all()
    
    def get_by_id(employeeId):
        return db.get_or_404(Employee, employeeId)
    
    def get_by_user_id(userId):
        return Employee.query.filter_by(UserId = userId).first_or_404()
    
    def update(employeeId, updated_employee):
        employee = db.get_or_404(Employee, employeeId)

        employee.FirstName = updated_employee["FirstName"]
        employee.MiddleName = updated_employee["MiddleName"]
        employee.LastName = updated_employee["LastName"]
        employee.IdCardNum = updated_employee["IdCardNum"]
        employee.TaxNum = updated_employee["TaxNum"]
        employee.Address = updated_employee["Address"]
        employee.PhoneNum = updated_employee["PhoneNum"]
        employee.BankAccountNum = updated_employee["BankAccountNum"]
        employee.Gender = updated_employee["Gender"]
        employee.JobTitle = updated_employee["JobTitle"]

        db.session.commit()
        return 1

    def deactivate(employeeId):
        employee = db.get_or_404(Employee, employeeId)

        employee.Status = EmployeeStatus.DEACTIVATED

        db.session.commit()
        return 1