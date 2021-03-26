#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_city = State(name='California', cities=[City(name='San Francisco')])
    session.add(new_city)
    session.commit()
