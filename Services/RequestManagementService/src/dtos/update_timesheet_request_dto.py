from src.models import ma

class UpdateTimesheetRequestDto(ma.Schema):
    class Meta:
        fields = ("Employee", "Date", "NewWorkHour", "Note")