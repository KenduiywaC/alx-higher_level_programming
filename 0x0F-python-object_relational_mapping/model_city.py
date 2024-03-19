#!/usr/bin/python3
#Represents a City model
#Inherits from SQLAlchemy Base and links to the MySQL table cities

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):
"""
Represents a city for a MySQL database.

Attributes:
__tablename__ (str): Name of the MySQL table to store Cities.
id (sqlalchemy.Integer): City's id.
name (sqlalchemy.String): City's name.
state_id (sqlalchemy.Integer): City's state id.
"""
__tablename__ = "cities"

id = Column(Integer, primary_key=True)
name = Column(String(128), nullable=False)
state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

def my_function():
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
print(my_function.__doc__)  # Function docstring
print(MyClass.my_function.__doc__)  # Function docstring
