from flask import Flask
from flask_mysqldb import MySQL
import cloudinary
import cloudinary.uploader
import cloudinary.api

cloudinary.config(
    cloud_name='dy6xdxgvl',
    api_key='484464816794794',
    api_secret='HLw5tgKnuys4IWnpOmTqV_jz-S0'
)


def create_app():
    app = Flask(__name__)
    
    app.secret_key = 'joshua'
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'joshua'
    app.config['MYSQL_DB'] = 'ssis'
    
    mysql = MySQL(app)
    
    from .main_route import views
    app.register_blueprint(views)
    
    from .Controller.student_routes import student_bp
    app.register_blueprint(student_bp)
    
    from .Controller.program_routes import program_bp
    app.register_blueprint(program_bp)
    
    from .Controller.college_routes import college_bp
    app.register_blueprint(college_bp)

    return app