#!/usr/bin/python3
"""
Defines state model
Inherits from SQLAlchemy Base. Links to MySQL table states.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from model_city import Base, City


class State(Base):
    """
    Reps state for MySQL database

    Attributes:
        __tablename__ (str): name of MYSQL table to store states
        id (sqlalchemy.Integer): State's id
        name (sqlalchemy.String): state's name.
        cities (sqlalchemy.orm.relationship): state-city relationship.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")
