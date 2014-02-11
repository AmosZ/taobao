#-*-coding:utf-8-*- 
import models
import sys
from scrapy.settings import Settings
from scrapy import log
import datetime
class SellerPipeline(object):
    sellerList = {} 
    commodityList = {}
    def __init__(self):
        models.db.connect()

        #Seller
        models.Seller.create_table(fail_silently=True)
        models.ReputScore.create_table(fail_silently=True)
        models.PositiveFeedbackRate.create_table(fail_silently=True)
        models.TrueDesc.create_table(fail_silently=True)
        models.ServAttitude.create_table(fail_silently=True)
        models.DeliSpeed.create_table(fail_silently=True)

        #Commodity
        models.Commodity.create_table(fail_silently=True)
        models.Turnover.create_table(fail_silently=True)
        models.RateNumber.create_table(fail_silently=True)

    def process_item(self, item, spider):
        flag = item.get('flag',None)
        today = datetime.date.today()
        if flag == 'Seller':
            #reputScore and positiveFeedbackRate may be empty
            seller = models.Seller(name=item['name'],sellerId=item['sellerId'],addedDate=today)
            reputScore = models.ReputScore(sellerId=item['sellerId'],addedDate=today,reputScore=item.get('reputScore',0))
            positiveFeedbackRate = models.PositiveFeedbackRate(sellerId=item['sellerId'],addedDate=today,positiveFeedbackRate=item.get('positiveFeedbackRate',0.0))
            trueDesc = models.TrueDesc(sellerId=item['sellerId'],addedDate=today,trueDesc=item['shopDesc'][0])
            servAttitude = models.ServAttitude(sellerId=item['sellerId'],addedDate=today,servAttitude=item['shopDesc'][1])
            deliSpeed = models.DeliSpeed(sellerId=item['sellerId'],addedDate=today,deliSpeed=item['shopDesc'][2])
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
            seller.save()
            reputScore.save()
            positiveFeedbackRate.save()
            trueDesc.save()
            servAttitude.save()
            deliSpeed.save()

        elif flag == 'Commodity':
            #turnover and rateNumber maybe empty
            commodity = models.Commodity(
                    title=item['title'],commId=item['commId'],sellerId=item['sellerId'],addedDate=today
                    )
            turnover = models.Turnover(commId=item['commId'],addedDate=today,turnover=item.get('turnover',0))
            rateNumber = models.RateNumber(commId=item['commId'],addedDate=today,rateNumber=item.get('rateNumber',0))
#            print item['title'],item['commId'],item['sellerId'],item.get('turnover',0),item.get('rateNumber',0)
 #           log.msg('title'+ str(item['title'])
                    #+ 'commId:' + str(item['commId'])
                    #+ 'sellerId: '+ str(item['sellerId'])
                    #+ 'turnover: '+ str(item['turnover'])
                    #+ 'rateNumber:' + str(item['rateNumber'])
                    #,level=log.INFO)
            commodity.save()
            turnover.save()
            rateNumber.save()

        return item
