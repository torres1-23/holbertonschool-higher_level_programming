#!/usr/bin/python3

"""This module lists the first row of the table states from the database
hbtn_0e_6_usa using module SQLAlchemy.

Usage:
    Should take 3 arguments: 'mysql username', 'mysql password' and
    'database name' and list the first row of states table.
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
    state = session.query(State).first()
    if state:
        print('{}: {}'.format(state.id, state.name))
    else:
        print('Nothing')
