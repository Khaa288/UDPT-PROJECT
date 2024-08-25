from enum import Enum

class RequestStatus(str, Enum):
    PENDING = 1
    ACCEPTED = 2
    DENIED = 3
    
class WfhTypeEnum(str, Enum):
    FULLDAY = 1
    HALFDAY = 2