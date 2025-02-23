import os

# Obtener la ruta absoluta del directorio actual
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Configuración de la base de datos SQLite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'BaseProyecto.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desactiva las notificaciones de modificaciones
    SECRET_KEY = '3c264d43624ea52126ef6107585c2de1'  # Clave secreta para la aplicación