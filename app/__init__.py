from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():

    app = Flask(__name__)

    db.init_app(app)

    from .main import main_bp
    app.register_blueprint(main_bp)

    from .apiv1 import apiv1_bp
    app.register_blueprint(apiv1_bp, url_prefix='/api')

    return app
