# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaobaoGoodsItem(scrapy.Item):
    GOODS_NAME = scrapy.Field()         # 商品名称
    GOODS_PRICE = scrapy.Field()        # 价格
    MONTHLY_SALES = scrapy.Field()      # 月销量
    GOODS_URL = scrapy.Field()          # 商品url


