from flask import Flask
from flask_mysqldb import MySQL


def create_app():
    app = Flask(__name__)
    
    app.secret_key = 'joshua'
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'joshua'
    app.config['MYSQL_DB'] = 'ssis'
    
    mysql = MySQL(app)
    
    from .routes import views
    app.register_blueprint(views)

    return app