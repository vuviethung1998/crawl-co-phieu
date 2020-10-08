# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from pymongo import MongoClient
# from crawl_cp_68.customize.telegram_notify import GTeleBot
from crawl_cp_cafef.import_setting import *

class MongoDBPipeline(object):
    def __init__(self):
        connection = MongoClient(settings.get('MONGODB_URI'))
        db = connection[settings['MONGODB_DATABASE']]

        # self.collection = {}
        # for collection_name in settings['CRAWLER_COLLECTION']:
        #     self.collection[collection_name] = db[collection_name]
        # self.collection = db.database[settings['CRAWLER_COLLECTION']]
        self.collection = db.database[settings['CRAWLER_COLLECTION']]

    def process_item(self, item, spider):
        self.collection.insert(item)
        return item

