#!/usr/bin/python3
"""Flask server (variable app)
"""


from flask import Flask
from models import storage
from os import getenv
from api.v1.views import app_views

app = Flask(__name__)

app.register_blueprint(app_views)



if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', 5000)
    app.run(host=host, port=port, threaded=True)