# # from scrapy.utils.project import get_project_settings
# import random
# import datetime
# # from bloom_filter import BloomFilter
# from pymongo import MongoClient
# from crawl_cp_68.customize import glog
# from scrapy.exceptions import IgnoreRequest
# from stem.control import Controller
# import time
# from scrapy.http import TextResponse
# from crawl_cp_68.import_setting import *
#
# logger = glog.config_log()
# settings = get_project_settings()
#
# class RandomUserAgentMiddleware(object):
#     def process_request(self, request, spider):
#         userAgent = random.choice(settings.get('USER_AGENT_LIST'))
#         if userAgent:
#             # request.headers.setdefault('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535')
#             request.headers.setdefault('User-Agent',
#                                        userAgent)
#             request.headers.setdefault('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
#             request.headers.setdefault('Accept-Encoding', 'gzip, deflate')
#             request.headers.setdefault('Accept-Language', 'en')
#             # request.headers.setdefault('Cache-Control', 'no-cache')
#             # request.headers.setdefault('Pragma', 'no-cache')
#
#         # logger.info('-------> ' + str(request.headers))
#         # logger.info('-------> ' + str(request.url))
#         # logger.info('-------> ' + str(request.body))
#         # logger.info('-------> ' + str(request.cookies))
#         # logger.info('-------> ' + str(request.meta))
#
#     def process_response(self, request, response, spider):
#         if isinstance(response, TextResponse):
#             return response
#         else:
#             return TextResponse(url=response.url, body=response.body, status=response.status, headers=response.headers,
#                                 flags=response.flags, request=response.request)
#
#
# class ProxyMiddleware(object):
#     def process_request(self, request, spider):
#         request.meta['proxy'] = settings.get('HTTP_PROXY')
#         # logger.info('Proxy : %s' % request.meta['proxy'])
#
#
# # class DuplicateFilterMiddleware(object):
# #     def __init__(self):
# #         try:
# #             logger.info('init middleware')
# #             logger.info(settings['CRAWLER_COLLECTION'])
# #             self.connection = MongoClient(settings.get('MONGODB_URI'))
# #             self.db = self.connection[settings['MONGODB_DATABASE']]
# #             self.collection = self.db[settings['CRAWLER_COLLECTION']]
# #             self.f = BloomFilter(max_elements=settings['BLOOM_FILTER_MAX_SIZE'],
# #                                  error_rate=settings['BLOOM_FILTER_ERROR_RATE'])
# #             logger.debug('init bloom filter')
# #             items = self.collection.find(
# #                 {'timestampISODate': {'$gt': datetime.datetime.now() - datetime.timedelta(7 * 365 / 12)}},
# #                 # {'timestampISODate': {'$gt': datetime.datetime.now() - datetime.timedelta(15)}},
# #                 no_cursor_timeout=True)
# #             count = 0
# #             for item in items:
# #                 self.f.add(normal(item['url']))
# #                 count += 1
# #             logger.info('done initializing bloom filter with size: ' + str(count))
# #         except Exception as e:
# #             print(str(e))
# #     def process_request(self, request, spider):
# #         if normal(request.url) in self.f:
# #             logger.info('found in bloomfilter:' + request.url, extra={'crawl_duplicate': 1})
# #             raise IgnoreRequest()
#
#
# # class RetryMiddleware(object):
# #     def __init__(self):
# #         self.controller = Controller.from_port(settings['TOR_HOST'], settings['TOR_PORT'])
# #
# #     def process_response(self, request, response, spider):
# #         if response.body.startswith(b'sorry'):
# #             logger.info('parse_page encountered an IP blocked of ' + str(response.url) + ' and status ' +
# #                         str(response.status) + ' and body ' + str(response.body),
# #                         extra={'crawl_retry': 1, 'domain': get_domain(response.url)})
# #             return self._retry(request)
# #         if response.status == 404:
# #             logger.info('404 {}'.format(response.url))
# #             if random.random() < 0.7:
# #                 return self._retry(request)
# #
# #         return response
# #
# #     def _retry(self, request):
# #         logger.info('crawl retry' + str(request))
# #         try:
# #             self.controller.new_circuit()
# #         except:
# #             pass
# #         time.sleep(random.randint(2, 4))
# #         retryreq = request.copy()
# #         retryreq.dont_filter = True
# #         return retryreq
