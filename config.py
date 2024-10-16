import os

class Config:
    password = os.getenv('SQL_PASS')
    SQLALCHEMY_DATABASE_URI = 'mysql://root:%s@localhost/url_shortener_db', (password)
    SQLALCHEMY_TRACK_MODIFICATIONS = False