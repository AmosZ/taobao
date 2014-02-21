#-*-coding:utf-8-*- 
import models
import sys
from scrapy.settings import Settings
from scrapy import log
import datetime
from sqlalchemy.orm import sessionmaker
class ListPagePipeline(object):
    sellerList = {}
    commodityList = {}
    def __init__(self):
        engine = models.db_connect()
        models.create_deals_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        if spider.name == 'list':
            flag = item.get('flag',None)
            today = datetime.date.today()
            session = self.Session()
            if flag == 'Seller':
                print item['name']
                #reputScore and positiveFeedbackRate may be empty
                seller = models.Seller(name=item['name'],sellerId=item['sellerId'],addedDate=today)
                reputScore = models.ReputScore(sellerId=item['sellerId'],addedDate=today,reputScore=item.get('reputScore',0))
                positiveFeedbackRate = models.PositiveFeedbackRate(sellerId=item['sellerId'],addedDate=today,positiveFeedbackRate=item.get('positiveFeedbackRate',0.0))
                trueDesc = models.TrueDesc(sellerId=item['sellerId'],addedDate=today,trueDesc=item['shopDesc'][0])
                servAttitude = models.ServAttitude(sellerId=item['sellerId'],addedDate=today,servAttitude=item['shopDesc'][1])
                deliSpeed = models.DeliSpeed(sellerId=item['sellerId'],addedDate=today,deliSpeed=item['shopDesc'][2])
                try:
                    session.add(seller)
                    session.add(reputScore)
                    session.add(positiveFeedbackRate)
                    session.add(trueDesc)
                    session.add(servAttitude)
                    session.add(deliSpeed)
                    session.commit()
                except:
                    session.rollback()
                    raise
                finally:
                    session.close()

            elif flag == 'Commodity':
                #turnover and rateNumber maybe empty
                print item['title']
                commodity = models.Commodity(
                        title=item['title'],commId=item['commId'],sellerId=item['sellerId'],addedDate=today
                        )
                turnover = models.Turnover(commId=item['commId'],addedDate=today,turnover=item.get('turnover',0))
                rateNumber = models.RateNumber(commId=item['commId'],addedDate=today,rateNumber=item.get('rateNumber',0))
                price = models.Price(commId=item['commId'],addedDate=today,price=item['price'])
                try:
                    session.add(commodity)
                    session.add(turnover)
                    session.add(rateNumber)
                    session.add(price)
                    session.commit()
                except:
                    session.rollback()
                    raise
                finally:
                    session.close()

        elif spider.name == "comments":
            flag = item.get('flag',None)
            today = datetime.date.today()
            session = self.Session()
            if flag == 'comment':
                print item['commentId']
                comment = models.Comment(commentId=item['commentId'],commId=item['commId'],
                        buyerName=item['buyerName'],buyId=item['buyId'],text=item['text'],
                        addedDate=today)
                try:
                    session.add(comment)
                    session.commit()
                except:
                    session.rollback()
                    raise
                finally:
                    session.close()

        return item
