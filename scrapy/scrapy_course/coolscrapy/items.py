# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class CourseItem(scrapy.Item):
    title = scrapy.Field()    # ����
    url = scrapy.Field()     # ����
    image_url = scrapy.Field()     # ����ͼƬ
    introduction = scrapy.Field() # �γ�����
    student = scrapy.Field() # ѧϰ����
