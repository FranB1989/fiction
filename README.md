# Prueba Técnica

Este proyecto es una aplicación Django que incluye funcionalidades para manejar entradas de blog y gestionar usuarios a través de diferentes grupos con permisos específicos.

## Requisitos

- Python 3.12
- Django
- Docker

## Instalación

1. **Clonar el Repositorio**
   ```bash
   git clone https://github.com/FranB1989/fiction.git
   cd fiction

2. **Crear un Entorno Virtual**

```bash
python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
```

## Instalar Dependencias

```bash
pip install -r requirements.txt
```

## Configurar la Base de Datos

Asegúrate de que la base de datos está configurada correctamente en `settings.py`.

## Cargar y Ejecutar la Imagen Docker

### Cargar la Imagen Docker

En la instancia EC2, cargamos la imagen Docker mediante el comando:

```bash
docker load -i prueba_fran_barcia.tar
```

### Ejecutar un Contenedor a Partir de la Imagen

```bash
docker run -d -p 0:8000 prueba_fran_barcia
```

## Configuraciones

Debemos asegurarnos de que el grupo de seguridad de la instancia EC2 permite el tráfico SSH y HTTP para acceder a la aplicación desde el navegador. Es necesario que el fichero “pem” de las claves tenga los permisos correctos.

## Acceso y Configuración del Contenedor Docker

### Obtener el Nombre o ID del Contenedor

Después de ejecutar la imagen Docker, obtenemos el nombre o ID del contenedor con el siguiente comando:

```bash
docker ps
```

### Acceder al Contenedor

Para ejecutar comandos dentro del contenedor, usamos el nombre o ID obtenido. Ejecutamos:

```bash
docker exec -it nombre_o_id_del_contenedor /bin/bash
```

### Ejecutar Migraciones

Una vez dentro, aplicamos las migraciones de la base de datos:

```bash
python manage.py migrate
```

### Crear un Superusuario

A continuación, creamos un superusuario:

```bash
python manage.py createsuperuser
```

### Crear Grupos y Asignar Permisos

Finalmente, ejecutamos el comando para crear los grupos:

```bash
python manage.py create_groups
```
