# -*- coding: utf-8 -*-
import scrapy
import os

class Haokan5Spider(scrapy.Spider):
    name = 'haokan5'
    classid = '13'
    root_path = os.path.dirname(os.path.abspath(__file__)) + '/' + name
    all_file = root_path + '/all.txt'
    collected_file = root_path + '/collected.txt'
    failed_file = root_path + '/failed.txt'
    def __init__(self):
        if not os.path.exists(root_path):
            os.makedirs(root_path)
        collected_books = failed_books = []
        if os.path.exists(collected_file):
            with open(collected_file) as fclist:
                collected_books = fclist.read().split("\n")
        if os.path.exists(failed_file):
            with open(failed_file) as fclist:
                failed_books = fclist.read().split("\n")
                
        self.source_id = ''
        self.site_id = '0'
        if os.path.exists(all_file):
            with open(all_file) as fall:
                books = fall.read().split("\n")
                for book in books:
                    book_info = book.split('|')
                    if book_info[1] not in collected_books:
                        self.source_id = book_info[1]
                        self.site_id = book_info[0]
                        book_title = book_info[2]
                        break
        if source_id != '':
            history_path = root_path + '/history/' + source_id
            if not os.path.exists(history_path):
                os.makedirs(history_path)
            self.item_id_file = history_path + '/id.txt'
            item_book_file = history_path + '/book.txt'
            item_urls_file = history_path + '/urls.txt'
            item_success_file = history_path + '/success.txt'
            item_fail_file = history_path + '/fail.txt'
            if os.path.exists(item_urls_file):
                with open(item_urls_file) as furls:
                    item_urls_list = furls.read().split("\n")
            if os.path.exists(item_success_file):
                with open(item_success_file) as fsuccess:
                    item_success_list = fsuccess.read().split("\n")
            if os.path.exists(item_fail_file):
                with open(item_fail_file) as ffail:
                    item_fail_lists = ffail.read().split("\n")

    def start_requests(self):
        #获取主信息
        url ='http://www.haokan5.com/show/' + self.source_id + '.html'
        if os.path.exists(self.item_id_file):
            with open(self.item_id_file) as fid:
                self.site_id = fid.read()
        else:
            yield scrapy.Request(url=url,callback=self.parse_book)
        pass

    def parse_book(self, response):
        selecor = scrapy.Selector(response)

        item['images'] = selecor.xpath('img[class="imgd"]/@src').extract_first()
        item['title'] = selecor.xpath('img[class="imgd"]/@alt').extract_first()
        conlist = selecor.xpath('div[class="conlist"]/p')
        item['author'] = conlist[5].xpath("/text()").extract_first()
        item['category'] = conlist[0].xpath("/text()").extract_first()
        item['class_id'] = classid;

        item['status'] = conlist[2].xpath("/text()").extract_first()
        item['audio'] = conlist[4].xpath("/text()").extract_first()
        item['intro'] = selecor.xpath('ul[class="introbox"]/p')[0].xpath('/text()').extract_first()
        with open(self.item_id_file) as fid:
            fid.write('12')
        print(item)
        pass
