def swagger_config():
    return {
        "swagger": "2.0",
        "info": {
            "title": "API REST Pedidos",
            "description": "API para gestionar usuarios y pedidos",
            "version": "1.0.0"
        },
        "basePath": "/api",
        "schemes": ["https"],
        "paths": {
            "/usuarios": {
                "get": get_usuarios_config(),
                "post": post_usuario_config()
            },
            "/usuarios/{id}": {
                "get": get_usuario_by_id_config(),
                "put": put_usuario_config(),
                "delete": delete_usuario_config()
            },
            "/pedidos": {
                "get": get_pedidos_config(),
                "post": post_pedido_config()
            },
            "/pedidos/{id}": {
                "get": get_pedido_by_id_config(),
                "put": put_pedido_config(),
                "delete": delete_pedido_config()
            }
        },
        "definitions": {
            "UsuarioCreate": usuario_create_schema(),
            "PedidoCreate": pedido_create_schema()
        }
    }

# Configuraciones para los endpoints de Usuarios
def get_usuarios_config():
    return {
        "summary": "Obtener todos los usuarios",
        "produces": ["application/json"],
        "tags": ["Usuarios"],
        "responses": {
            "200": {
                "description": "Lista de usuarios"
            }
        }
    }

def get_usuario_by_id_config():
    return {
        "summary": "Obtener un usuario por ID",
        "produces": ["application/json"],
        "tags": ["Usuarios"],
        "parameters": [
            {
                "name": "id",
                "in": "path",
                "type": "integer",
                "required": True,
                "description": "ID del usuario"
            }
        ],
        "responses": {
            "200": {
                "description": "Usuario encontrado"
            },
            "404": {
                "description": "Usuario no encontrado"
            }
        }
    }

def post_usuario_config():
    return {
        "summary": "Crear un nuevo usuario",
        "produces": ["application/json"],
        "tags": ["Usuarios"],
        "parameters": [
            {
                "name": "usuario",
                "in": "body",
                "description": "Datos del usuario",
                "schema": {
                    "$ref": "#/definitions/UsuarioCreate"
                }
            }
        ],
        "responses": {
            "201": {
                "description": "Usuario creado"
            }
        }
    }

def put_usuario_config():
    return {
        "summary": "Actualizar un usuario",
        "produces": ["application/json"],
        "tags": ["Usuarios"],
        "parameters": [
            {
                "name": "id",
                "in": "path",
                "type": "integer",
                "required": True,
                "description": "ID del usuario"
            },
            {
                "name": "usuario",
                "in": "body",
                "description": "Datos actualizados",
                "schema": {
                    "$ref": "#/definitions/UsuarioCreate"
                }
            }
        ],
        "responses": {
            "200": {
                "description": "Usuario actualizado"
            },
            "404": {
                "description": "Usuario no encontrado"
            }
        }
    }

def delete_usuario_config():
    return {
        "summary": "Eliminar un usuario",
        "produces": ["application/json"],
        "tags": ["Usuarios"],
        "parameters": [
            {
                "name": "id",
                "in": "path",
                "type": "integer",
                "required": True,
                "description": "ID del usuario"
            }
        ],
        "responses": {
            "204": {
                "description": "Usuario eliminado"
            },
            "404": {
                "description": "Usuario no encontrado"
            }
        }
    }

# Configuraciones para los endpoints de Pedidos
def get_pedidos_config():
    return {
        "summary": "Obtener todos los pedidos",
        "produces": ["application/json"],
        "tags": ["Pedidos"],
        "responses": {
            "200": {
                "description": "Lista de pedidos"
            }
        }
    }

def get_pedido_by_id_config():
    return {
        "summary": "Obtener un pedido por ID",
        "produces": ["application/json"],
        "tags": ["Pedidos"],
        "parameters": [
            {
                "name": "id",
                "in": "path",
                "type": "integer",
                "required": True,
                "description": "ID del pedido"
            }
        ],
        "responses": {
            "200": {
                "description": "Pedido encontrado"
            },
            "404": {
                "description": "Pedido no encontrado"
            }
        }
    }

def post_pedido_config():
    return {
        "summary": "Crear un nuevo pedido",
        "produces": ["application/json"],
        "tags": ["Pedidos"],
        "parameters": [
            {
                "name": "pedido",
                "in": "body",
                "description": "Datos del pedido",
                "schema": {
                    "$ref": "#/definitions/PedidoCreate"
                }
            }
        ],
        "responses": {
            "201": {
                "description": "Pedido creado"
            }
        }
    }

def put_pedido_config():
    return {
        "summary": "Actualizar un pedido",
        "produces": ["application/json"],
        "tags": ["Pedidos"],
        "parameters": [
            {
                "name": "id",
                "in": "path",
                "type": "integer",
                "required": True,
                "description": "ID del pedido"
            },
            {
                "name": "pedido",
                "in": "body",
                "description": "Datos actualizados",
                "schema": {
                    "$ref": "#/definitions/PedidoCreate"
                }
            }
        ],
        "responses": {
            "200": {
                "description": "Pedido actualizado"
            },
            "404": {
                "description": "Pedido no encontrado"
            }
        }
    }

def delete_pedido_config():
    return {
        "summary": "Eliminar un pedido",
        "produces": ["application/json"],
        "tags": ["Pedidos"],
        "parameters": [
            {
                "name": "id",
                "in": "path",
                "type": "integer",
                "required": True,
                "description": "ID del pedido"
            }
        ],
        "responses": {
            "204": {
                "description": "Pedido eliminado"
            },
            "404": {
                "description": "Pedido no encontrado"
            }
        }
    }

# Definiciones de esquemas
def usuario_create_schema():
    return {
        "type": "object",
        "required": ["nombre", "email"],  # No incluir "id" aquí
        "properties": {
            "nombre": {
                "type": "string"
            },
            "email": {
                "type": "string"
            }
        }
    }


def pedido_create_schema():
    return {
        "type": "object",
        "required": ["usuario_id", "producto", "cantidad"],
        "properties": {
            "usuario_id": {
                "type": "integer"
            },
            "producto": {
                "type": "string"
            },
            "cantidad": {
                "type": "integer"
            }
        }
    }