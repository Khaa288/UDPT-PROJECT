from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_marshmallow import Marshmallow

# sql alchemy instance
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

# Flask Migrate instance to handle migrations
migrate = Migrate()

ma = Marshmallow()

# import models to let the migrate tool know
from src.models.user_model import User
from src.models.employee_model import Employee
