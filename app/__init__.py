from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS  # Importa CORS
from config import Config

# Crear una instancia de SQLAlchemy
db = SQLAlchemy()

def create_app():
    # Crear la aplicación Flask
    app = Flask(__name__)
    app.config.from_object(Config)  # Cargar la configuración desde config.py
    
    # Inicializar la base de datos con la aplicación
    db.init_app(app)
    
    # Habilitar CORS para todas las rutas
    CORS(app)  # Esto habilita CORS para todas las rutas
    
    # Registrar el Blueprint (rutas)
    from app.routes import bp
    app.register_blueprint(bp)
    
    # Configuración de Swagger UI
    from swagger import swagger_config
    
    @app.route('/api/swagger.json')
    def get_swagger():
        return jsonify(swagger_config())
    
    SWAGGER_URL = '/docs'  # URL para acceder a la interfaz Swagger UI
    API_URL = '/api/swagger.json'  # Donde se encuentra tu especificación Swagger
    
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "API REST Pedidos"
        }
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    
    return app