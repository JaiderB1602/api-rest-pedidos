API REST de Pedidos
Este proyecto es una API REST desarrollada con Flask que permite gestionar usuarios y pedidos. La API está dockerizada para facilitar su despliegue y utiliza SQLite como base de datos.

Tabla de Contenidos
Requisitos

Configuración

Ejecución

Endpoints

Pruebas con Postman

Despliegue en la nube

Contribuciones

Contacto

Requisitos

Docker

Docker Compose

Postman (opcional, para probar los endpoints)

Configuración
Clona el repositorio:


git clone https://github.com/JaiderB1602/api-rest-pedidos.git
cd api-rest-pedidos
Construye y ejecuta los contenedores:


docker-compose up --build
Esto levantará un contenedor para la API Flask en el puerto 5000.

Ejecución
Una vez que los contenedores estén en ejecución, puedes acceder a la API en:


http://localhost:5000
Endpoints
Usuarios
Obtener todos los usuarios:

Método: GET

URL: {{base_url}}/api/usuarios

Obtener un usuario específico:

Método: GET

URL: {{base_url}}/api/usuarios/<id>

Crear un nuevo usuario:

Método: POST

URL: {{base_url}}/api/usuarios

Body (JSON):

json


{
  "nombre": "Nombre del usuario",
  "email": "usuario@example.com"
}

Actualizar un usuario:

Método: PUT

URL: {{base_url}}/api/usuarios/<id>

Body (JSON):

json


{
  "nombre": "Nuevo nombre",
  "email": "nuevo@email.com"
}
Eliminar un usuario:

Método: DELETE

URL: {{base_url}}/api/usuarios/<id>

Pedidos
Obtener todos los pedidos:

Método: GET

URL: {{base_url}}/api/pedidos

Obtener un pedido específico:

Método: GET

URL: {{base_url}}/api/pedidos/<id>

Crear un nuevo pedido:

Método: POST

URL: {{base_url}}/api/pedidos

Body (JSON):

json


{
  "usuario_id": 1,
  "producto": "Nombre del producto",
  "cantidad": 2
}
Actualizar un pedido:

Método: PUT

URL: {{base_url}}/api/pedidos/<id>

Body (JSON):

json


{
  "producto": "Nuevo producto",
  "cantidad": 5
}
Eliminar un pedido:

Método: DELETE

URL: {{base_url}}/api/pedidos/<id>

Pruebas con Postman

Puedes probar los endpoints de la API utilizando Postman. Hemos preparado una colección de Postman y dos entornos preconfigurados (Local y Producción) para facilitar las pruebas.

Archivos disponibles

Colección de Postman

Entorno Local

Entorno Producción

Pasos para configurar Postman

Descarga los archivos:

Descarga los archivos de la colección y los entornos desde los enlaces anteriores o desde la carpeta /postman del repositorio.

Importa la colección y los entornos en Postman:

Abre Postman y haz clic en Import.

Selecciona los archivos collection.json, local_environment.json, y production_environment.json.

Selecciona el entorno:

En Postman, ve a la sección Environments (Entornos).

Selecciona el entorno que desees usar:

Local: Para pruebas en http://localhost:5000.

Producción (Cloud): Para pruebas en https://api-rest-pedidos-production.up.railway.app.

Prueba los endpoints:

Una vez configurado el entorno, puedes ejecutar las solicitudes de la colección. Todas las URLs usarán automáticamente la base_url del entorno seleccionado.

Ventajas de este enfoque

Facilidad de uso: Los usuarios no necesitan configurar manualmente las variables de entorno.

Flexibilidad: Pueden cambiar fácilmente entre entornos (local y producción) sin modificar las URLs.

Mantenimiento más fácil: Si actualizas la colección o los entornos, solo necesitas compartir los nuevos archivos.

Ejemplo de uso

Pruebas locales:

Selecciona el entorno Local.

Ejecuta las solicitudes de la colección. Las URLs apuntarán a http://localhost:5000.

Pruebas en la nube:

Selecciona el entorno Producción (Cloud).

Ejecuta las solicitudes de la colección. Las URLs apuntarán a https://api-rest-pedidos-production.up.railway.app

Despliegue en la nube

Este proyecto está desplegado en Railway. Puedes acceder a la API en la siguiente URL:


https://api-rest-pedidos-production.up.railway.app

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

Notas adicionales:

Variables de entorno: Si en el futuro necesitas configurar variables de entorno (como credenciales de bases de datos o claves API), puedes hacerlo en la sección Variables de Railway.

Si necesitas modificar las variables de entorno (por ejemplo, cambiar la base_url), puedes hacerlo directamente en Postman editando el entorno correspondiente.

Asegúrate de que tu aplicación esté en ejecución (localmente o en la nube) antes de probar los endpoints.