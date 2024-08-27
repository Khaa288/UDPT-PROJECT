from src.models import ma

class UpdateTimesheetWorkHourtDto(ma.Schema):
    class Meta:
        fields = ("Date", "NewWorkHour")