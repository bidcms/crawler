# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class CourseItem(scrapy.Item):
    title = scrapy.Field()    # 标题
    url = scrapy.Field()     # 链接
    image_url = scrapy.Field()     # 标题图片
    introduction = scrapy.Field() # 课程描述
    student = scrapy.Field() # 学习人数
