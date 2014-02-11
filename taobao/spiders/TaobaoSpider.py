#-*-coding:utf-8-*-
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.shell import inspect_response
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import MapCompose, Join
from scrapy import log
#We define same Seller class in directory Models and Items.I
#It won't bring any confusion because Spider is at the highest layer and it can only access class Seller in Items
from ..Items.Seller import *
from ..Items.Commodity import *

class TaobaoSpider(Spider):
    name = "taobao"
    allowed_domains = ["taobao.com"]
    start_urls = ["http://www.taobao.com/market/3c/phone_index.php"]

    category_url_xpath = '//*[@id="guid-1355118887616"]/div/div/div/p[1]/a[1]/@href'
#   start_urls = ["http://spu.taobao.com/spu/3c/detail.htm?&cat=1512&spuid=229361412"]
    next_page_xpath = './/a[@class="vm-page-next"]/@href'
    page = 0
    #Retrieve iphone5s list url
    def parse(self,response):
        selector = Selector(response)
        yield Request(selector.xpath(self.category_url_xpath).extract()[0],callback=self.parse_list)

    #Parse iphone5s list
    def parse_list(self,response):
        #Get seller attributes
        sel = Selector(response)
        self.page += 1
        for s in sel.xpath(Seller.base_xpath):
            seller_loader = ItemLoader(Seller(),selector=s)

            # iterate over fields and add xpaths to the seller_loader
            seller_loader.add_value('page',self.page)
            seller_loader.add_value('flag','Seller')
            seller_loader.add_xpath('name',Seller.item_fields['name'])
            seller_loader.add_xpath('sellerId',Seller.item_fields['sellerId'])
            seller_loader.add_xpath('reputScore',Seller.item_fields['reputScore'])
            seller_loader.add_xpath('positiveFeedbackRate',Seller.item_fields['positiveFeedbackRate'])
            seller_loader.add_xpath('shopDesc',Seller.item_fields['shopDesc'])
            yield seller_loader.load_item()

        #Get commodity attributes
        for s in sel.xpath(Commodity.base_xpath):
            comm_loader = ItemLoader(Commodity(),selector=s)
            comm_loader.add_value('page',self.page)
            comm_loader.add_value('flag','Commodity')
            comm_loader.add_xpath('title',Commodity.item_fields['title'])
            comm_loader.add_xpath('commId',Commodity.item_fields['commId'])
            comm_loader.add_xpath('sellerId',Commodity.item_fields['sellerId'])
            comm_loader.add_xpath('turnover',Commodity.item_fields['turnover'])
            comm_loader.add_xpath('rateNumber',Commodity.item_fields['rateNumber'])
            yield comm_loader.load_item()

        if(sel.xpath(self.next_page_xpath)):
            yield Request("http://spu.taobao.com/spu/3c/detail.htm" +
                    sel.xpath(self.next_page_xpath).extract()[0],
                    callback=self.parse_list)

