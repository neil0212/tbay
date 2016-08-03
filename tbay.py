from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    items=relationship('Item',backref='owner')
    bids=relationship('Bid',backref='bidder')


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    user_id=Column(Integer,ForeignKey('user.id'),nullable=False)
    bids=relationship('Bid',backref='item')


class Bid(Base):
    __tablename__ = "bid"

    id = Column(Integer, primary_key=True)
    price = Column(String, nullable=False)
    user_id=Column(Integer,ForeignKey('user.id'),nullable=False)
    item_id=Column(Integer,ForeignKey('item.id'),nullable=False)


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


#user DB
joe = User(username='joe', password='joe')
apple = User(username='apple', password='apple')
genie = User(username='genie', password='genie')

baseball = Item(name='baseball',description='baseball sport',owner=joe)


apple_bid = Bid(price=10000, item=baseball, bidder=apple)
genie_bid = Bid(price=10007, item=baseball, bidder=genie)



session.add_all([joe,apple, genie,baseball,apple_bid, genie_bid])
session.commit()

row = session.query(User.username, Item.name, Bid.price).join(Bid).order_by(Bid.price).all()
highest_bidder = row[-1].username
print(row)
print(highest_bidder)




