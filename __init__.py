from flask import Flask
from user_login.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

flaskApp = Flask(__name__)
flaskApp.config.from_object(Config)
db = SQLAlchemy(flaskApp)
migrate = Migrate(flaskApp, db)
login = LoginManager(flaskApp)
login.login_view = 'login'

from user_login import routes, models