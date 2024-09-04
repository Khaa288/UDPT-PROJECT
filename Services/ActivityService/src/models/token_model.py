from src.models.activity_model import Activity
from src.models import db
from dataclasses import dataclass
from sqlalchemy import String,DateTime,ForeignKey
from src.models import db
from sqlalchemy.orm import Mapped, mapped_column
import datetime

@dataclass
class Token (db.Model):
    __tablename__ = "Token"
    EmployeeId: Mapped[int] = mapped_column()
    AccessToken: Mapped[str] = mapped_column(String(128))
    Refreshtoken: Mapped[str] = mapped_column(String(128))
    Token_id : Mapped[int] = mapped_column(primary_key=True) ##Dummy
    def get_token_by_EmployeeId(employee_id):
       token = db.session.query(Token).filter(Token.EmployeeId == employee_id)
       return token.all()
    def create_token(employee_id: int, access_token : str, refresh_token : str ):
        newToken = Token(
            EmployeeId=employee_id,
            AccessToken= access_token,
            Refreshtoken= refresh_token

            

        )
        db.session.add(newToken)
        db.session.commit()
        return newToken
