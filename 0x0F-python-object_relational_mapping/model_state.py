#!/usr/bin/python3
#Represents a State model
#Inherits from SQLAlchemy Base and links to the MySQL table states

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
"""
Represents a state for a MySQL database.

Attributes:
__tablename__ (str): Name of the MySQL table to store States.
id (sqlalchemy.Integer): State's id.
name (sqlalchemy.String): State's name.
"""
__tablename__ = "states"

id = Column(Integer, primary_key=True)
name = Column(String(128), nullable=False)

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
print(State.__doc__)  # Class docstring
print(State.__tablename__)  # Attribute docstring
print(State.id.__doc__)  # Attribute docstring
print(State.name.__doc__)  # Attribute docstring
print(my_function.__doc__)  # Function docstring
print(MyClass.my_function.__doc__)  # Function docstring
