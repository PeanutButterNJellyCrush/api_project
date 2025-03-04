from flask import Flask
from init import db, ma
import os
from blueprints.db_bp import db_bp
from blueprints.students_bp import students_bp


def create_app():
    app = Flask(__name__)

    # connect to sql db
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URI")

    db.init_app(app)
    ma.init_app(app)

    # pass in blueprint. db_bp variable is passed in as parameter
    app.register_blueprint(db_bp)
    app.register_blueprint(students_bp)

    return app
