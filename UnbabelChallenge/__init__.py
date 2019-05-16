"""
The flask application package.
"""
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime

app = Flask(__name__)
import UnbabelChallenge.views
