from flask import Flask
import os
from src.config.config import Config
from dotenv import load_dotenv

# loading environment variables
load_dotenv()

# declaring flask application
app = Flask(__name__)

# calling the dev configuration
config = Config().dev_config

# making our application to use dev env
app.env = config.ENV

import py_eureka_client.eureka_client as eureka_client
eureka_client.init(eureka_server="http://localhost:8761/",
                    app_name="api_gateway",
                    instance_ip=config.HOST,
                    instance_port=config.PORT,
                    instance_host='localhost')

res = eureka_client.do_service("profile_service", "/api/employee/1")
print("result of other service" + res)