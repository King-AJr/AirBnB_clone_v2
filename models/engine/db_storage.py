#!/usr/bin/python3
""" class in charge of db connection"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import scoped_session


class DBStorage:
   """ manages db storage of data""" 
   __engine = None
   __session = None

   def __init__(self):
      HBNB_ENV = getenv('HBNB_ENV')
      HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
      HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
      HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
      HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
      connection_string = 'mysql+mysqldb://{}:{}@{}/{}'.format(
HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB)
      self.__engine = create_engine(connection_string, pool_pre_ping=True)
      if HBNB_ENV == 'test':
         Base.metadata.drop_all(bind=self.__engine)
      Session = sessionmaker(bind=self.__engine)
      self.__session = Session()

    
   def all(self, cls=None):
    """ Query db for classes """
    objs = []
    if cls is None:
        tables = [State, City, User, Place, Review, Amenity]
        for table in tables:
            objs.extend(self.__session.query(table).all())
    else:
        if type(cls) == str:
            cls = eval(cls)
        objs = self.__session.query(cls).all()

    return {"{}.{}: {}".format(type(i).__name__, i.id, i) for i in objs}

    
   def new(self, obj):
      """add new object to session"""
      self.__session.add(obj)


   def save(self):
      """commit session"""
      self.__session.commit()


   def delete(self, obj=None):
      """ delete object from current session """
      if obj != None:
         self.__session.delete(obj)


   def reload(self):
      """reload session """
      Base.metadata.create_all(bind=self.__engine)
      session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
      Session = scoped_session(session_factory)
      self.__session = Session()
