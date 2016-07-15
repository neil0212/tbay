from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://action:action@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from tbay import User, Item, Bid, session

'''beyonce = User()
beyonce.username = "bknowles"
beyonce.password = "uhohuhohuhohohnana"'''
beyonce = User(username="bknowles", password="uhohuhohuhohohnana")
session.add(beyonce)
session.commit()

'''neil = User()
beyonce.username = "neil"
beyonce.password = "q123611"
session.add(neil)
session.commit()


apple = Item()
apple.name = "ape"
apple.description = "fruit"
session.add(apple)
session.commit()


banana = Item()
banana.name = "bna"
apple.description = "fruit"
session.add(banana)
session.commit()'''

Base.metadata.create_all(engine)