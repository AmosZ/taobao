#-*-coding:utf-8-*- 
import models
import sys
from scrapy.settings import Settings
from scrapy import log
import datetime
from sqlalchemy.orm import sessionmaker
class SellerPipeline(object):
    sellerList = {}
    commodityList = {}
    def __init__(self):
        engine = models.db_connect()
        models.create_deals_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        flag = item.get('flag',None)
        today = datetime.date.today()
        session = self.Session()
        if flag == 'Seller':
            #reputScore and positiveFeedbackRate may be empty
            seller = models.Seller(name=item['name'],id=item['sellerId'],addedDate=today)
            reputScore = models.ReputScore(id=item['sellerId'],addedDate=today,reputScore=item.get('reputScore',0))
            positiveFeedbackRate = models.PositiveFeedbackRate(id=item['sellerId'],addedDate=today,positiveFeedbackRate=item.get('positiveFeedbackRate',0.0))
            trueDesc = models.TrueDesc(id=item['sellerId'],addedDate=today,trueDesc=item['shopDesc'][0])
            servAttitude = models.ServAttitude(id=item['sellerId'],addedDate=today,servAttitude=item['shopDesc'][1])
            deliSpeed = models.DeliSpeed(id=item['sellerId'],addedDate=today,deliSpeed=item['shopDesc'][2])
#            print item['name'],item['sellerId'],item.get('reputScore',0),item.get('positiveFeedbackRate',0.0),item['shopDesc'][0],item['shopDesc'][1],item['shopDesc'][2]
#            log.msg(' name: '+ str(item['name']) 
                    #+ 'sellerId: ' + str(item['sellerId'])
                    #+ 'reputScore: ' + str(item['reputScore'])
                    #+ 'positiveFeedbackRate: ' + str(item['positiveFeedbackRate'])
                    #+ 'trueDesc: '+ str(item['shopDesc'][0])
                    #+ 'servAttitude: '+ str(item['shopDesc'][1])
                    #+ 'deliSpeed: '+ str(item['shopDesc'][2])
                    #,level=log.INFO)

#Why I can't set sellerId and date as primary key?
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
            commodity = models.Commodity(
                    title=item['title'],id=item['commId'],sellerId=item['sellerId'],addedDate=today
                    )
            turnover = models.Turnover(id=item['commId'],addedDate=today,turnover=item.get('turnover',0))
            rateNumber = models.RateNumber(id=item['commId'],addedDate=today,rateNumber=item.get('rateNumber',0))
#            print item['title'],item['commId'],item['sellerId'],item.get('turnover',0),item.get('rateNumber',0)
 #           log.msg('title'+ str(item['title'])
                    #+ 'commId:' + str(item['commId'])
                    #+ 'sellerId: '+ str(item['sellerId'])
                    #+ 'turnover: '+ str(item['turnover'])
                    #+ 'rateNumber:' + str(item['rateNumber'])
                    #,level=log.INFO)
            try:
                session.add(commodity)
                session.add(turnover)
                session.add(rateNumber)
                session.commit()
            except:
                session.rollback()
                raise
            finally:
                session.close()

        return item
