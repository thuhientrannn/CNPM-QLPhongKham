from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import cloudinary
from flask_login import LoginManager
from twilio.rest import Client

app = Flask(__name__)

app.secret_key = "super key" #akj+fg823762531341=2901r-9sd-7g2f98r3sa8d1-2751849
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@localhost/phongkhamdb?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

cloudinary.config(
    cloud_name='cloud_name',
    api_key='api_key',
    api_secret='api_secret'
)

#twilio infomation
keys = {
    'account_sid': 'account_sid',
    'auth_token': 'auth_token',
    'twilio_number': '+123456789'
}
#client = Client(account_sid, auth_token)
client = Client(keys['account_sid'], keys['auth_token'])

db = SQLAlchemy(app=app)
login = LoginManager(app=app)
