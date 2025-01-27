import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://neondb_owner:GBYUhV93gPwC@ep-wispy-art-a4rjnsko.us-east-1.aws.neon.tech/neondb?sslmode=require')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)  # or another method to set a secret key

