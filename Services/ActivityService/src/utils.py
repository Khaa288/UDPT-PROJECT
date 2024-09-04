from enum import Enum

class EmployeeStatus(str, Enum):
    ACTIVATED = 1
    DEACTIVATED = 2