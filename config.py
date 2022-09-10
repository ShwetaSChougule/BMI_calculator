class Config():
    SECRET_KEY = 'qwertsyu123'
#     sqlalchemy db URI = <dilect+driver>://<user>:<password>@<IP>/<databasename>
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/bmi_db'    #user_info - db name
    SQLALCHEMY_TRACK_MODIFICATIONS =False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True

class TestingConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/testing_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False

# we created a dict:
app_config ={
    'development':DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}