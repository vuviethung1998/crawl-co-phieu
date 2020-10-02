import scrapy
from scrapy_splash import SplashRequest

class TryTorSpider(scrapy.Spider):
    name = 'try_tor'
    allowed_domains = ['check.torproject.org']
    start_urls = ['http://check.torproject.org/']

    script = """
        function main(splash, args)
          assert(splash:go(args.url))
          assert(splash:wait(1))
          return {
            html = splash:html()
          }
        end
        """

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                                endpoint='execute',
                                args={'lua_source': self.script}
                                )

    def parse(self, response):
        print(response.css('.content').extract_first())
