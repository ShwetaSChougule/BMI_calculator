from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config

db = SQLAlchemy()
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    from BMI_calculator.bmi.views import mod as bmi_cal
    app.register_blueprint(bmi_cal)
    db.init_app(app)
    return app
