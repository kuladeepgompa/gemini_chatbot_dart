from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.routes import api

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    CORS(app, origins=Config.CORS_ORIGINS)

    # Register blueprints
    app.register_blueprint(api, url_prefix='/api/v1')

    return app
