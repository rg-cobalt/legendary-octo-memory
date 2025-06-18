from flask import Flask
from config import SECRET_KEY

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['DEBUG'] = True  # Insecure for production

    from .routes import main
    app.register_blueprint(main)

    return app
