#-*-coding:utf-8-*- 
import models
from scrapy.settings import Settings
from scrapy import log
class SellerPipeline(object):
    def __init__(self):
        models.db.connect()
        models.Seller.create_table(fail_silently=True)
        models.Commodity.create_table(fail_silently=True)

    def process_item(self, item, spider):
        flag = item.get('flag',None)
#        print flag
        if flag == 'Seller':
            #reputScore and positiveFeedbackRate may be empty
            seller = models.Seller(
                    name=item['name'],sellerId=item['sellerId'],reputScore=item.get('reputScore',0),
                    positiveFeedbackRate = item.get('positiveFeedbackRate',0.0),trueDesc = item['shopDesc'][0],
                    servAttitude = item['shopDesc'][1],deliSpeed=item['shopDesc'][2]
                    )
#            print item['name'],item['sellerId'],item.get('reputScore',0),item.get('positiveFeedbackRate',0.0),item['shopDesc'][0],item['shopDesc'][1],item['shopDesc'][2]
#            log.msg(' name: '+ str(item['name']) 
                    #+ 'sellerId: ' + str(item['sellerId'])
                    #+ 'reputScore: ' + str(item['reputScore'])
                    #+ 'positiveFeedbackRate: ' + str(item['positiveFeedbackRate'])
                    #+ 'trueDesc: '+ str(item['shopDesc'][0])
                    #+ 'servAttitude: '+ str(item['shopDesc'][1])
                    #+ 'deliSpeed: '+ str(item['shopDesc'][2])
                    #,level=log.INFO)
            seller.save()

        elif flag == 'Commodity':
            #turnover and rateNumber maybe empty
            commodity = models.Commodity(
                    title=item['title'],commId=item['commId'],sellerId=item['sellerId'],
                    turnover=item.get('turnover',0),rateNumber=item.get('rateNumber',0)
                    )
#            print item['title'],item['commId'],item['sellerId'],item.get('turnover',0),item.get('rateNumber',0)
 #           log.msg('title'+ str(item['title'])
                    #+ 'commId:' + str(item['commId'])
                    #+ 'sellerId: '+ str(item['sellerId'])
                    #+ 'turnover: '+ str(item['turnover'])
                    #+ 'rateNumber:' + str(item['rateNumber'])
                    #,level=log.INFO)
            commodity.save()
        return item
