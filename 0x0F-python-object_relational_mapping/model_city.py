#!/usr/bin/python3
"""
Defines city model
Inherits from SQLAlchemy Base links to MySQL table cities
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

Base = declarative_base()


class City(Base):
    """
    Reps city for MYSQL database

    Attributes:
        id (str): City id
        name (sqlalchemy.Integer): city name
        state_id (sqlalchemy.String): city state id
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
