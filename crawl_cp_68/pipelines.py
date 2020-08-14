from pymongo import MongoClient
# from crawl_cp_68.customize.telegram_notify import GTeleBot
from crawl_cp_68.import_setting import *

class MongoDBPipeline(object):
    def __init__(self):
        connection = MongoClient(settings.get('MONGODB_URI'))
        db = connection[settings['MONGODB_DATABASE']]
        # self.collection = db[settings['CRAWLER_COLLECTION']]
        self.collection = db.database[settings['CRAWLER_COLLECTION']]

    def process_item(self, item, spider):
        self.collection.insert(item)
        return item


# class ElasticsearchPipeline(object):
#     def __init__(self):
#         self.es_client = Elasticsearch(settings.get('ES_ADDRESS'))
#
#     def process_item(self, item, spider):
#         item.pop('_id')
#         self.es_client.index(index=settings.get('ES_CRAWL_INDEX'),
#                              doc_type=settings.get('ES_CRAWL_TYPE'),
#                              id=item.get('url'), body=item)
#         return item


# class KafkaPipeline(object):
#     def __init__(self):
#         try:
#             self.producer = KafkaProducer(bootstrap_servers=settings['KAFKA_ADDRESS'],
#                                           value_serializer=lambda x: dumps(x, ensure_ascii=False).encode('utf-8'))
#         except Exception as e:
#             logger.exception('Crawler kafka exception ' + str(e))
#             tele_bot.send_message('Crawler kafka not access')
#
#     def process_item(self, item, spider):
#         try:
#             item['_id'] = {'oid': str(item['_id'])}
#             item.pop('timestampISODate')
#             self.producer.send(settings['KAFKA_TOPIC'], value=item)
#             # print(item)
#             return item
#         except Exception as e:
#             logger.exception('Crawler url kafka exception ' + str(e))
#             tele_bot.send_message('Crawler url kafka exception ' + item.get('url'))
