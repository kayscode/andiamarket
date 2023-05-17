from flask import Flask

from .blueprints.client import bp as bp_client
from .blueprints.company import bp as bp_company
from .blueprints.product import bp as bp_product


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    from .database.db import db
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    db.init_app(app)

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'this is our home page'

    app.register_blueprint(bp_client)
    app.register_blueprint(bp_company)
    app.register_blueprint(bp_product)

    return app
