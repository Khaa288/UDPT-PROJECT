from enum import Enum

class EmployeeStatus(str, Enum):
    ACTIVATED = 1
    DEACTIVATED = 2

class EmployeeGender(str, Enum):
    MALE = 1
    FEMALE = 2
    OTHER = 3