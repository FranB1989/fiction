# Prueba Técnica

Este proyecto es una aplicación Django que incluye funcionalidades para manejar entradas de blog y gestionar usuarios a través de diferentes grupos con permisos específicos.

## Requisitos

- Python 3.12
- Django

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

### Ejecutar Migraciones

Aplicamos las migraciones de la base de datos:

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
