'''
Flask => es un microframework de Python para crear aplicaciones web.
jsonify => convierte datos a formato JSON para las respuestas HTTP.
request => maneja los datos de las solicitudes HTTP entrantes.
CORS (Cross-Origin Resource Sharing) => es una extensión que permite solicitudes
desde diferentes dominios, facilitando la comunicación entre frontend y backend.
SQLAlchemy => es una herramienta de ORM (Object-Relational Mapping) que permite
interactuar con bases de datos de forma más sencilla y con código más limpio.
Marshmallow => es una biblioteca para serializar y deserializar datos, 
facilitando la validación y conversión de objetos Python a y desde formatos como JSON.
'''

from flask import Flask ,jsonify ,request
# del modulo flask importar la clase Flask y los métodos jsonify,request
from flask_cors import CORS # del modulo flask_cors importar CORS
from flask_sqlalchemy import SQLAlchemy # del modulo flask_sqlalchemy importar SQLAlchemy
from flask_marshmallow import Marshmallow # del modulo flask_marshmallow importar Marshmallow
app=Flask(__name__)  # crear el objeto app de la clase Flask
CORS(app) #modulo cors es para que me permita acceder desde el frontend al backend

'''
=======================================================================================================================================
'''
# configuro la base de datos, con el nombre el usuario y la clave
# app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/restoradar' Usando MySQL local
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://user1261:clave1261@user1261.mysql.pythonanywhere-services.com/user1261$default'
# URI de la BBDD                          driver de la BD  user:clave@URLBBDD/nombreBBDD
# Configura la URI de la base de datos, indicando el tipo de base de datos (MySQL),
# el driver (pymysql), el usuario (root), la contraseña (root), la dirección del servidor (localhost)
# y el nombre de la base de datos (proyecto).
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #none Desactiva el seguimiento de modificaciones de objetos, lo que ahorra memoria.
db= SQLAlchemy(app)   #crea el objeto db de la clase SQLAlquemy que se usará para interactuar con la base de datos.
ma=Marshmallow(app)   #crea el objeto ma de de la clase Marshmallow que se usará para la serialización y deserialización de datos.


from controladores.restaurant_controlador import *

'''
=======================================================================================================================================
'''
# programa principal
if __name__=='__main__':  # Verifica si el script se está ejecutando directamente (es decir, no está siendo importado como un módulo en otro script
    app.run(debug=True, port=5000)   # Inicia el servidor Flask en el entorno local

# debug=True: Habilita el modo de depuración, lo que facilita la identificación y solución de problemas en el código Flask.
# port=5000: Especifica el puerto en el que el servidor Flask escuchará las solicitudes entrantes. 
# En este caso, el puerto 5000 es comúnmente utilizado para aplicaciones Flask en entornos de desarrollo.

