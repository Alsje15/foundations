from flask import Flask
from . import routes
from app.extensions.database import db, migrate
from app.extensions.authentication import login_manager

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    register_extensions(app)
    register_blueprints(app)

    return app

# Initialise blueprints
def register_blueprints(app:Flask):
    app.register_blueprint(routes.routes.blueprint)

# Initialise db
def register_extensions(app:Flask):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
