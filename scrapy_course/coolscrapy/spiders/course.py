# -*- coding:utf8-*-
import scrapy
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')
from scrapy_course.items import  CourseItem
from scrapy.selector import Selector
sys.stdout = open('output.txt', 'w')
pageIndex = 0

class CourseSpider(scrapy.Spider):

    #��������Spider
    name = "MySpider"
    #������ʵ���
    allowed_domains = ['imooc.com']
    #��ȡ�ĵ�ַ
    start_urls = ["http://www.imooc.com/course/list"]
    #��ȡ����
    def parse(self, response):

        # ʵ��һ������������ȡ����Ϣ
        item = CourseItem()
        # �ⲿ������ȡ���֣�ʹ��xpath�ķ�ʽѡ����Ϣ�����巽��������ҳ�ṹ����
        # �Ȼ�ȡÿ���γ̵�div
        sel = Selector(response)
        title = sel.xpath('/html/head/title/text()').extract()  # ����
        print title[0]
        # sels = sel.xpath('//div[@class="course-card-content"]')
        sels = sel.xpath('//a[@class="course-card"]')
        pictures = sel.xpath('//div[@class="course-card-bk"]')
        index = 0
        global pageIndex
        pageIndex += 1
        print u'%s' % (time.strftime('%Y-%m-%d %H-%M-%S'))
        print '��' + str(pageIndex)+ 'ҳ '
        print '----------------------------------------------'
        for box in sels:
            print ' '
            # ��ȡdiv�еĿγ̱���
            item['title'] = box.xpath('.//h3[@class="course-card-name"]/text()').extract()[0].strip()
            print '���⣺' + item['title']

            # ��ȡdiv�еĿγ̼��
            item['introduction'] = box.xpath('.//p/text()').extract()[0].strip()
            print '��飺' + item['introduction']

            # ��ȡÿ��div�еĿγ�·��
            item['url'] = 'http://www.imooc.com' + box.xpath('.//@href').extract()[0]
            print  '·����' +item['url']

            # ��ȡdiv�е�ѧ������
            item['student'] = box.xpath('.//div[@class="course-card-info"]/text()').extract()[0].strip()
            print item['student']

            # ��ȡdiv�еı���ͼƬ��ַ
            item['image_url'] = pictures[index].xpath('.//img/@src').extract()[0]
            print 'ͼƬ��ַ��' + item['image_url']
            index += 1
            yield item

        time.sleep(1)
        print u'%s' % (time.strftime('%Y-%m-%d %H-%M-%S'))
        # next =u'��һҳ'
        # url = response.xpath("//a[contains(text(),'" + next + "')]/@href").extract()
        # if url:
        #     # ����Ϣ��ϳ���һҳ��url
        #     page = 'http://www.imooc.com' + url[0]
        #     # ����url
        #     yield scrapy.Request(page, callback=self.parse)