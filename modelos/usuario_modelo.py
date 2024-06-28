from app import app, db
from sqlalchemy import Column,ForeignKey,Integer,Table
from sqlalchemy.orm import declarative_base,relationship


''' # USUARIOS
class Usuario(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    usuario=db.Column(db.String(30))
    nombre=db.Column(db.String(100))
    rol=db.Column(db.Integer)
    foto=db.Column(db.String(400))
    

    def __init__(self,usuario,nombre,rol,foto):
        self.usuario=usuario
        self.nombre=nombre
        self.rol=rol
        self.foto=foto
        
''' 

with app.app_context():  # Entra en el contexto de la aplicación Flask para poder realizar operaciones de configuración
    # y base de datos que requieren acceso a la aplicación.
    db.create_all()  # aqui crea todas las tablas si es que no estan creadas