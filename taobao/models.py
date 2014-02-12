#-*-coding:utf-8-*- 
#from peewee import *
from sqlalchemy import *
from sqlalchemy import create_engine,Column
from sqlalchemy.types import Integer,String,BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
import settings

DeclarativeBase = declarative_base()
def create_deals_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))

#########################Seller#######################################
class SellerAttribute():
#   One Seller may appear on different pages.
    sellerId = Column(BigInteger,primary_key=True)
    addedDate = Column(Date,primary_key=True)

class Seller(SellerAttribute,DeclarativeBase):
    __tablename__ = 'Seller'
    name = Column('name', String)

class ReputScore(SellerAttribute,DeclarativeBase):
    __tablename__ = 'ReputScore'
    reputScore = Column('reputScore',BigInteger)

class PositiveFeedbackRate(SellerAttribute,DeclarativeBase):
    __tablename__ = 'PositiveFeedbackRate'
    positiveFeedbackRate = Column('positiveFeedbackRate',Float)

class TrueDesc(SellerAttribute,DeclarativeBase):
#    trueDesc = FloatField()
    __tablename__ = 'TrueDesc'

    trueDesc = Column('trueDesc',Float)

class ServAttitude(SellerAttribute,DeclarativeBase):
    __tablename__ = 'ServAttitude'
    servAttitude = Column('servAttitude',Float)

class DeliSpeed(SellerAttribute,DeclarativeBase):
    __tablename__ = 'DeliSpeed'
    deliSpeed = Column('deliSpeed',Float)

###########################Commodity#############################
class CommodityAttribute():
#   One Commodity may appear on different pages.
    commId = Column(BigInteger,primary_key=True)
    addedDate = Column(Date,primary_key=True)

class Commodity(CommodityAttribute,DeclarativeBase):
    __tablename__ = 'Commodity'
    sellerId = Column('sellerId',BigInteger)
    title = Column('title', String)

class Turnover(CommodityAttribute,DeclarativeBase):
    __tablename__ = 'Turnover'
    turnover = Column('turnover',Integer)

class RateNumber(CommodityAttribute,DeclarativeBase):
    __tablename__ = 'RateNumber'
    rateNumber = Column('rateNumber',Integer)

class Price(CommodityAttribute,DeclarativeBase):
    __tablename__ = 'Price'
    price = Column('price',Float)



