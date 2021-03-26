#!/usr/bin/python3

"""This module defines a State class that inherits from Base class from module
SQLAlchemy.

Usage:
    Creates an instance of Base class from SQLAlchemy and then create State
    class that represents an instance of a state in a SQL table.
"""
from sqlalchemy import ForeignKey, Column, Integer, String
from relationship_state import Base


class City(Base):
    """Represents an instance of State class.

    Attributes:
        __tablename__ (str): Name of the table.
        id (sqlalchemy.Integer): id of city.
        name (sqlalchemy.String): name of state.
        state_id (sqlalchemy.Integer): foreign key to states.id.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
