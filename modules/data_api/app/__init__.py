import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from app.config import config_by_name
from sqlalchemy import create_engine


print("Connecting to: " + config_by_name[os.getenv("FLASK_ENV") or "test"].SQLALCHEMY_DATABASE_URI)
engine = create_engine(config_by_name[os.getenv("FLASK_ENV") or "test"].SQLALCHEMY_DATABASE_URI)


def create_app(env=None):
    from app.config import config_by_name
    from app.routes import register_routes

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "test"])
    api = Api(app, title="UdaConnect DATA API", version="0.1.0")

    CORS(app)  # Set CORS for development

    register_routes(api, app)
    db.init_app(app)

    @app.route("/health")
    def health():
        return jsonify("healthy")

    return app
