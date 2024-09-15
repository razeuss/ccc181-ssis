from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import the blueprint
    from .routes import views

    # Register the blueprint (without url_prefix)
    app.register_blueprint(views)

    return app