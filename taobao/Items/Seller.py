#-*-coding:utf-8-*- 
from scrapy.item import Item, Field
from scrapy.contrib.loader.processor import MapCompose, Join
from utility import *
class Seller(Item):
    base_xpath = '//*[@id="J_ListContent"]/ul/li'
    item_fields = {
            'name': './/div[@class="seller"]/a/text()',
            #url : http://rate.taobao.com/user-rate-380624657.htm: http://rate.taobao.com/user-rate-$sellerId$.htm
#            'url': './/div[@class="title"]/a/@href',
            'sellerId': './/@data-quicklook',
            #10001－20000个卖家信用积分
            'reputScore': './/li[@class="ensurer"]/p/img/@title',
            'positiveFeedbackRate': './/li[@class="ensurer"]/p[@class="hp"]/text()',
            'shopDesc': './/li[@class="ensurer"]//ul[@class="dropdown-list"]/li/a/span/text()',
            }
    name = Field(
            input_processor = MapCompose(unicode.strip),
#            output_processor = Join()
            )
#   url : http://rate.taobao.com/user-rate-380624657.htm
#   url = Field(
#            input_processor = MapCompose(unicode.strip),
#            output_processor = Join()
#            )
    sellerId = Field(
            input_processor=MapCompose(unicode.strip,getSellerId),
#            output_processor=Join()
            )
    reputScore = Field(
            #10001－20000个卖家信用积分
            input_processor = MapCompose(unicode.strip,getReputScore),
#            output_processor = Join()
            )
    positiveFeedbackRate = Field(
            #好评率：99.86%
            input_processor = MapCompose(unicode.strip,getPositiveFeedbackRate),
#            output_processor = Join()
            )
#如实描述
#服务态度
#发货速度
    shopDesc = Field(
            input_processor = MapCompose(unicode.strip,getShopDesc),
    #        output_processor = Join()
            )

