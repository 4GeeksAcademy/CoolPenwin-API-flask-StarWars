"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Starships, Characters,Films, Liked,films_characters
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/users', methods=['GET'])
def get_users():
    all_users = User.query.all()
    results = list(map(lambda user: user.serialize(), all_users))

    return jsonify(results), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()

    return jsonify(user.serialize()), 200



@app.route('/characters', methods=['GET'])
def get_characters():
    all_characters = Characters.query.all()
    results = list(map(lambda character: character.serialize(), all_characters))

    return jsonify(results), 200

@app.route('/characters/<int:character_id>', methods=['GET'])
def get_character(character_id):
    character = Characters.query.filter_by(id=character_id).first()

    return jsonify(character.serialize()), 200


@app.route('/starships', methods=['GET'])
def get_starships():
    all_starships = Starships.query.all()
    results = list(map(lambda starship: starship.serialize(), all_starships))

    return jsonify(results), 200

@app.route('/starships/<int:starship_id>', methods=['GET'])
def get_starship(starship_id):
    starship = Starships.query.filter_by(id=starship_id).first()

    return jsonify(starship.serialize()), 200

@app.route('/species', methods=['GET'])
def get_species():
    all_species = Species.query.all()
    results = list(map(lambda specie: specie.serialize(), all_species))

    return jsonify(results), 200

@app.route('/species/<int:specie_id>', methods=['GET'])
def get_specie(specie_id):
    specie = Species.query.filter_by(id=specie_id).first()

    return jsonify(specie.serialize()), 200


@app.route('/films', methods=['GET'])
def get_films():
    all_films = Films.query.all()
    results = list(map(lambda film: film.serialize(), all_films))

    return jsonify(results), 200

@app.route('/films/<int:film_id>', methods=['GET'])
def get_film(film_id):
    film = Films.query.filter_by(id=film_id).first()

    return jsonify(film.serialize()), 200


@app.route('/likeds', methods=['GET'])
def get_likeds():
    all_likeds = Liked.query.all()
    results = list(map(lambda liked: liked.serialize(), all_likeds))

    return jsonify(results), 200

@app.route('/likeds/<int:liked_id>', methods=['GET'])
def get_liked(liked_id):
    liked = Liked.query.filter_by(id=liked_id).first()

    return jsonify(liked.serialize()), 200



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
