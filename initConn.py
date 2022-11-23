from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#THIS FILE CREATES A WHOLE NEW TABLE, is then called for its connection

engine = create_engine('postgresql://admin:password@127.0.0.1:5433/Flask', echo=True)
base = declarative_base()

class bank(base):

    __tablename__ = "bank"

    ID = Column(Integer, primary_key=True)
    name = Column(String),
    moneys = Column(Float)

base.metadata.create_all(engine)