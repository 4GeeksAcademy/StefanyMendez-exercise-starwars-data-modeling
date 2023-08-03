import os
import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(250), nullable=False)
    fecha_subcription = Column(DateTime, default=datetime.datetime.utcnow)


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)
    climate = Column(String(100))
    gravity = Column(String(100))
    terrain = Column(String(100))
    surface_water = Column(Integer)
    population = Column(Integer)


class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    model = Column(String(100))
    manufacturer = Column(String(100))
    cost_in_credits = Column(Integer)
    length = Column(Float)
    max_atmosphering_speed = Column(Float)
    crew = Column(Float)
    passengers = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(100))
    vehicle_class = Column(String(100))

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    height = Column(Float)
    mass = Column(Float)
    hair_color = Column(String(100))
    skin_color = Column(String(100))
    eye_color = Column(String(100))
    birth_year = Column(String(100))
    gender = Column(String(100))
    id_homeworld = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)

class CharacterVehicle(Base):
    __tablename__ = 'character_vehicle'
    id_vehicle = Column(Integer, ForeignKey('vehicle.id'), primary_key=True)
    id_character = Column(Integer, ForeignKey('character.id'))
    vehicle = relationship(Vehicle)
    character = relationship(Character)

class CharacterFavorites(Base):
    __tablename__ = 'character_favorites'
    id_character = Column(Integer, ForeignKey(
        'character.id'), primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    character = relationship(Character)


class PlanetFavorites(Base):
    __tablename__ = 'planet_favorites'
    id_planet = Column(Integer, ForeignKey('planet.id'), primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    planet = relationship(Planet)


class VehicleFavorites(Base):
    __tablename__ = 'vehicle_favorites'
    id_vehicle = Column(Integer, ForeignKey('vehicle.id'), primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    planet = relationship(Vehicle)


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(100))
    url = Column(String(250))
    id_post = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    id_author = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    id_post = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)


class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    id_user_from = Column(Integer, ForeignKey('user.id'))
    id_user_to = Column(Integer, ForeignKey('user.id'))


def to_dict(self):
    return {}

# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
