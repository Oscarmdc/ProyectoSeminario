# Proyecto Seminario de Programación
Proyecto final de seminario con Python, Django y PostgreSQL

## Requisitos
* Python 3.12.3
* Django 5.0.4
* PostgreSQL -> pgAdmin4

## Comandos esenciales
* Ejecutar servidor -> python manage.py runserver
* Crear una app -> python manage.py startapp nombre_app
* Comprobar salud de una app -> python manage.py check nombre_app
* Crear la base de datos -> python manage.py makemigrations
* Crear tablas y sql -> python manage.py sqlmigrate nombre_app num_migración
  * Ejemplo: python manage.py sqlmigrate articulos 0001
* Migrar tablas al db -> python manage.py migrate

## Operaciones CRUD Django
* Create (Insert): nom_var = Nom_Object.objects.create(campo_1= valor_1, campo_2= valor_2, campo_n= valor_n)
  * Ejemplo: art = Articulos.objects.create(nombre='taladro',seccion='herramientas', precio = 100)
* Update: nom_var = campo_n = new_value
  * Ejemplo: art.precio = 85
* Delete:
  * nom_var = Nom_Object.get(id = num_id)
  * nom_var.delete()
  * Ejemplo:
    * art2 = Articulos.get(id = 4)
    * art2.delete() 
* Read (Select): nom_var = Nom_Object.objects.all()
  * lista_articulos = Articulos.objects.all()

## IMPORTANTE
Para ejecutar es necesario crear la base de datos de forma local con postgreSQL

### script
CREATE DATABASE "bdAlmacen"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LOCALE_PROVIDER = 'libc'
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

## Integrantes
* OscarMDC
* FcoAlejandroG
* JoelQuijada
