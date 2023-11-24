#!/usr/bin/python3
"""
Defines City model
Inherits from SQLAlchemy Base. Links to MYSQL table cities.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String
from model_state import Base

Base = declarative_base()


class City(Base):
    """
    Reps city for Mysql database

    Attributes:
        id (sqlalchemy.Column): The city's id.
        name (sqlalchemy.Column): The city's name.
        state_id (sqlalchemy.Column): The city's state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities", cascade="all, delete-orphan")
