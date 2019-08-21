# -*- coding: utf-8 -*-
import os,requests

name = 'haokan5'
root_path = os.path.dirname(os.path.abspath(__file__)) + '/' + name
print(root_path)

if not os.path.exists(root_path):
    os.makedirs(root_path)
all_file = root_path + '/all.txt'
collected_file = root_path + '/collected.txt'
failed_file = root_path + '/failed.txt'

collected_books = failed_books = []
if os.path.exists(collected_file):
    with open(collected_file) as fclist:
        collected_books = fclist.read().split("\n")
if os.path.exists(failed_file):
    with open(failed_file) as fclist:
        failed_books = fclist.read().split("\n")
        
source_id = ''    
if os.path.exists(all_file):
    with open(all_file) as fall:
        books = fall.read().split("\n")
        for book in books:
            book_info = book.split('|')
            if book_info[1] not in collected_books:
                source_id = book_info[1]
                break
print(source_id)
#获取主信息
url ='http://www.haokan5.com/show/' + source_id + '.html'
response = requests.get(url)
print(response.text)
