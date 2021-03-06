#-*-coding:utf-8-*- 
import models
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
                #reputScore and positiveFeedbackRate may be empty
                seller = models.Seller(name=item['name'],sellerId=item['sellerId'])
                addedDate = models.SellerDate(sellerId=item['sellerId'],addedDate=today)
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
                    session.add(addedDate)
                    session.commit()
                except:
                    session.rollback()
                    raise
                finally:
                    session.close()

            elif flag == 'Commodity':
                #turnover and rateNumber maybe empty
                commodity = models.Commodity(
                        title=item['title'],commId=item['commId'],sellerId=item['sellerId']
                        )
                addedDate = models.CommodityDate(commId=item['commId'],addedDate=today)
                turnover = models.Turnover(commId=item['commId'],addedDate=today,turnover=item.get('turnover',0))
                rateNumber = models.RateNumber(commId=item['commId'],addedDate=today,rateNumber=item.get('rateNumber',0))
                price = models.Price(commId=item['commId'],addedDate=today,price=item['price'])
                try:
                    session.add(commodity)
                    session.add(addedDate)
                    session.add(turnover)
                    session.add(rateNumber)
                    session.add(price)
                    session.commit()
                except:
                    session.rollback()
                    raise
                finally:
                    session.close()

        elif spider.name == "detail":
            flag = item.get('flag',None)
            today = datetime.date.today()
            session = self.Session()
            if flag == 'comment':
                comment = models.Comments(commentId=item['commentId'],commId=item['commId'],rate=item['rate'],
                        buyId=item['buyId'],text=item['text'],time=item['time'],useful=item['useful'],
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
