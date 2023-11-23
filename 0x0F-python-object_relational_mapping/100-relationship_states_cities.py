#!/usr/bin/python3
"""
Creates the State 'California' with the City 'San Francisco'
from hbtn_0e_100_usa database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City
from sys import argv

if __name__ == "__main__":
    username, password, database = argv[1], argv[2], argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)
    new_state.cities.append(new_city)
    session.add(new_state)
    session.commit()
    session.close()
