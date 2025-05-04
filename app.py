from flask import Flask, render_template as render, request as req, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_restful import Api, Resource
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os


# Load environment variables form .env file
load_dotenv()


# Initialize Flask app
app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///anime.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
app.config['BOOTSTRAP_USE_MINIFIED'] = True
app.config['BOOTSTRAP_CDN'] = True


# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
api = Api(app)
bootstrap = Bootstrap(app)
bcrypt = Bcrypt(app)
CORS(app)


# Configure login manager
login_manager.login_view = 'login'
login_manager.login_message = 'Please log in to access this page.'
login_manager.login_message_category = 'info'


# Create a models for the database
