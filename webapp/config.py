import os

basedir = os.path.abspath(os.path.dirname(__file__))


WEATHER_DEFAULT_CITY = "London"
WEATHER_API_KEY = "e781992e8f1f4b0fbcb95744210809" 
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'..','webapp.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False