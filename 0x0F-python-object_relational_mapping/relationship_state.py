#!/usr/bin/python3
#Represents States model
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
"""Represents a state for a MySQL database.

Attributes:
__tablename__ (str): The name of the MySQL table to store States.
id (sqlalchemy.Integer): The state's id.
name (sqlalchemy.String): The state's name.
cities (sqlalchemy.orm.relationship): The State-City relationship.
"""
__tablename__ = "states"
id = Column(Integer, primary_key=True)
name = Column(String(128), nullable=False)

cities = relationship("City", back_populates="state", cascade="all, delete")

class City(Base):
"""Represents a city for a MySQL database.

Attributes:
__tablename__ (str): The name of the MySQL table to store Cities.
id (sqlalchemy.Integer): The city's id.
name (sqlalchemy.String): The city's name.
state_id (sqlalchemy.Integer): The id of the state this city belongs to.
"""
__tablename__ = "cities"
id = Column(Integer, primary_key=True)
name = Column(String(128), nullable=False)
state_id = Column(Integer, ForeignKey('states.id'))

state = relationship("State", back_populates="cities")

def my_function():
"""This is a standalone function."""
pass

class MyClass:
"""This is a class with a function."""

def my_function(self):
"""This is a function inside MyClass."""
pass

if __name__ == "__main__":
print(__doc__)  # Module docstring
print(State.__doc__)  # State class docstring
print(City.__doc__)  # City class docstring
print(State.__tablename__)  # State attribute docstring
print(State.id.__doc__)  # State attribute docstring
print(State.name.__doc__)  # State attribute docstring
print(State.cities.__doc__)  # State attribute docstring
print(City.__tablename__)  # City attribute docstring
print(City.id.__doc__)  # City attribute docstring
print(City.name.__doc__)  # City attribute docstring
print(City.state_id.__doc__)  # City attribute docstring
print(City.state.__doc__)  # City attribute docstring
print(my_function.__doc__)  # Function docstring
print(MyClass.my_function.__doc__)  # Function docstring
