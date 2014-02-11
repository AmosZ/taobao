#-*-coding:utf-8-*- 
from peewee import *
db = PostgresqlDatabase('taobao',user='zq')
class PostgresqlModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db
#########################Seller#######################################
class SellerAttribute(PostgresqlModel):
    sellerId = BigIntegerField(index=True,unique=True)
    #datetime.date.today())
    addedDate = DateField(index=True)

class Seller(SellerAttribute):
    name = TextField()

class ReputScore(SellerAttribute):
    reputScore = BigIntegerField()

class PositiveFeedbackRate(SellerAttribute):
    positiveFeedbackRate = FloatField()

class TrueDesc(SellerAttribute):
    trueDesc = FloatField()

class ServAttitude(SellerAttribute):
    servAttitude = FloatField()

class DeliSpeed(SellerAttribute):
    deliSpeed = FloatField()

###########################Commodity#############################
class CommodityAttribute(PostgresqlModel):
    commId = BigIntegerField(index=True,unique=True)
    #datetime.date.today())
    addedDate = DateField(index=True)

class Commodity(CommodityAttribute):
    sellerId = BigIntegerField(index=True,unique=True)##seller id in taobao
    title = TextField()

class Turnover(CommodityAttribute):
    turnover = IntegerField()

class RateNumber(CommodityAttribute):
    rateNumber = IntegerField()



