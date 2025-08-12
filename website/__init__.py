from flask import Flask
from flask_mysqldb import MySQL
import cloudinary
import cloudinary.uploader
import cloudinary.api
from config import ( SECRET_KEY, MYSQL_DB, MYSQL_HOST, MYSQL_PASSWORD, 
                    MYSQL_USER, CLOUD_API_KEY, CLOUD_API_SECRET, CLOUD_NAME,
                    MYSQL_PORT, MYSQL_UNIX_SOCKET, MYSQL_READ_DEFAULT_FILE,
                    MYSQL_CONNECT_TIMEOUT, MYSQL_USE_UNICODE, MYSQL_CHARSET
                    , MYSQL_SQL_MODE, MYSQL_CURSORCLASS, MYSQL_AUTOCOMMIT)

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
    
    app.config['MYSQL_PORT'] = MYSQL_PORT
    app.config['MYSQL_UNIX_SOCKET'] = MYSQL_UNIX_SOCKET
    app.config['MYSQL_CONNECT_TIMEOUT'] = MYSQL_CONNECT_TIMEOUT
    app.config['MYSQL_READ_DEFAULT_FILE'] = MYSQL_READ_DEFAULT_FILE
    app.config['MYSQL_USE_UNICODE'] = MYSQL_USE_UNICODE
    app.config['MYSQL_CHARSET'] = MYSQL_CHARSET
    app.config['MYSQL_SQL_MODE'] = MYSQL_SQL_MODE
    app.config['MYSQL_CURSORCLASS'] = MYSQL_CURSORCLASS
    app.config['MYSQL_AUTOCOMMIT'] = MYSQL_AUTOCOMMIT
    app.config['MYSQL_CUSTOM_OPTIONS'] = {}

    
    from .main_route import views
    app.register_blueprint(views)
    
    from .Controller.student_routes import student_bp
    app.register_blueprint(student_bp)
    
    from .Controller.program_routes import program_bp
    app.register_blueprint(program_bp)
    
    from .Controller.college_routes import college_bp
    app.register_blueprint(college_bp)

    return app