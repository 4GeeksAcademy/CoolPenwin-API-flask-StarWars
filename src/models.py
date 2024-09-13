# Importaciones
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Association Tables
films_characters = db.Table('films_characters', db.Model.metadata,
    db.Column('film_id', db.Integer, db.ForeignKey('films.id'), primary_key=True),
    db.Column('character_id', db.Integer, db.ForeignKey('characters.id'), primary_key=True)
)

films_planets = db.Table('films_planets', db.Model.metadata,
    db.Column('film_id', db.Integer, db.ForeignKey('films.id'), primary_key=True),
    db.Column('planet_id', db.Integer, db.ForeignKey('planets.id'), primary_key=True)
)

films_starships = db.Table('films_starships', db.Model.metadata,
    db.Column('film_id', db.Integer, db.ForeignKey('films.id'), primary_key=True),
    db.Column('starship_id', db.Integer, db.ForeignKey('starships.id'), primary_key=True)
)

films_species = db.Table('films_species', db.Model.metadata,
    db.Column('film_id', db.Integer, db.ForeignKey('films.id'), primary_key=True),
    db.Column('species_id', db.Integer, db.ForeignKey('species.id'), primary_key=True)
)

# Modelos
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    nick_name = db.Column(db.String(250), nullable=False, unique=True)
    first_name = db.Column(db.String(250), nullable=True)
    last_name = db.Column(db.String(250), nullable=True)
    liked_items = db.relationship("Liked", back_populates="user")

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Starships(db.Model):
    __tablename__ = 'starships'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    starship_class = db.Column(db.String(250))
    manufacturer = db.Column(db.String(250))
    cost_in_credits = db.Column(db.String(250))
    length = db.Column(db.String(250))
    crew = db.Column(db.String(250))
    passengers = db.Column(db.String(250))
    max_atmosphering_speed = db.Column(db.Integer)
    hyperdrive_rating = db.Column(db.String(250))
    MGLT = db.Column(db.String(250))
    cargo_capacity = db.Column(db.String(250))
    consumables = db.Column(db.String(250))
    pilots = db.Column(db.String(250))
    films = db.relationship("Films", secondary=films_starships, back_populates="starships")
    liked_items = db.relationship("Liked", back_populates="starship")

    def __repr__(self):
        return '<Starships %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "starship_class": self.starship_class,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "hyperdrive_rating": self.hyperdrive_rating,
            "MGLT": self.MGLT,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "pilots": self.pilots
        }

class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    height = db.Column(db.String(250))
    mass = db.Column(db.String(250))
    hair_color = db.Column(db.String(250))
    skin_color = db.Column(db.String(250))
    eye_color = db.Column(db.String(250))
    birth_year = db.Column(db.String(250))
    gender = db.Column(db.String(250))
    homeworld = db.Column(db.String(250))
    force_side = db.Column(db.String(250))
    films = db.relationship("Films", secondary=films_characters, back_populates="characters")
    liked_items = db.relationship("Liked", back_populates="character")

    def __repr__(self):
        return '<Characters %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "homeworld": self.homeworld,
            "force_side": self.force_side
        } 
    
class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    diameter = db.Column(db.Float)
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    gravity = db.Column(db.String(250))
    population = db.Column(db.Integer)
    climate = db.Column(db.String(250))
    terrain = db.Column(db.String(250))
    surface_water = db.Column(db.Integer)
    films = db.relationship("Films", secondary=films_planets, back_populates="planets")
    liked_items = db.relationship("Liked", back_populates="planet")
    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water
        }


class Species(db.Model):
    __tablename__ = 'species'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    classification = db.Column(db.String(250))
    designation = db.Column(db.String(250))
    average_height = db.Column(db.String(250))
    average_lifespan = db.Column(db.String(250))
    hair_colors = db.Column(db.String(250))
    skin_colors = db.Column(db.String(250))
    eye_colors = db.Column(db.String(250))
    homeworld = db.Column(db.String(250))
    language = db.Column(db.String(250))
    films = db.relationship("Films", secondary=films_species, back_populates="species")
    liked_items = db.relationship("Liked", back_populates="species")

    def __repr__(self):
        return '<Species %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "classification": self.classification,
            "designation": self.designation,
            "average_height": self.average_height,
            "average_lifespan": self.average_lifespan,
            "hair_colors": self.hair_colors,
            "skin_colors": self.skin_colors,
            "eye_colors": self.eye_colors,
            "homeworld": self.homeworld,
            "language": self.language
        }   

class Films(db.Model):
    __tablename__ = 'films'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    episode_num = db.Column(db.Integer)
    release_date = db.Column(db.Integer)
    director = db.Column(db.String(250))
    characters = db.relationship('Characters', secondary=films_characters, back_populates='films')
    planets = db.relationship('Planets', secondary=films_planets, back_populates='films')
    starships = db.relationship('Starships', secondary=films_starships, back_populates='films')
    species = db.relationship('Species', secondary=films_species, back_populates='films')

    def __repr__(self):
        return '<Films %r>' % self.title

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "episode_num": self.episode_num,
            "release_date": self.release_date,
            "director": self.director
        }

class Liked(db.Model):
    __tablename__ = 'liked'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    item_id = db.Column(db.Integer, primary_key=True)
    item_type = db.Column(db.String(50))  

    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    starship_id = db.Column(db.Integer, db.ForeignKey('starships.id'))
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'))

    user = db.relationship('User', back_populates="liked_items")
    character = db.relationship('Characters', back_populates="liked_items")
    planet = db.relationship('Planets', back_populates="liked_items")
    starship = db.relationship('Starships', back_populates="liked_items")
    species = db.relationship('Species', back_populates="liked_items")

    def __repr__(self):
        return '<Liked %r>' % self.item_id

    def serialize(self):
        return {
            "user_id": self.user_id,
            "item_id": self.item_id,
            "item_type": self.item_type,
            "character_id": self.character_id,
            "planet_id": self.planet_id,
            "starship_id": self.starship_id,
            "species_id": self.species_id
        }


# davinia ejjemplos


# homeworld_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
#     planets = db.relationship(Planets)

# vehicles_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
#     vehicles = db.relationship(Vehicles)




  




#  # ejemplo edo ----------
  
# class User(db.Model):
#     __tablename__ = "User"
#     id = db.Column(db.Integer, primary_key=True)
#     name =  db.Column(db.String(250), nullable=False)
#     email = db.Column(db.String(250), nullable=False)
    
#     character_fav = db.relationship("Character_fav", back_populates="user")
#     planet_fav = db.relationship("Planet_fav", back_populates="user")
#     starship_fav = db.relationship("Starship_fav", back_populates="user")


#     def __repr__(self):
#         return '<User %r>' % self.username

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }




# class Character(db.Model):
#     __tablename__ = "Character"
#     id = db.Column(db.Integer, primary_key=True)
#     name =  db.Column(db.String(250), nullable=False)
#     height = db.Column(db.Float, nullable=False)
#     mass = db.Column(db.Float, nullable=False)
#     hair_color = db.Column(db.String(250), nullable=False)
#     skin_color = db.Column(db.String(250), nullable=False)

#     character_fav = db.relationship("Character_fav", back_populates="character")

# class Character_fav(db.Model):
#     __tablename__ = "Character_fav"
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey("User.id"))
#     character_id = db.Column(db.Integer, db.ForeignKey("Character.id"))

#     user = db.relationship("User", back_populates="character_fav")
#     character = db.relationship("Character", back_populates="character_fav")

# ##-----FIN edo----