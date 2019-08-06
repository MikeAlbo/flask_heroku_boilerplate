from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# init the database
db = SQLAlchemy()
migrate = Migrate()


def create_app(**config_override):
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # print("app settings", os.environ['APP_SETTINGS'])
    app.config.update(config_override)

    # ini the db
    db.init_app(app)
    migrate.init_app(app, db)

    # init the blueprint
    from application.api.api import demo_api_blueprint

    # register the blueprint
    app.register_blueprint(demo_api_blueprint)

    # @app.route("/")
    # def test_route():
    #     return "test route working \n"

    return app




