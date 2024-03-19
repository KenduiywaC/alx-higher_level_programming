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
