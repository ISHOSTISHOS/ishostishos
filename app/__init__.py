from flask import Flask

app = Flask(__name__)
app.secret_key = 'djsndsjd'
from app import routes