#-*-coding:utf-8-*- 
from peewee import *
db = PostgresqlDatabase('taobao',user='zq')
class PostgresqlModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db
#########################Seller#######################################
class SellerAttribute(PostgresqlModel):
#   One Seller may appear on different pages.
    sellerId = BigIntegerField(index=True)
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
#   One Commodity may appear on different pages.
    commId = BigIntegerField(index=True)
    #datetime.date.today())
    addedDate = DateField(index=True)

class Commodity(CommodityAttribute):
    sellerId = BigIntegerField(index=True)##seller id in taobao
    title = TextField()

class Turnover(CommodityAttribute):
    turnover = IntegerField()

class RateNumber(CommodityAttribute):
    rateNumber = IntegerField()



