from dataclasses import dataclass

@dataclass
class Employee():
    EmployeeId: int
    EmployeeName: str
    EmployeeJobTitle: str
    EmployeeIdCardNum: str
    
    def __init__(self, employeeId, employeeName, employeeJobTitle, employeeIdCardNum):
        self.EmployeeId = employeeId
        self.EmployeeName = employeeName
        self.EmployeeJobTitle = employeeJobTitle
        self.EmployeeIdCardNum = employeeIdCardNum
        