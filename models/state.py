#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from datetime import datetime
from models.base_model import BaseModel, Base
import models
from models.city import City
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='states', cascade='delete')
    if getenv('HBNB_TYPE_STORAGE') != 'db':
       @property
       def cities(self):
            rel_cities = []
            for i in list(models.storage.all(City).values()):
                if i.id == self.id:
                    rel_cities.append(i)
            return rel_cities
