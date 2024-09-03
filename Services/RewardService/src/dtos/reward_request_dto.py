from src.models import ma

class SendPointRequestDto(ma.Schema):
    class Meta:
        fields = ("SenderId", "ReceiverId", "Point")

class ExchangeGiftRequestDto(ma.Schema):
    class Meta:
        fields = ("EmployeeId", "GiftId", "BrandId")