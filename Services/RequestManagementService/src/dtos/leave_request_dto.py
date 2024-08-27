from src.models import ma

class LeaveRequestDto(ma.Schema):
    class Meta:
        fields = ("Employee", "FromDate", "ToDate", "Note")