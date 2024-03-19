#!/usr/bin/python3
#Represents a city model
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):
"""Represents a city for a MySQL database.

Attributes:
__tablename__ (str): The name of the MySQL table to store Cities.
id (sqlalchemy.Integer): The city's id.
name (sqlalchemy.String): The city's name.
state_id (sqlalchemy.Integer): The id of the state this city belongs to.
state (sqlalchemy.orm.relationship): The City-State relationship.
"""
__tablename__ = "cities"
id = Column(Integer, primary_key=True)
name = Column(String(128), nullable=False)
state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

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
print(City.__doc__)  # Class docstring
print(City.__tablename__)  # Attribute docstring
print(City.id.__doc__)  # Attribute docstring
print(City.name.__doc__)  # Attribute docstring
print(City.state_id.__doc__)  # Attribute docstring
print(City.state.__doc__)  # Attribute docstring
print(my_function.__doc__)  # Function docstring
print(MyClass.my_function.__doc__)  # Function docstring
