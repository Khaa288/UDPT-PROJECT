from src.models import ma

class EmployeeUpdateRequestDto(ma.Schema):
    class Meta:
        fields = ("employeeId", "firstName", "middleName","lastName")