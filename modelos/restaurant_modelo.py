from app import app, db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,ForeignKey,Integer,Table
from sqlalchemy.orm import declarative_base,relationship


# defino las tablas
# RESTAURANTES
class Restaurant(db.Model):  # la clase Restaurant hereda de db.Model de SQLAlquemy, es una clase base
    # utilizada en Flask para definir modelos que representan tablas en una base de datos.  
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    name=db.Column(db.String(100))
    logo=db.Column(db.String(255))
    website=db.Column(db.String(255))
    foto=db.Column(db.String(255))
    direccion=db.Column(db.String(255))
    barrio=db.Column(db.String(50))
    cocina=db.Column(db.JSON) # Tabla
    horario=db.Column(db.String(100))
    precio = db.Column(db.String(20))
    latitud = db.Column(db.Float(precision=8))
    longitud = db.Column(db.Float(precision=8))
    capacidad=db.Column(db.Integer)

    #crea el constructor de la clase
    def __init__(self, name, logo=None, website=None, foto=None, direccion=None, barrio=None, cocina=None, horario=None, precio=None, latitud=None, longitud=None, capacidad=None):
        # no hace falta el id porque lo crea sola mysql por ser auto_incremental
        self.name = name
        self.logo = logo
        self.website = website
        self.foto = foto
        self.direccion = direccion
        self.barrio = barrio
        self.cocina = cocina
        self.horario = horario
        self.precio = precio
        self.latitud = latitud
        self.longitud = longitud
        self.capacidad = capacidad


with app.app_context():  # Entra en el contexto de la aplicación Flask para poder realizar operaciones de configuración
    # y base de datos que requieren acceso a la aplicación.
    db.create_all()  # aqui crea todas las tablas si es que no estan creadas


