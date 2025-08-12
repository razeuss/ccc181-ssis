from flask import Flask
from flask_mysqldb import MySQL
import cloudinary
import cloudinary.uploader
import cloudinary.api
from config import SECRET_KEY, MYSQL_DB, MYSQL_HOST, MYSQL_PASSWORD, MYSQL_USER, CLOUD_API_KEY, CLOUD_API_SECRET, CLOUD_NAME

cloudinary.config(
    cloud_name=CLOUD_NAME,
    api_key=CLOUD_API_KEY,
    api_secret=CLOUD_API_SECRET
)


def create_app():
    app = Flask(__name__)
    
    app.secret_key = SECRET_KEY
    app.config['MYSQL_HOST'] = MYSQL_HOST
    app.config['MYSQL_USER'] = MYSQL_USER
    app.config['MYSQL_PASSWORD'] = MYSQL_PASSWORD
    app.config['MYSQL_DB'] = MYSQL_DB
    
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