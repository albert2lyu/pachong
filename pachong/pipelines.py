# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class PachongPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.pchdb = self.client['pchdb']
        self.pchtab = self.pchdb['pchtab']

    def process_item(self, item, spider):
        self.pchtab.insert_one(dict(item))
        return item
