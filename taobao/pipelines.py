# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import models
class TaobaoPipeline(object):
#    def __init__(self):
#        models.create_tables()

    def process_item(self, item, spider):
        print item
#        commodity = models.Commodity(title=item['title'],url=item['url'],sellerId=item['sellerId'])
        #commodity = models.Commodity(title=item['title'],url=item['url'])
#        commodity.save()
        return item
