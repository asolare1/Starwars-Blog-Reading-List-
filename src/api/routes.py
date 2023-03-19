"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/users', methods=['GET'])
def handle_user():  
    store_user = User.query.all()
    store_user = [user.serialize() for user in store_user]

    return jsonify(users = store_user)


@api.route('/users/<int:id>', methods=['GET'])
def getsingleuser(id):  
    store_user = User.query.filter_by(id=id).first()

    return jsonify(user = store_user.serialize())


@api.route('/people', methods=['GET'])
def handle_people():  
    store_people = People.query.all()
    store_people = [people.serialize() for people in store_people]

    return jsonify(people = store_people)

@api.route('/people/<int:id>', methods=['GET'])
def getsinglepeople(id):  
    store_people = People.query.filter_by(id=id).first()

    return jsonify(people = store_people.serialize())

@api.route('/planets', methods=['GET'])
def handle_planet():  
    store_planet = Planet.query.all()
    store_planet = [planet.serialize() for planet in store_planet]

    return jsonify(planets = store_planet)

@api.route('/planets/<int:id>', methods=['GET'])
def getsingleplanet(id):  
    store_planet = Planet.query.filter_by(id=id).first()

    return jsonify(planet = store_planet.serialize())