from flask import jsonify,request
from app import app,db,ma

from modelos.restaurant_modelo import *

class RestaurantSchema(ma.Schema):
    class Meta:
        fields=('id','name','logo','website','foto','direccion','barrio','cocina','horario','precio','latitud','longitud','capacidad')

restaurant_schema=RestaurantSchema()  # El objeto restaurant_schema es para traer un restaurante
restaurantes_schema=RestaurantSchema(many=True)  # El objeto restaurantes_schema es para traer multiples registros de restaurantes


'''
=======================================================================================================================================
'''
# crea los Apis o rutas (json) => define una ruta o endpoint en una aplicación Flask para proporcionar una API JSON
# que devuelve todos los restaurantes almacenados en la base de datos.


# crea los endpoint o rutas (json)
@app.route('/restaurantes',methods=['GET'])
def get_Restaurantes():
    all_restaurantes=Restaurant.query.all() # el metodo query.all() lo hereda de db.Model
    result=restaurantes_schema.dump(all_restaurantes)  #el metodo dump() lo hereda de ma.schema y
                                                 # trae todos los registros de la tabla
    return jsonify(result)     # retorna un JSON de todos los registros de la tabla


@app.route('/restaurantes/<id>',methods=['GET'])
def get_restaurant(id):
    restaurant=Restaurant.query.get(id)
    return restaurant_schema.jsonify(restaurant)   # retorna el JSON de un restaurante recibido como parametro

@app.route('/restaurantes/<id>',methods=['DELETE'])
def delete_restaurant(id):
    restaurant=Restaurant.query.get(id)
    db.session.delete(restaurant)
    db.session.commit()                     # confirma el delete
    return restaurant_schema.jsonify(restaurant) # me devuelve un json con el registro eliminado

@app.route('/restaurantes', methods=['POST']) # crea ruta o endpoint
def create_restaurant():
    #print(request.json)  # request.json contiene el json que envio el cliente
    name=request.json['name']
    logo=request.json['logo']
    website=request.json['website']
    foto=request.json['foto']
    direccion=request.json['direccion']
    barrio=request.json['barrio']
    cocina=request.json['cocina']
    horario=request.json['horario']
    precio=request.json['precio']
    latitud=request.json['latitud']
    longitud=request.json['longitud']
    capacidad=request.json['capacidad']
    new_restaurant=Restaurant(name,logo,website,foto,direccion,barrio,cocina,horario,precio,latitud,longitud,capacidad)
    db.session.add(new_restaurant)
    db.session.commit() # confirma el alta
    return restaurant_schema.jsonify(new_restaurant)

@app.route('/restaurantes/<id>' ,methods=['PUT'])
def update_restaurant(id):
    restaurant=Restaurant.query.get(id)
 
    restaurant.name=request.json['name']
    restaurant.logo=request.json['logo']
    restaurant.website=request.json['website']
    restaurant.foto=request.json['foto']
    restaurant.direccion=request.json['direccion']
    restaurant.barrio=request.json['barrio']
    restaurant.cocina=request.json['cocina']
    restaurant.horario=request.json['horario']
    restaurant.precio=request.json['precio']
    restaurant.latitud=request.json['latitud']
    restaurant.longitud=request.json['longitud']
    restaurant.capacidad=request.json['capacidad']

    db.session.commit()    # confirma el cambio
    return restaurant_schema.jsonify(restaurant)    # y retorna un json con el restaurante


@app.route('/')
def bienvenida():
    return "Bienvenidos al backend"   # retorna el JSON recibido como parametro
