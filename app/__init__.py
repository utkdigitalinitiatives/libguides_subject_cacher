from flask import Flask
from flask_cors import CORS
import sys

app = Flask(__name__)
app.config.from_object('config')
CORS(app)

print("Starting Flask")
sys.stdout.flush()

from app import views
