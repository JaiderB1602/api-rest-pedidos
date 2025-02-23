from flask import Blueprint, jsonify, request
from app.models import db, Usuario, Pedido

# Define el Blueprint con un prefijo de ruta
bp = Blueprint('api', __name__, url_prefix='/api')

# Rutas para Usuarios
@bp.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([usuario.to_dict() for usuario in usuarios])

@bp.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    return jsonify(usuario.to_dict())

@bp.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.get_json()
    nuevo_usuario = Usuario(
        nombre=data['nombre'],
        email=data['email']
    )
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify(nuevo_usuario.to_dict()), 201

@bp.route('/usuarios/<int:id>', methods=['PUT'])
def update_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    data = request.get_json()
    usuario.nombre = data.get('nombre', usuario.nombre)
    usuario.email = data.get('email', usuario.email)
    db.session.commit()
    return jsonify(usuario.to_dict())

@bp.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return '', 204  # Respuesta vacía con código 204 (No Content)

# Rutas para Pedidos
@bp.route('/pedidos', methods=['GET'])
def get_pedidos():
    pedidos = Pedido.query.all()
    return jsonify([pedido.to_dict() for pedido in pedidos])

@bp.route('/pedidos/<int:id>', methods=['GET'])
def get_pedido(id):
    pedido = Pedido.query.get_or_404(id)
    return jsonify(pedido.to_dict())

@bp.route('/pedidos', methods=['POST'])
def create_pedido():
    data = request.get_json()
    nuevo_pedido = Pedido(
        usuario_id=data['usuario_id'],
        producto=data['producto'],
        cantidad=data['cantidad']
    )
    db.session.add(nuevo_pedido)
    db.session.commit()
    return jsonify(nuevo_pedido.to_dict()), 201

@bp.route('/pedidos/<int:id>', methods=['PUT'])
def update_pedido(id):
    pedido = Pedido.query.get_or_404(id)
    data = request.get_json()
    pedido.producto = data.get('producto', pedido.producto)
    pedido.cantidad = data.get('cantidad', pedido.cantidad)
    db.session.commit()
    return jsonify(pedido.to_dict())

@bp.route('/pedidos/<int:id>', methods=['DELETE'])
def delete_pedido(id):
    pedido = Pedido.query.get_or_404(id)
    db.session.delete(pedido)
    db.session.commit()
    return '', 204  # Respuesta vacía con código 204 (No Content)