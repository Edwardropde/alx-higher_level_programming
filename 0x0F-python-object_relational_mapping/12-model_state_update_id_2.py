#!/usr/bin/python3
"""
Changes name of state object with id = 2 to New Mexico
in the hbtn_0e_6_usa database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter_by(id=2).first()
    if state is not None:
        state.name = "New Mexico"
        session.commit()
    session.close()
