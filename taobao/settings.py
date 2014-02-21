# Scrapy settings for taobao project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'taobao'

SPIDER_MODULES = ['taobao.spiders']
NEWSPIDER_MODULE = 'taobao.spiders'

ITEM_PIPELINES = {
        'taobao.pipelines.ListPagePipeline':100,
#        'taobao.pipelines.CommodityPipeline':200,
        }
DATABASE = {'drivername': 'postgres',
            'host': 'localhost',
            'port': '5432',
            'username': 'zq',
            'password': '111111',
            'database': 'taobao'}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.5 Safari/537.36'
#COOKIES_ENABLED = False
#DOWNLOAD_DELAY = 0.25
