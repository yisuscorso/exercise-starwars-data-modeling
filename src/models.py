import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table character.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)


class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table planet
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    User_id= Column(String(250), nullable=False)

    

   
    def to_dict(self):
        return {}

class FavoriteCharacters(Base):
    __tablename__ = 'favorite_characters'
   
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_id= Column(String(250),ForeignKey('character.id'), nullable=False)
    character = relationship(User)
    user_id= Column(String(250),ForeignKey('user.id'), nullable=False)
    user = relationship(User)

class FavoritePlanets(Base):
    __tablename__ = 'favorite_planets'
    
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_id= Column(String(250),ForeignKey('planet.id'), nullable=False)
    planet = relationship(User)
    user_id= Column(String(250),ForeignKey('user.id'), nullable=False)
    user = relationship(User)
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')