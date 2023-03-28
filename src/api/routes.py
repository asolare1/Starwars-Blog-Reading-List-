"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, People, Planets, Favorites
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)



@api.route('/users', methods=['GET'])
def handle_user():  
    store_user = User.query.all()
    store_user = [user.serialize() for user in store_user]

    return jsonify(users = store_user)


@api.route('/users/<int:id>', methods=['GET'])
def getsingleuser(id):  
    store_user = User.query.filter_by(id=id).first()

    return jsonify(user = store_user.serialize())


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200



@api.route('/people', methods=['GET'])
def get_people():
    people = People.query.all()
    if people is None:
        return jsonify(msg="This page does not exist."), 400
    else:
        return jsonify(
        people=[person.serialize() for person in people]), 200

@api.route('/people/<int:id>', methods=['GET'])
def get_person(id):
    person = People.query.filter(
        People.id == id
    ).one_or_none()
    if person is None:
        return jsonify(msg="This person does not exist."), 400
    else:
        return jsonify(
        data=person.serialize()
        ), 200

@api.route('/planets', methods=['GET'])
def handle_planet():  
    store_planets = Planets.query.all()
    store_planets = [planets.serialize() for planets in store_planets]

    return jsonify(planets = store_planets)

@api.route('/planets/<int:id>', methods=['GET'])
def getsingleplanet(id):  
    store_planets = Planets.query.filter_by(id=id).first()

    return jsonify(planets = store_planets.serialize())

@api.route('users/favorites', methods=['GET'])
def handle_favorites():  
    store_favorites = Favorites.query.all()
    store_favorites = [favorites.serialize() for favorites in store_favorites]

    return jsonify(favorites = store_favorites)

@api.route('/favorites/planet/<int:planet_id>', methods=['POST'])
def add_new_favoriteplanet():
    request_body = request.get_json(force=True)
    favorite_planets = request_body
    
    return jsonify(favorite_planets) 

@api.route('/favorites/people/<int:people_id>', methods=['POST'])
def add_new_favoritepeople():
    request_body = request.get_json(force=True)
    favorite_people = request_body
    
    return jsonify(favorite_people) 
   
@api.route('/favorites/planets/<int:position>', methods=['DELETE'])
def delete_favoriteplanet(position):
    del favorites[planet.id]
    print("This is the planet to delete: ",position)

    return jsonify(favorites)

@api.route('/favorites/people/<int:position>', methods=['DELETE'])
def delete_favoritepeople(position):
    del favorites[people.id]
    print("This is the people to delete: ",position)

    return jsonify(favorites)
