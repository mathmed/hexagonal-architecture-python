from .flask_adapter import api_routes
import os
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

def main():
    CORS(app)
    app.register_blueprint(api_routes)
    app.run(host='0.0.0.0', port=os.getenv('APP_PORT'))

