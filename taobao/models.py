from peewee import *
db = PostgresqlDatabase('taobao',user='zq')
class PostgresqlModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db

def connect():
    db.connect()

class Commodity(PostgresqlModel):
    commodity_id = PrimaryKeyField()
#Avoid circular reference
#    seller_id = ForeignKeyField(Seller,related_name='seller_id')
    title = TextField()
    commId = BigIntegerField()
    turnover = IntegerField()
    rateNumber = IntegerField()

class Seller(PostgresqlModel):
    seller_id = PrimaryKeyField()
    commodity_id = ForeignKeyField(Commodity,related_name='seller')
    name = TextField()
    sellerId = BigIntegerField()
    reputScore = BigIntegerField()
    positiveFeedbackRate = FloatField()

    #Shop describe
    trueDesc = FloatField()
    servAttitude = FloatField()
    deliSpeed = FloatField()

