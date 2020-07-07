# Imports
from flask import Flask
from config import Config
from logger import logger
from flask_migrate import Migrate



LOGGER = logger(__name__)
# app initialization
app = Flask(__name__)
app.debug = True

# Configs
app.config['DEBUG'] = Config.DEBUG
# TO-DO# Modules
# TO-DO# Models
# TO-DO# Schema Objects
# TO-DO# Routes
# TO-DO


@app.route('/')
def index():
    return '<p> Welcome to Book Bee</p>'


if __name__ == '__main__':
    app.run()
