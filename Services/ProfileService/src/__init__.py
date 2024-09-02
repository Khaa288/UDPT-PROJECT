from flask import Flask
import os
from src.config.config import Config
from dotenv import load_dotenv
from src.routes import api
from src.models import db, migrate, ma

# loading environment variables
load_dotenv()

# declaring flask application
app = Flask(__name__)

# calling the dev configuration
config = Config().dev_config

# making our application to use dev env
app.env = config.ENV

# Path for our local sql lite database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLACHEMY_DATABASE_URI")

# To specify to track modifications of objects and emit signals
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")

# import api blueprint to register it with app
app.register_blueprint(api, url_prefix = "/api")

# import db and migration
db.init_app(app)
migrate.init_app(app, db)

# import marshmallow for mapping
ma.init_app(app)

# Client to eureka server
import py_eureka_client.eureka_client as eureka_client
eureka_client.init(eureka_server="http://localhost:8761/",
                    app_name="profile_service",
                    instance_ip=config.HOST,
                    instance_port=config.PORT,
                    instance_host='localhost')