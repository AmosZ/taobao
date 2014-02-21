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
from ..Items.Comment import *
import datetime
from .. import models

class CommentsSpider(Spider):
    name = "detail"
    allowed_domains = ["taobao.com","item.taobao.com"]
    day = datetime.date.today()
    #start_urls = ["http://item.taobao.com/item.htm?id=20128886326"]
    page = 0
    headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'item.taobao.com',
            'Referer': 'http://spu.taobao.com/spu/3c/detail.htm?&cat=1512&spuid=229361412',
            'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36'\
                ' (KHTML, like Gecko) Chrome/30.0.1599.114 Safari/537.36',
            }
    # We shoud query sellerId and commId to get URL
    def __init__(self):
        engine = models.db_connect()
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()

    #The default implementation uses make_requests_from_url() to generate Requests for each url in start_urls.
    def start_requests(self):
        urls =  models.Commodity.getCommodityURL(session=self.session)
        #print urls
        for url in urls:
            yield Request(url,headers=self.headers,callback=self.parse)

    def parse(self,response):
        sel = Selector(response)
        self.page += 1
        #for s in sel.xpath(Comment.base_xpath):
        from scrapy.shell import inspect_response
        inspect_response(response)
        for s in sel.xpath('//*[@id="J_listBuyerOnView"]'):
            #[u'<div id="reviews" data-reviewapi="http://rate.taobao.com/detail_rate.htm?userNumId=853982&amp;auctionNumId=21894319337&amp;showContent=1&amp;currentPage=1&amp;ismore=0&amp;siteID=7" data-reviewcountapi="" data-listapi="http://rate.taobao.com/feedRateList.htm?userNumId=853982&amp;auctionNumId=21894319337&amp;siteID=7" data-commonapi="http://orate.alicdn.com/detailCommon.htm?userNumId=853982&amp;auctionNumId=21894319337&amp;siteID=7" data-usefulapi="http://rate.taobao.com/vote_useful.htm?userNumId=853982&amp;auctionNumId=21894319337">\r\n</div>']

            common_loader = ItemLoader(Comment(),selector=s)
            # iterate over fields and add xpaths to the common_loader
            common_loader.add_value('page',self.page)
            common_loader.add_value('flag','comment')
            for key,value in Comment.item_fields.iteritems():
                common_loader.add_xpath(key,value)
            yield common_loader.load_item()

        sel.xpath('//*[@id="J_listBuyerOnView"]/@data-api').extract()
    #[u'http://detailskip.taobao.com/json/show_buyer_list.htm?step=false&bid_page=1&page_size=15&item_type=b&ends=1393151382000&starts=1392546582000&item_id=37213780715&user_tag=337448960&old_quantity=2800&zhichong=true&sold_total_num=16&seller_num_id=1723583774&dk=0&title=%B5%B1%CC%EC%B7%A2+%CB%CD%BA%EC%B0%FC+%BC%D9%D2%BB%C5%E2%CD%F2+Apple%2F%C6%BB%B9%FB+iPhone+5s+%C6%BB%B9%FB5s+%C8%D5%B0%E6%CA%D6%BB%FA&sbn=49d392362c217a64309a3d99b957b776&isTKA=false&msc=1']















