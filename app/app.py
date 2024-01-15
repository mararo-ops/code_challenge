from flask import Flask, make_response,jsonify,request
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api,Resource

from models import db, Hero,HeroPowers,Power
CORS(app)
migrate = Migrate(app, db)

db.init_app(app)
api = Api(app)

class HeroResource(Resource):
    def get(self):
      #getting the heroes
      heros=Hero.query.all()

      heroes_list = [{'id': hero.id, 'name': hero.name, 'super_name': hero.super_name} for hero in heros]
      return make_response(jsonify(heroes_list),200)
