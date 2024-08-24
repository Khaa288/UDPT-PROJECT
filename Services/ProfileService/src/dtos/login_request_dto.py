from src.models import ma

class LoginRequestDto(ma.Schema):
    class Meta:
        fields = ("Username", "Password")