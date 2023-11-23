#!/usr/bin/python3
"""
Lists state object with name passed as args from hbtn_0e_6_usa database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_name = sys.argv[4]
    state = session.query(State).filter_by(name=state_name).first()
    if state is not None:
        print(state.id)
    else:
        print("Not found")
    session.close()
