from flask import Flask

app = Flask(__name__)
app.secret_key = "super secret key"

from opt import views
from opt import db
from opt.resources import user


# pip install flask-sqlalchemy