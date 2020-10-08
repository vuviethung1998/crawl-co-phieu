# -*- coding: utf-8 -*-
import scrapy

class TryTorSpider(scrapy.Spider):
    name = 'try_tor'
    allowed_domains = ['check.torproject.org']
    start_urls = ['http://check.torproject.org/']

    def parse(self, response):
        print(response.css('.content').extract_first())
