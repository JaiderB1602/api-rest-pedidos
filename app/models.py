from app import db

# Modelo de Usuario
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pedidos = db.relationship('Pedido', backref='usuario', cascade='all, delete-orphan')  # Eliminación en cascada

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email
        }

# Modelo de Pedido
class Pedido(db.Model):
    __tablename__ = 'pedidos'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    producto = db.Column(db.String(80), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "producto": self.producto,
            "cantidad": self.cantidad
        }