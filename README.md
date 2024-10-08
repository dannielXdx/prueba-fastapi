# Autenticación de usuarios con JWT usando FastAPI con microservicios RESTful 

## Descripción

Este proyecto es un microservicio de autenticación desarrollado con **FastAPI** que utiliza JWT (JSON Web Tokens) para manejar la autenticación de usuarios. El microservicio permite registrar usuarios, iniciar sesión, refrescar tokens, verificar la validez de tokens y cerrar sesión.

## Estrategia de Desarrollo

### 1. **Tecnologías Utilizadas**
   - **FastAPI**: Framework web moderno y de alto rendimiento para construir APIs con Python 3.10+.
   - **SQLite**: Base de datos liviana utilizada para almacenar los datos de los usuarios.
   - **SQLAlchemy**: ORM (Object-Relational Mapping) para interactuar con la base de datos de manera más eficiente.
   - **JWT (JSON Web Tokens)**: Utilizado para la autenticación segura de los usuarios.
   - **bcrypt**: Algoritmo de hashing de contraseñas para almacenar contraseñas de forma segura.
   - **pytest**: Framework de pruebas utilizado para las pruebas unitarias del proyecto.
   - **Docker**: Entorno para correr el proyecto de forma estandarizada con contenedores.



### 2. **Pasos de Implementación**
- **Configuración Inicial**: Se creó el entorno de desarrollo, configurando la estructura básica del proyecto y asegurando que las dependencias estuvieran correctamente instaladas.

- **Base de Datos**: Se configuró SQLite como la base de datos utilizando SQLAlchemy para manejar las interacciones con la base de datos de manera ORM. Esto incluyó la creación de modelos de usuario y la gestión de la conexión a la base de datos.

- **Autenticación JWT**: Se implementó la lógica para generar y verificar JWTs usando la librería `python-jose`, asegurando la seguridad mediante el uso de `bcrypt` para el hashing de contraseñas.

- **Rutas de Autenticación**: Se implementaron las rutas de registro, inicio de sesión, refresh token, verificación de token y logout. Cada ruta está diseñada para interactuar con la base de datos y manejar la lógica de autenticación de manera segura.

- **Pruebas Unitarias**: Se añadieron pruebas unitarias utilizando `pytest` para verificar la funcionalidad de los endpoints clave del sistema. Las pruebas cubren los casos de registro, inicio de sesión, verificación de token, refresh token y logout.


## Ejecución del proyecto en local

1. Instala las dependencias en un entorno virtual con los comandos:
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
2. Crea el archivo `.env` tomando como referencia el `.env.example`.
```bash
cp .env.example .env
```

3. (OPCIONAL) Genera un SECRET_KEY y agregalo a la variable del `.env`. El siguiente comando es una sugerencia para generarlo:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

4. Despliega del servicio en modo desarrollo con el comando:
```bash
fastapi dev app/main.py
```

5. Puedes consultar la documentación de las APIs en http://127.0.0.1:8000/docs/ para comenzar a usarlas.


## Ejecución del proyecto con Docker

1. Crea el archivo `.env` tomando como referencia el `.env.example`.
```bash
cp .env.example .env
```

2. (OPCIONAL) Genera un SECRET_KEY y agregalo a la variable del `.env`. El siguiente comando es una sugerencia para generarlo:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

3. Para desplegar el contenedor, usa el siguiente comando:

```bash
docker-compose up --build
```
Este mismo ejecuta los test antes de levantar el servidor, aunque también se pueden correr los test de forma independiente.

## Ejecución de pruebas

Las pruebas unitarias están diseñadas para garantizar que los endpoints funcionen como se espera. Las pruebas pueden ejecutarse utilizando `pytest` con el siguiente comando:

```bash
pytest
```

También se puede ejecutar una rutina dentro del contenedor para ejecutar los test con el siguiente comando:

```bash
docker-compose run test
```
