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
from src.models.activity_model import Activity
from src.models.participant_model import Participant
from src.models.token_model import Token
