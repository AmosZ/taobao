#-*-coding:utf-8-*-
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import re,json
import datetime
#text: {'sellerId':'196118321','itemId':'19974242521','evaNum':'5313','virtual':'false'}
def getSellerId(text):
    text = text.replace('\'','')
    p = re.compile(r'sellerId:(\d+)')
    r = p.search(text)
    if r:
        return int(r.group(1))
    else:
        return 0

#text: {'sellerId':'196118321','itemId':'19974242521','evaNum':'5313','virtual':'false'}
def getItemId(text):
    text = text.replace('\'','')
    p = re.compile(r'itemId:(\d+)')
    r = p.search(text)
    if r:
        return int(r.group(1))
    else:
        return 0

#text: {'sellerId':'196118321','itemId':'19974242521','evaNum':'5313','virtual':'false'}
def getEvaNum(text):
    text = text.replace('\'','')
    p = re.compile(r'evaNum:(\d+)')
    r = p.search(text)
    if r:
        return int(r.group(1))
    else:
        return 0

#text:20001－50000个卖家信用积分
def getReputScore(text):
    p = re.compile(r'^\d+')
    r = p.search(text)
    if r:
        return int(r.group(0))
    else:
        return 0
#text: 好评率：99.86%
def getPositiveFeedbackRate(text):
    p = re.compile(r'\d\d\.\d\d')
    r = p.search(text)
    if r:
        return float(r.group(0))
    else:
        return 0.0
#如实描述:4.7
#服务态度:4.7
#发货速度:4.8
def getShopDesc(text):
    p = re.compile(r'\d\.\d')
    r = p.search(text)
    if r:
        return float(r.group(0))
    else:
        return 0.0

def getTurnover(text):
    p = re.compile(r'\d+')
    r = p.search(text)
    if r:
        return int(r.group(0))
    else:
        return 0
def getPrice(text):
    return float(text)

def getBuyId(text):
    return int(text)

def getCommentId(text):
   return int(text)

def getTime(time_string):
    print "time_string" + time_string
    p = re.compile(r'^(\d{4})\D+(\d{2})\D+(\d{2})\D+\s+(\d{2}):(\d{2})')
    year = int(p.search(time_string).group(1))
    month = int(p.search(time_string).group(2))
    date = int(p.search(time_string).group(3))
    hour = int(p.search(time_string).group(4))
    minute = int(p.search(time_string).group(5))
    return datetime.datetime(year,month,date,hour,minute)

