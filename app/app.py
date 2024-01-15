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

class HeroID(Resource):
   def get(self,id):
      hero_one=Hero.query.filter_by(id=id).first()
      if hero_one is None:
         return make_response(jsonify({ "error": "Hero not found"}),404)
      else:
          #getting the powers for that hero
          hero_details = {
              'id': hero_one.id,
              'name': hero_one.name,
              'super_name': hero_one.super_name,
              'powers': []
          }

          for hero_power in hero_one.hero_powers:
             power_info = {
                'id': hero_power.power.id,
                'name': hero_power.power.name,
                'description': hero_power.power.description
             }
             hero_details['powers'].append(power_info)

          return make_response(jsonify(hero_details), 200)
      
      class PowerResource(Resource):
 def get(self):
      powers=Power.query.all()
      powers_list=[{'id':power.id,'name':power.name,'description':power.description} for power in powers]

      return make_response(jsonify(powers_list),200)

#power by id
class PowerID(Resource):
   def get(self,id):
      power_one=Power.query.filter_by(id=id).first()

      if power_one is None:
         return make_response(jsonify({"error": "Power not found"}),404)
      else:
         power_details=[{'id':power_one.id,'name':power_one.name,'description':power_one.description}]
         return make_response(jsonify(power_details),200)
