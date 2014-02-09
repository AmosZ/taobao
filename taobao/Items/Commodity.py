#-*-coding:utf-8-*- 
from scrapy.item import Item, Field
from scrapy.contrib.loader.processor import MapCompose, Join
from utility import *
class Commodity(Item):
    base_xpath = '//*[@id="J_ListContent"]/ul/li'
    item_fields = {
            'title': './/h3[@class="title"]/a/text()',
            #'url': './/h3[@class="title"]/a/@href',
            #url: http://item.taobao.com/item.htm?id=19904928406
            'commId': './/@data-quicklook',
            'turnover': './/ul[@class="attribute"]/li[@class="trade"]/p[1]',
            'rateNumber': './/@data-quicklook',
            }

    title = Field(
            input_processor = MapCompose(unicode.strip),
#            output_processor = Join()
            )
#    url = Field(
#            input_processor = MapCompose(unicode.strip),
#            output_processor = Join()
#            )
#最近成交227笔
    turnover = Field(
            input_processor=MapCompose(unicode.strip,getTurnover),
#            output_processor=Join()
            )
#evaNum':'5313 in data-quicklook
    rateNumber = Field(
            input_processor=MapCompose(unicode.strip,getEvaNum),
#            output_processor=Join()
            )
