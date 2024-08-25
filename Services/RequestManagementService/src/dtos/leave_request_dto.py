from src.models import ma

class LeaveRequestDto(ma.Schema):
    class Meta:
        fields = ("EmployeeId", "FromDate", "ToDate", "Note")