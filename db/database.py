from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///data.sqlite')
session = scoped_session(sessionmaker(bind=engine))

class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)

class Poem(Base):
    __tablename__ = 'Poems'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    name = Column(String)
    text = Column(String)
    date = Column(String)
