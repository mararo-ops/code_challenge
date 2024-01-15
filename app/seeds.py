from random import randint,choice as rc
import random
from faker import Faker

from app import app
from models import db,Power,Hero,HeroPowers

fake=Faker()

with app.app_context():
    #clearing the existing data
    HeroPowers.query.delete()
    Hero.query.delete()
    Power.query.delete()

#seeding hero
    heros=[] #empty list to store the heros
    for i in range(10):
        b=Hero(name=fake.name(),
                     super_name=fake.name())
        heros.append(b)
    
    db.session.add_all(heros)
    db.session.commit()
    