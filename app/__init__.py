# Import flask and template operators
from flask import Flask, render_template

# Import flask flask swagger ui
from flask_swagger_ui import get_swaggerui_blueprint


from flask_sqlalchemy import SQLAlchemy
#from flask_mysqldb import MySQL

# Define the WSGI application object
app = Flask(__name__, instance_relative_config=True)



# Load the default configuration
#app.config.from_object('config.default')

# Load the configuration from the instance folder
app.config.from_pyfile('config.py')

# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration
#PP_CONFIG_FILE = '/mnt/g/flask_project/instance/G:/flask_project/config/local.py'
#app.config.from_envvar('APP_CONFIG_FILE')


# Define the database object which is imported
# by modules and controllers
#mysql = MySQL(app)
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


from app.api_home.controllers import bp_home as home_bp

app.register_blueprint(home_bp)
