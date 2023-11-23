#!/usr/bin/python3
"""
Lists city objects from the hbtn_0e_101_usa database
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
    query = session.query(City).order_by(City.id)
    for city in query.all():
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.close()
