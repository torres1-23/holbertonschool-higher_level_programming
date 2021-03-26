#!/usr/bin/python3

"""This module prints the State object with the name passed as argument from
the database hbtn_0e_6_usa using module SQLAlchemy.

Usage:
    Should take 4 arguments: 'mysql username', 'mysql password',
    'database name' and 'state name to search'and list all 'id' and containing
    an 'state name' passed as argument.
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == sys.argv[4]).first()
    if (state):
        print(state.id)
    else:
        print('Not found')
