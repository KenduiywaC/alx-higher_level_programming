#!/usr/bin/python3
#Lists all states from the database hbtn_0e_0_usa

import MySQLdb
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from MySQLdb import State, Base

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
        session.close()
