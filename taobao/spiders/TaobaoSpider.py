from scrapy.spider import Spider
from scrapy.selector import Selector
from taobao.items import Category,Retailer
from scrapy.http import Request
from scrapy.shell import inspect_response
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import MapCompose, Join
from scrapy import log

class TaobaoSpider(Spider):
    name = "taobao"
    allowed_domains = ["taobao.com"]
    start_urls = ["http://www.taobao.com/market/3c/phone_index.php"]

    category_url_xpath = '//*[@id="guid-1355118887616"]/div/div/div/p[1]/a[1]/@href'
    item_fields = {
            'title': './/a/text()',
            'url': './/a/@href'
            }

    def parse(self,response):
        selector = Selector(response)
        for url in selector.xpath(self.category_url_xpath).extract():
            yield Request(url,callback=self.parse_list)

    def parse_list(self,response):
        retailer_list_xpath = '//h3[@class="title"]'
        sel = Selector(response)
        for s in sel.xpath(retailer_list_xpath):
            loader = ItemLoader(Retailer(),selector=s)

            # define processors
            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()

            # iterate over fields and add xpaths to the loader
            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
            yield loader.load_item()

