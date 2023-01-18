from flask import Flask
from flask_smorest import abort, Api

from opt.resources.user import blp as UserBlueprint
from opt.resources.category import blp as CategoryBlueprint
from opt.resources.cost import blp as CostBlueprint
from opt.resources.currency import blp as CurrencyBlueprint

from opt.db import db


def create_app():
    app = Flask(__name__)
    app.secret_key = "super secret key"
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Finance REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.8.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(UserBlueprint)
    api.register_blueprint(CategoryBlueprint)
    api.register_blueprint(CostBlueprint)
    api.register_blueprint(CurrencyBlueprint)

    return app

