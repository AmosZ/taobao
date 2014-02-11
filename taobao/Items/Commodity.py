#-*-coding:utf-8-*- 
from scrapy.item import Item, Field
from scrapy.contrib.loader.processor import MapCompose, Join,TakeFirst
from utility import *
class Commodity(Item):
    base_xpath = '//*[@id="J_ListContent"]/ul/li'
    item_fields = {
            'title': './/h3[@class="title"]/a/text()',
            #url: http://item.taobao.com/item.htm?id=19904928406
            'commId': './/@data-quicklook',
            'sellerId':'.//@data-quicklook',
            'turnover': './/ul[@class="attribute"]/li[@class="trade"]/p[1]',
            'rateNumber': './/@data-quicklook',
            }
    page = Field()
    flag = Field(
            output_processor = TakeFirst()
            )

    title = Field(
            input_processor = MapCompose(unicode.strip),
            output_processor = TakeFirst()
            )
    commId = Field(
            input_processor=MapCompose(unicode.strip,getItemId),
            output_processor=TakeFirst()
            )
    sellerId = Field(
            input_processor=MapCompose(unicode.strip,getSellerId),
            output_processor=TakeFirst()
            )

#最近成交227笔
    turnover = Field(
            input_processor=MapCompose(unicode.strip,getTurnover),
            output_processor=TakeFirst()
            )
#evaNum':'5313 in data-quicklook
    rateNumber = Field(
            input_processor=MapCompose(unicode.strip,getEvaNum),
            output_processor=TakeFirst()
            )
