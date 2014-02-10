# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import models
class SellerPipeline(object):
    def __init__(self):
        models.db.connect()
        models.Seller.create_table(fail_silently=True)
        models.Commodity.create_table(fail_silently=True)

    def process_item(self, item, spider):
        flag = item.get('flag',None)
#        print flag
        if flag == 'Seller':
            seller = models.Seller(
                    name=item['name'],sellerId=item['sellerId'],commId=item['commId'],reputScore=item['reputScore'],
                    positiveFeedbackRate = item['positiveFeedbackRate'],trueDesc = item['shopDesc'][0],
                    servAttitude = item['shopDesc'][1],deliSpeed=item['shopDesc'][2]
                    )
            print item['name'],item['sellerId'],item['reputScore'],item['positiveFeedbackRate'],item['shopDesc'][0],item['shopDesc'][1],item['shopDesc'][2]
            seller.save()

        elif flag == 'Commodity':
            commodity = models.Commodity(
                    title=item['title'],commId=item['commId'],sellerId=item['sellerId'],
                    turnover=item['turnover'],rateNumber=item['rateNumber']
                    )
            print item['title'],item['commId'],item['sellerId'],item['turnover'],item['rateNumber']
            commodity.save()
        return item
