#!/usr/bin/python3

"""This module defines a State class that inherits from Base class from module
SQLAlchemy.

Usage:
    Creates an instance of Base class from SQLAlchemy and then create State
    class that represents an instance of a state in a SQL table.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Represents an instance of State class.

    Attributes:
        __tablename__ (str): Name of the table.
        id (sqlalchemy.Integer): id of state.
        name (sqlalchemy.String): name of state.
        cities (sqlalchemy.orm.relationship): Relation between State-City.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')
