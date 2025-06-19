import uuid
import logging
from flask import Flask, request, render_template
from pymongo import MongoClient

# Use flask-session instead of flask-sessionstore (recommended for newer versions)
from flask_session import Session
from flask_session_captcha import FlaskSessionCaptcha

app = Flask(__name__)

# Database Config
mongoClient = MongoClient('localhost', 27017)

# Session Configuration
app.config['SECRET_KEY'] = str(uuid.uuid4())
app.config['SESSION_TYPE'] = 'filesystem'

app.config['SESSION_MONGODB'] = mongoClient
app.config['SESSION_MONGODB_DB'] = 'flask_session_db'
app.config['SESSION_MONGODB_COLLECTION'] = 'sessions'  # Explicit collection name

# Captcha Configuration
app.config['CAPTCHA_ENABLE'] = True
app.config['CAPTCHA_LENGTH'] = 5
app.config['CAPTCHA_WIDTH'] = 160
app.config['CAPTCHA_HEIGHT'] = 60

# Initialize extensions
Session(app)  # Initialize session first
captcha = FlaskSessionCaptcha(app)  # Then captcha

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        if captcha.validate():
            return "success"
        return "fail"
    return render_template("form.html")

if __name__ == "__main__":
    app.debug = True
    logging.basicConfig(level=logging.DEBUG)
    app.run()