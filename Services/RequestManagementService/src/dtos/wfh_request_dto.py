from src.models import ma

class WfhRequestDto(ma.Schema):
    class Meta:
        fields = ("EmployeeId", "Date", "WfhType", "Note")