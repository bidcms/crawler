# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaobaoGoodsItem(scrapy.Item):
    GOODS_NAME = scrapy.Field()         # ��Ʒ����
    GOODS_PRICE = scrapy.Field()        # �۸�
    MONTHLY_SALES = scrapy.Field()      # ������
    GOODS_URL = scrapy.Field()          # ��Ʒurl


