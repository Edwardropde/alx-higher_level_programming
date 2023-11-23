#!/usr/bin/python3
"""
Lists states and corresponding cities in the hbtn_0e_101_usa database
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
    query = session.query(State).order_by(State.id, City.id)
    for state in query.all():
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
    session.close()
