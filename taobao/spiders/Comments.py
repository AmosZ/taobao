#-*-coding:utf-8-*-
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.shell import inspect_response
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import MapCompose, Join
from sqlalchemy.orm import sessionmaker

#We define same Seller class in directory Models and Items.I
#It won't bring any confusion because Spider is at the highest layer and it can only access class Seller in Items
from ..Items.Seller import *
from ..Items.Commodity import *
import datetime
from .. import models

class CommentsSpider(Spider):
    name = "commentsSpider"
    allowed_domains = ["taobao.com"]
#    comment_xpath = '//ul[@class="tb-r-comments"]'
#    comment_xpath = '//*[@id="reviews"]/div[2]/ul'
    day = datetime.date.today()
    start_urls = ["http://item.taobao.com/item.htm?id=20128886326"]
    page = 0
    # We shoud query sellerId and commId to get URL
#    def __init__(self):
        #engine = models.db_connect()
        #self.Session = sessionmaker(bind=engine)
        #self.session = self.Session()

    #The default implementation uses make_requests_from_url() to generate Requests for each url in start_urls.
#    def start_requests(self):
        #urls =  models.Commodity.getCommodityURL(session=self.session,date=datetime.date(2014,2,12))
        #for url in urls:
            #yield self.make_requests_from_url(url)

    def parse(self,response):
 #       print response.body
        sel = Selector(response)
        self.page += 1
#        print sel.xpath('//*[@id="reviews"]/div[2]/ul/li[1]/div[2]/div/div[1]/text()')
 #       print sel.xpath('.//a[@class="tb-tab-anchor"]')
        print response.body

        ##Get commodity attributes
        #for s in sel.xpath(Commodity.base_xpath):
            #comm_loader = ItemLoader(Commodity(),selector=s)
            #comm_loader.add_value('page',self.page)
            #comm_loader.add_value('flag','Commodity')
            #for key,value in Commodity.item_fields.iteritems():
                #comm_loader.add_xpath(key,value)
            #yield comm_loader.load_item()

        #if(sel.xpath(self.next_page_xpath)):
            #yield Request("http://spu.taobao.com/spu/3c/detail.htm" +
                    #sel.xpath(self.next_page_xpath).extract()[0],
                    #callback=self.parse_list)
