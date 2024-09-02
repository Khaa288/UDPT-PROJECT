from src.models import ma

class CheckInRequestDto(ma.Schema):
    class Meta:
        fields = ("Employee", "CheckInNote")

class CheckOutRequestDto(ma.Schema):
    class Meta:
        fields = ("Employee", "CheckOutNote")