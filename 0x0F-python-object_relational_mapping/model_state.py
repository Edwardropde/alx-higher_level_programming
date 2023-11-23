#!/usr/bin/python3
"""
Defines state model
Inherits from SQLAlchemy Base. Links to MySQL table states
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Reps state for MYSQL database

    Arguments:
        __tablename__ (str): MYSQL table name to store states
        id (sqlalchemy.Integer): state's id
        name (sqlalchemy.String): state's name
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
