# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random
from scrapy import signals
from crawl_cp_tvsi.import_setting import *
from scrapy.http import TextResponse
from stem.control import Controller
import time

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        userAgent = random.choice(settings.get('USER_AGENT_LIST'))
        if userAgent:
            request.headers.setdefault('User-Agent', userAgent)
            request.headers.setdefault('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
            request.headers.setdefault('Accept-Encoding', 'gzip, deflate')
            request.headers.setdefault('Accept-Language', 'en')

    def process_response(self, request, response, spider):
        if isinstance(response, TextResponse):
            return response
        else:
            return TextResponse(url=response.url, body=response.body, status=response.status, headers=response.headers,
                                flags=response.flags, request=response.request)


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = settings.get('HTTP_PROXY')

class RetryMiddleware(object):
    def __init__(self):
        self.controller = Controller.from_port(settings['TOR_HOST'], settings['TOR_PORT'])

    def process_response(self, request, response, spider):
        if response.body.startswith(b'sorry'):
            # logger.info('parse_page encountered an IP blocked of ' + str(response.url) + ' and status ' +
            #             str(response.status) + ' and body ' + str(response.body),
            #             extra={'crawl_retry': 1, 'domain': get_domain(response.url)})
            return self._retry(request)
        if response.status == 404:
            # logger.info('404 {}'.format(response.url))
            if random.random() < 0.7:
                return self._retry(request)

        return response

    def _retry(self, request):
        # logger.info('crawl retry' + str(request))
        try:
            self.controller.new_circuit()
        except:
            pass
        time.sleep(random.randint(2, 4))
        retryreq = request.copy()
        retryreq.dont_filter = True
        return retryreq