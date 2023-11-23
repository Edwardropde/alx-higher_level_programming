#!/usr/bin/python3
"""
Defines state model
Inherits from SQLAlchemy Base. Links to MySQL table states
"""
import sys
from sqlalchemy import Column, Integer, String, create_engine
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
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
