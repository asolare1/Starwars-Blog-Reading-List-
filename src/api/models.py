from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorites = db.relationship("Favorites", backref="user", lazy=True)
    
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
    favorites = db.relationship("Favorites", backref="people", lazy=True)
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
    favorites = db.relationship("Favorites", backref="planets", lazy=True)
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
    id = db.Column(db.Integer,unique=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    planets_id = db.Column(db.Integer, db.ForeignKey("planets.id"))
    people_id = db.Column(db.Integer, db.ForeignKey("people.id"))
    planet_name = db.Column(db.String(256))
    People_name = db.Column(db.String(256))

    def serialize(self):
        return {
            "user_id": self.user_id,
            "planet_name": self.planets_name,
            "people_name": self.people_name
        }
