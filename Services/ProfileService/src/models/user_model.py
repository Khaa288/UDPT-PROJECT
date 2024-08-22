from dataclasses import dataclass
from sqlalchemy import String
from src.models import db
from sqlalchemy.orm import Mapped, mapped_column

@dataclass
class User(db.Model):
    __tablename__ = "User"

    UserId: Mapped[int] = mapped_column(primary_key=True)
    Username: Mapped[str] = mapped_column(String(128), unique=True)
    Password: Mapped[str] = mapped_column(String(128))