#-*-coding:utf-8-*- 
from peewee import *
db = PostgresqlDatabase('taobao',user='zq')
class PostgresqlModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db


class Seller(PostgresqlModel):
    seller_id = PrimaryKeyField()
    sellerId = BigIntegerField(index=True)#seller id in taobao
    name = TextField()
    reputScore = BigIntegerField()
    positiveFeedbackRate = FloatField()

    #Shop describe
    trueDesc = FloatField()
    servAttitude = FloatField()
    deliSpeed = FloatField()

class Commodity(PostgresqlModel):
    commodity_id = PrimaryKeyField()
    commId = BigIntegerField(index=True)#Commodity id in taobao
    sellerId = BigIntegerField(index=True)##seller id in taobao
    title = TextField()
    turnover = IntegerField()
    rateNumber = IntegerField()

def disconnect():
    db.close()
