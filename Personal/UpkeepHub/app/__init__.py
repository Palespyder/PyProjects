from flask import Flask
from .models import db
import os
from .routes.auth_routes import auth_bp
from .routes.equipment_routes import equipment_bp
from .routes.home_routes import home_bp
from .routes.livestock_routes import livestock_bp
from .routes.outbuilding_routes import outbuildings_bp
from .routes.pet_routes import pets_bp
from .routes.vehicle_routes import vehicles_bp

def create_app():
    app = Flask(__name__, static_folder='static', static_url_path='')

    # Load configuration
    app.config.from_object('config.Config')    

    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    
    # Load configuration from environment variables
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', '45UP3R53CR3TK3Y')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', f'sqlite:///{os.path.join(BASEDIR, "./data", "upkeephub.db")}')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize database
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(equipment_bp, url_prefix='/equipment')
    app.register_blueprint(home_bp, url_prefix='/')
    app.register_blueprint(livestock_bp, url_prefix='/livestock')
    app.register_blueprint(outbuildings_bp, url_prefix='/outbuildings')
    app.register_blueprint(pets_bp, url_prefix='/pets')
    app.register_blueprint(vehicles_bp, url_prefix='/vehicles')    

    return app
