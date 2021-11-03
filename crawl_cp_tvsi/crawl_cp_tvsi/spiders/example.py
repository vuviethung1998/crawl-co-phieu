import scrapy
from crawl_cp_tvsi.import_setting import *
from crawl_cp_tvsi.config.ListStock import *

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        pass
