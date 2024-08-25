from src.models import ma

class CheckInRequestDto(ma.Schema):
    class Meta:
        fields = ("EmployeeId", "CheckInNote")

class CheckOutRequestDto(ma.Schema):
    class Meta:
        fields = ("EmployeeId", "CheckOutNote")