from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Crear una instancia de SQLAlchemy
db = SQLAlchemy()

def create_app():
    # Crear la aplicación Flask
    app = Flask(__name__)
    app.config.from_object(Config)  # Cargar la configuración desde config.py
    
    # Inicializar la base de datos con la aplicación
    db.init_app(app)
    
    # Registrar el Blueprint (rutas)
    from app.routes import bp
    app.register_blueprint(bp)
    
    return app