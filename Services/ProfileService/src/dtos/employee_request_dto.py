from src.models import ma

class EmployeeUpdateRequestDto(ma.Schema):
    class Meta:
        fields = ("FirstName", "MiddleName","LastName", "IdCardNum", "TaxNum", "Address", "PhoneNum", "Gender", "JobTitle", "BankAccountNum")