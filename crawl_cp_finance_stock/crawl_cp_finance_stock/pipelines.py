# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from pymongo import MongoClient
# from crawl_cp_68.customize.telegram_notify import GTeleBot
from crawl_cp_finance_stock.import_setting import *
from scrapy.exceptions import DropItem

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
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            # self.collection[item['Chung_khoan_name']].insert(dict(item))
            self.collection.insert(dict(item))

        return item

if __name__=="__main__":
    connection = MongoClient(settings["MONGODB_URI"])
    db = connection[settings["MONGODB_DATABASE"]]
    test = db["AAA"].find({})
    for x in test:
        print(x)


