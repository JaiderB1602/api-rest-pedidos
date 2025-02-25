from flask import Flask, jsonify, request, redirect
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
    
    # Habilitar CORS solo para HTTPS
    CORS(app, supports_credentials=True)  

    # Forzar HTTPS en producción
    @app.before_request
    def before_request():
        """Redirige HTTP a HTTPS en producción"""
        if request.headers.get("X-Forwarded-Proto") == "http":
            return redirect(request.url.replace("http://", "https://"), code=301)
    
    # Registrar el Blueprint (rutas)
    from app.routes import bp
    app.register_blueprint(bp)
    
    # Configuración de Swagger UI
    from swagger import swagger_config

    @app.route('/api/swagger.json')
    def get_swagger():
        return jsonify(swagger_config())
    
    SWAGGER_URL = '/docs'  # URL para acceder a la interfaz Swagger UI
    API_URL = 'https://api-rest-pedidos-production.up.railway.app/api/swagger.json'  # URL corregida con HTTPS
    
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "API REST Pedidos",
            'validatorUrl': None,  # Evita errores de validación automática
        }
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    
    return app
