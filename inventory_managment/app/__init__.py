from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# from app.routes.inventory_routes import bp as inventory_bp
# from app.routes.api_routes import api_bp


db = SQLAlchemy()
print(db)
migrate  = Migrate()

def crete_app(config_class = 'config.dev.DevConfig'):
    #create flask app
    app = Flask(__name__)

    #load configration
    app.config.from_object(config_class)

    # Initialize extention

    # Binds the SQLAlchemy instance to the Flask application.
    db.init_app(app)

    # Associates the migration engine with the application and the database.
    migrate.init_app(app, db)

    #Ensures that the application context is available when importing models
    with app.app_context():
        from app import models     # Import models to register them with SQLAlchemy

    # # Register blueprint
    # app.register_blueprint(inventory_bp)
    # app.register_blueprint(api_bp)

    return app
