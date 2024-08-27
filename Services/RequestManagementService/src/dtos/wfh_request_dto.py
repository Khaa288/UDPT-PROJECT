from src.models import ma

class WfhRequestDto(ma.Schema):
    class Meta:
        fields = ("Employee", "Date", "WfhType", "Note")