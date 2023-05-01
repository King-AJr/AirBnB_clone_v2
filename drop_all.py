#!/usr/bin/python3
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
HBNB_ENV = getenv('HBNB_ENV')
HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
connection_string = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_DB)
engine = create_engine(connection_string)

Base.metadata.drop_all(bind=engine)
metadata.drop_all()

