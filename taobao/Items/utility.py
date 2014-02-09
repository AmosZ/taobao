#-*-coding:utf-8-*-
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import re
#text: {'sellerId':'196118321','itemId':'19974242521','evaNum':'5313','virtual':'false'}
def getSellerId(text):
    text = text.replace('\'','')
    p = re.compile(r'sellerId:(\d+)')
    return int(p.search(text).group(1))

#text: {'sellerId':'196118321','itemId':'19974242521','evaNum':'5313','virtual':'false'}
def getItemId(text):
    text = text.replace('\'','')
    p = re.compile(r'itemId:(\d+)')
    return int(p.search(text).group(1))

#text: {'sellerId':'196118321','itemId':'19974242521','evaNum':'5313','virtual':'false'}
def getEvaNum(text):
    text = text.replace('\'','')
    p = re.compile(r'evaNum:(\d+)')
    return int(p.search(text).group(1)) #group(0) return evaNum:5313 itself. group(1) return '5313'

#text:20001－50000个卖家信用积分
def getReputScore(text):
    p = re.compile(r'^\d+')
    return int(p.search(text).group(0))
#text: 好评率：99.86%
def getPositiveFeedbackRate(text):
    p = re.compile(r'\d\d\.\d\d')
    return float(p.search(text).group(0))
#如实描述:4.7
#服务态度:4.7
#发货速度:4.8
def getShopDesc(text):
    p = re.compile(r'\d\.\d')
    return float(p.search(text).group(0))

def getTurnover(text):
    p = re.compile(r'\d+')
    return int(p.search(text).group(0))
