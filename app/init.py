from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    # Load config from app/config.py -> class Config
    app.config.from_object('app.config.Config')

    # Enable CORS (optional)
    CORS(app)

    # Register routes blueprint
    from app.routes import bp
    app.register_blueprint(bp)

    return app
