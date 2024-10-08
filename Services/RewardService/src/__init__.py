from flask import Flask
import os
from src.config.config import Config
from dotenv import load_dotenv
from src.routes import api
from src.models import ma
from src.background_jobs import scheduler, BackgroundConfig

# loading environment variables
load_dotenv()

# declaring flask application
app = Flask(__name__)

# calling the dev configuration
config = Config().dev_config

# making our application to use dev env
app.env = config.ENV

# import api blueprint to register it with app
app.register_blueprint(api, url_prefix = "/api")

# import marshmallow for mapping
ma.init_app(app)

# import background jobs
app.config.from_object(BackgroundConfig())
scheduler.init_app(app)
scheduler.start()

import py_eureka_client.eureka_client as eureka_client
eureka_client.init(eureka_server="http://localhost:8761/",
                    app_name="reward_service",
                    instance_ip=config.HOST,
                    instance_port=config.PORT,
                    instance_host='localhost')