from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'hero'

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String,nullable=False)
    super_name=db.Column(db.String)
    created_at=db.Column(db.DateTime,server_default=db.func.now())
    updated_at=db.Column(db.DateTime,onupdate=db.func.now())

    hero_powers = db.relationship('HeroPowers', back_populates='hero')

   
    def __repr__(self):
        return f'<Hero {self.name} {self.super_name}>'
    