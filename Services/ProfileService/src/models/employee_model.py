from dataclasses import dataclass
from sqlalchemy import ForeignKey, String, select
from src.models import db
from sqlalchemy.orm import Mapped, mapped_column
from src.models.user_model import User

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

    def get_all():
        return Employee.query.all()
    
    def get_by_id(employeeId):
        return db.get_or_404(Employee, employeeId)
    
    def update(employeeId):
        employee = db.get_or_404(Employee, employeeId)

        employee.FirstName = 'ye'
        employee.MiddleName = 'ye'
        employee.LastName = 'ye'

        print('ye')
        return 1

