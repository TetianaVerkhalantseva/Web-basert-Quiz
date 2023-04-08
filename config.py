import secrets


class BaseConfig:
    SECRET_KEY = secrets.token_urlsafe(32)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://stud_v23_tda072:2021T-Dakhno32\
    @kark.uit.no:3306/stud_v23_tda072?charset=utf8"
