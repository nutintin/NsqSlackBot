from flask import Flask
from flask_compress import Compress
from flask_cors import CORS

from rest.helpers import mongo
from rest.routes import nsq

compress = Compress()
cors = CORS()


def create_app(configuration):
    app = Flask(__name__.split(',')[0], static_url_path='/static', 
                static_folder='../static')

    # Register route blueprint
    app.register_blueprint(nsq.bp)

    # load configuration
    app.config.from_object(configuration)

    # flask extensions initialization
    # mongo init
    mongo.init_app(app)

    compress.init_app(app)
    cors.init_app(app, resources={r"/*": {"origins": "*"}})

    return app