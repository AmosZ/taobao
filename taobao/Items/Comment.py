#-*-coding:utf-8-*- 
from scrapy.item import Item, Field
from scrapy.contrib.loader.processor import MapCompose, Join,TakeFirst
from utility import *
class Comment(Item):
#    base_xpath = './/ul[@class="tb-r-comments"]'
    #item_fields = {
            #'commentId': './/div[@class="tb-rev-item"]/@data-id ',
            #'buyerName': './/div[@class="tb-r-buyer"]//span[@class="tb-r-unick"]/text()',
            #'buyId':'.//div[@class="tb-r-buyer"]//a[@class="tb-r-ulink"]/@data-uid',
            #'text':'.//div[@class="tb-r-buyer"]//a[@class="tb-r-ulink"]/span[@class="tb-r-unick"]/text()',
            #}
    flag = Field(
            output_processor = TakeFirst()
            )

    commentId = Field(
            output_processor = TakeFirst()
            )

    commId = Field(
            output_processor = TakeFirst()
            )
    buyId = Field(
            output_processor = TakeFirst()
            )
    useful = Field(
            output_processor = TakeFirst()
            )
    rate = Field(
            output_processor = TakeFirst()
            )
    time = Field(
            input_processor=MapCompose(unicode.strip,getTime),
            output_processor = TakeFirst()
            )
    text = Field(
            output_processor = TakeFirst()
            )

