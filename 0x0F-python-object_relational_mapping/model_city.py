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
