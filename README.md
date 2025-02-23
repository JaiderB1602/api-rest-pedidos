# API REST de Pedidos

Este proyecto es una API REST desarrollada con Flask que permite gestionar usuarios y pedidos. La API está dockerizada para facilitar su despliegue y utiliza SQLite como base de datos.

---

## **Tabla de Contenidos**
1. [Requisitos](#requisitos)
2. [Configuración](#configuración)
3. [Ejecución](#ejecución)
4. [Endpoints](#endpoints)
5. [Despliegue en la nube](#despliegue-en-la-nube)
6. [Contribuciones](#contribuciones)

---

## **Requisitos**

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Postman](https://www.postman.com/) (opcional, para probar los endpoints)

---

## **Configuración**

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/JaiderB1602/api-rest-pedidos.git
   cd api-rest-pedidos
Construye y ejecuta los contenedores:

bash
Copy
docker-compose up --build
Esto levantará un contenedor para la API Flask en el puerto 5000.

Ejecución
Una vez que los contenedores estén en ejecución, puedes acceder a la API en:

Copy
http://localhost:5000
Endpoints
Usuarios
Obtener todos los usuarios:

Método: GET

URL: http://localhost:5000/api/usuarios

Obtener un usuario específico:

Método: GET

URL: http://localhost:5000/api/usuarios/<id>

Crear un nuevo usuario:

Método: POST

URL: http://localhost:5000/api/usuarios

Body (JSON):

json:

Copy
{
  "nombre": "Nombre del usuario",
  "email": "usuario@example.com"
}
Actualizar un usuario:

Método: PUT

URL: http://localhost:5000/api/usuarios/<id>

Body (JSON):

json:

Copy
{
  "nombre": "Nuevo nombre",
  "email": "nuevo@email.com"
}
Eliminar un usuario:

Método: DELETE

URL: http://localhost:5000/api/usuarios/<id>

Pedidos
Obtener todos los pedidos:

Método: GET

URL: http://localhost:5000/api/pedidos

Obtener un pedido específico:

Método: GET

URL: http://localhost:5000/api/pedidos/<id>

Crear un nuevo pedido:

Método: POST

URL: http://localhost:5000/api/pedidos

Body (JSON):

json:

Copy
{
  "usuario_id": 1,
  "producto": "Nombre del producto",
  "cantidad": 2
}
Actualizar un pedido:

Método: PUT

URL: http://localhost:5000/api/pedidos/<id>

Body (JSON):

json:

Copy
{
  "producto": "Nuevo producto",
  "cantidad": 5
}
Eliminar un pedido:

Método: DELETE

URL: http://localhost:5000/api/pedidos/<id>

Despliegue en la nube
Este proyecto puede ser desplegado en servicios como Render, Railway, o Heroku. Asegúrate de configurar las variables de entorno necesarias (por ejemplo, DATABASE_URL).

Contribuciones
Si deseas contribuir a este proyecto, sigue estos pasos:

Haz un fork del repositorio.

Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).

Haz commit de tus cambios (git commit -m 'Añade nueva funcionalidad').

Haz push a la rama (git push origin feature/nueva-funcionalidad).

Abre un Pull Request.


Contacto
Si tienes alguna pregunta o sugerencia, no dudes en contactarme:

Nombre: Jaider Giovanny Bernal Sierra.

Correo: jaiderbernalsierra@gmail.com

GitHub: JaiderB1602