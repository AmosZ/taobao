#-*-coding:utf-8-*- 
#from peewee import *
from sqlalchemy import *
from sqlalchemy import create_engine,Column
from sqlalchemy.types import Integer,String,BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
import settings
import datetime

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
class SellerAttribute(object):
#   One Seller may appear on different pages.
    sellerId = Column(BigInteger,primary_key=True)
    addedDate = Column(Date,primary_key=True)

class Seller(DeclarativeBase):
    __tablename__ = 'Seller'
    sellerId = Column(BigInteger,primary_key=True)
    name = Column('name', String)
    @staticmethod
    def getSellerURL(session,sellerId=0,date=datetime.date.today()):
        result = []
        if sellerId:
            result.append('http://rate.taobao.com/user-rate-'+ str(sellerId) +'.htm:')
        else:
            try:
                result = session.query(Seller.sellerId).\
                        filter(Seller.addedDate == date).all()
                for index,value in enumerate(result):
                    result[index] = 'http://rate.taobao.com/user-rate-'+ str(value[0]) +'.htm:'

            except NameError:
                print self.__class__.__name__ + 'session doesn\'t exist!'
        return result
class SellerDate(SellerAttribute,DeclarativeBase):
    __tablename__ = 'SellerDate'

class ReputScore(SellerAttribute,DeclarativeBase):
    __tablename__ = 'ReputScore'
    reputScore = Column('reputScore',BigInteger)


class PositiveFeedbackRate(SellerAttribute,DeclarativeBase):
    __tablename__ = 'PositiveFeedbackRate'
    positiveFeedbackRate = Column('positiveFeedbackRate',Float)

class TrueDesc(SellerAttribute,DeclarativeBase):
    __tablename__ = 'TrueDesc'

    trueDesc = Column('trueDesc',Float)

class ServAttitude(SellerAttribute,DeclarativeBase):
    __tablename__ = 'ServAttitude'
    servAttitude = Column('servAttitude',Float)

class DeliSpeed(SellerAttribute,DeclarativeBase):
    __tablename__ = 'DeliSpeed'
    deliSpeed = Column('deliSpeed',Float)

###########################Commodity#############################
class CommodityAttribute(object):
#   One Commodity may appear on different pages.
    commId = Column(BigInteger,primary_key=True)
    addedDate = Column(Date,primary_key=True)

class CommodityDate(CommodityAttribute,DeclarativeBase):
    __tablename__ = 'CommodityDate'
    @staticmethod
    def getAllCommodityIds(session,date=datetime.date.today()):
        # query return a list of tuple
        result =  session.query(CommodityDate.commId).filter(CommodityDate.addedDate == date).all()
        ret = []
        for i in result:
            ret.append(i[0])
        return ret


class Commodity(DeclarativeBase):
    __tablename__ = 'Commodity'
    sellerId = Column('sellerId',BigInteger)
    commId = Column(BigInteger,primary_key=True)
    title = Column('title', String)
    # We can get commodify's url but I can scrapy it because taobao block spider
    @staticmethod
    def getCommodityURL(session,commId=0,date=datetime.date.today()):
        result = []
        if commId:
            result.append("http://item.taobao.com/item.htm?id=" + str(commId))
        else:
            try:
                result = session.query(Commodity.commId).\
                        filter(Commodity.addedDate == date).all()
                for index,value in enumerate(result):
                    result[index] = "http://item.taobao.com/item.htm?id=" + str(value[0])

            except NameError:
                print self.__class__.__name__ + 'session doesn\'t exist!'
        return result

class Turnover(CommodityAttribute,DeclarativeBase):
    __tablename__ = 'Turnover'
    turnover = Column('turnover',Integer)
    @staticmethod
    def getTurnover(session,commId=0,date=datetime.date.today()):
        result = ()
        try:
            if commId:
                result = session.query(Commodity.commId,Turnover.turnover).\
                        filter(Turnover.commId == commId,Commodity.commId == commId,
                            Commodity.addedDate == date,
                            Turnover.addedDate == date).first()
            else:
                result = session.query(Commodity.commId,Turnover.turnover).\
                        filter(Commodity.commId == Turnover.commId,
                                Turnover.addedDate == date,
                                Commodity.addedDate == date).all()
        except NameError:
            print self.__class__.__name__ + 'session doesn\'t exist!'

        return result
class RateNumber(CommodityAttribute,DeclarativeBase):
    __tablename__ = 'RateNumber'
    rateNumber = Column('rateNumber',Integer)
    @staticmethod
    def getRateNumber(session,commId=0,date=datetime.date.today()):
        result = ()
        try:
            if commId:
                result = session.query(Commodity.commId,RateNumber.rateNumber).\
                        filter(RateNumber.commId == commId,Commodity.commId == commId,
                            Commodity.addedDate == date,
                            RateNumber.addedDate == date).first()
            else:
                result = session.query(Commodity.commId,RateNumber.rateNumber).\
                        filter(Commodity.commId == RateNumber.commId,
                                RateNumber.addedDate == date,
                                Commodity.addedDate == date).all()
        except NameError:
            print self.__class__.__name__ + 'session doesn\'t exist!'

        return result


class Price(CommodityAttribute,DeclarativeBase):
    __tablename__ = 'Price'
    price = Column('price',Float)
    @staticmethod
    def getPrice(session,commId=0,date=datetime.date.today()):
        result = ()
        try:
            if commId:
                result = session.query(Commodity.commId,Price.price).\
                        filter(Price.commId == commId,Commodity.commId == commId,
                            Commodity.addedDate == date,
                            Price.addedDate == date).first()
            else:
                result = session.query(Commodity.commId,Price.price).\
                        filter(Commodity.commId == Price.commId,
                                Price.addedDate == date,
                                Commodity.addedDate == date).all()
        except NameError:
            print self.__class__.__name__ + 'session doesn\'t exist!'

        return result


############################Comments##################################

#http://a.m.tmall.com/ajax/rate_list.do?item_id=20098897075&p=1&ps=15&rateRs=-1
# p : page, ps:page size, rateRs:rate type ---  1: good, 0: normal, -1:bad

class Comments(DeclarativeBase):
    __tablename__ = 'Comments'
    addedDate = Column(Date)
    commentId = Column(BigInteger,primary_key=True)
    commId = Column(BigInteger)
    #buyerName = Column(String)
    buyId = Column(BigInteger)
    useful = Column(Integer)
    rate = Column(Integer)
    time = Column(DateTime)
    text = Column(String)
    @staticmethod
    def getCommentsURLPrefix(session,commId=0,sellerId=0):
        #http://rate.taobao.com/feedRateList.htm?callback=jsonp_reviews_list&userNumId=380624657&auctionNumId=27610584433&currentPageNum=1
        try:
            if commId and sellerId:
                match_seller_id = session.query(Commodity.sellerId).filter(Commodity.commId == commId).first()[0]
                if(match_seller_id == sellerId):
                    return 'http://rate.taobao.com/feedRateList.htm?callback=jsonp_reviews_list&userNumId='\
                            + str(sellerId) + '&auctionNumId=' + str(commId) + '&currentPageNum='
                else:
                    return None

            elif commId:
                sellerId = session.query(Commodity.sellerId).filter(Commodity.commId == commId).first()[0]
                if sellerId:
                    return 'http://rate.taobao.com/feedRateList.htm?callback=jsonp_reviews_list&userNumId='\
                            + str(sellerId) + '&auctionNumId=' + str(commId) + '&currentPageNum='
                else:
                    return None

        except NameError:
            print self.__class__.__name__ + 'session doesn\'t exist!'


