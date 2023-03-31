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
def get_favorites(user_id):
    favorites = Favorites.query.filter_by(user_id = user_id)
    favorites_dictionary = []
    for favorite in favorites:
        favorites_dictionary.append(favorite.serialize())
    return jsonify(favorites_dictionary), 200

@api.route('favorites/people/<int:user_id>/<int:character_id>', methods=['POST'])
def add_poeple_to_favorites(people_id, user_id):

    new_favorite_data = request.json
    favorites = Favorites.query.filter_by(user_id = user_id, people_id = people_id).first()
    if favorites is not None:
        return jsonify({"message": "The person is already in favorites."}), 401
    else:
        try:
            new_favorite = Favorites.create_favorite(user_id = user_id, people_id = people_id, **new_favorite_data)
            return jsonify(new_favorite.serialize()), 201

@api.route('favorite/poeple/<int:user_id>/<int:character_id>', methods=['DELETE'])  
def delete_people_from_favorites(people_id, user_id):
    favorite_to_delete = Favorites.query.filter_by(user_id = user_id, people_id = people_id).first()
    try:
        delete_poep = Favorites.delete_favorite(favorite_to_delete)
        return jsonify(delete_peop), 200
    
@api.route('favorite/planets/<int:user_id>/<int:planet_id>', methods=['POST'])
def add_planet_to_favorites(planet_id, user_id):

    new_favorite_data = request.json
    favorites = Favorites.query.filter_by(user_id = user_id, planet_id = planet_id).first()
    if favorites is not None:
        return jsonify({"message": "The planet is already in favorites."}), 401
    else:
        try:
            new_favorite = Favorite.create_favorite(user_id = user_id, planet_id = planet_id, **new_favorite_data)
            return jsonify(new_favorite.serialize()), 201

@api.route('favorite/planets/<int:user_id>/<int:planet_id>', methods=['DELETE'])  
def delete_planet_from_favorites(planet_id, user_id):
    favorite_to_delete = Favorites.query.filter_by(user_id = user_id, planet_id = planet_id).first()
    try:
        delete_planet = Favorites.delete_favorite(favorite_to_delete)
        return jsonify(delete_planet), 200
    