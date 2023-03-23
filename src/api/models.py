from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }

class People(db.Model):
    __tablename__ = "people"
    name = db.Column(db.String(256))
    height = db.Column(db.Float)
    mass = db.Column(db.String(256))
    hair_color = db.Column(db.String(256))
    skin_color = db.Column(db.String(256))
    eye_color = db.Column(db.String(256))
    birth_year = db.Column(db.String(256))
    gender = db.Column(db.String(256))
    homeworld = db.Column(db.String(256))
    id = db.Column(db.Integer,unique=True, primary_key=True)


    def serialize(self):
        return {
            "name": self.name,
            "birth_year": self.birth_year,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "height": self.height,
            "mass": self.mass,
            "skin_color": self.skin_color,
            "homeworld": self.homeworld
        }
class Planets(db.Model):
    __tablename__ = "planets"
    name = db.Column(db.String(256))
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    diameter = db.Column(db.Integer)
    climate = db.Column(db.String(256))
    gravity = db.Column(db.Integer)
    terrain = db.Column(db.String(256))
    surface_water = db.Column(db.Integer)
    population = db.Column(db.Integer)
    id = db.Column(db.Integer,unique=True, primary_key=True)


    def serialize(self):
        return {
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "population": self.population,
        }

class Favorites(db.Model):
    __tablename__ = "favorites"
    planet_name = db.Column(db.String(256))
    people_name = db.Column(db.String(256))
    id = db.Column(db.Integer,unique=True, primary_key=True)


    def serialize(self):
        return {
            "planet_name": self.planets_name,
            "people_name": self.people_name,
        }