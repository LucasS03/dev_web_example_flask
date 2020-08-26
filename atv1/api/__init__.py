from flask import Flask

app = Flask(__name__)
# app.config['DEBUG'] = True
app.debug = True

from api import routes