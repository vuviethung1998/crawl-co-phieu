import json
from scrapy.spiders import CrawlSpider
from scrapy import Request, FormRequest
import random
from crawl_cp_tvsi.import_setting import *
from crawl_cp_tvsi.config.ListStock import *
from bs4 import BeautifulSoup as soup

class TvsiStockTopCompanySpider(CrawlSpider):
    name = "tvsi_stock_top_company"

    def __init__(self, **kwargs):
        super(TvsiStockTopCompanySpider, self).__init__(**kwargs)
        self.allowed_domains = ['finance.tvsi.com.vn']

        self.lst_cp =  HOSE + HNX

        self.start_urls = ['https://finance.tvsi.com.vn'] # /tools/topCompanyPart
        settings['CRAWLER_COLLECTION'] = "INDUSTRY"

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, callback=self.parse, meta={
                "currentPage" : 1
            })

    def parse(self, response):
        current_page = response.meta['currentPage']

        # adata=0&adata=2&adata=12&adata=13&adata=18&adata=21&adata=23&adata=24&adata=36&adata=38&adata=50&adata=59&adata=62&adata=76&currentPage=1&exchange=&industryId=0&pageSize=100&SortKeyArr=MarketCap&SortDirectionArr=1&check=true&check_Cookie_Top=0
        yield FormRequest('https://finance.tvsi.com.vn/tools/topCompanyPart',
                          method="POST",
                          callback= self.parse_top_company,
                          body= 'adata=0&adata=1&adata=2&adata=3&adata=12&adata=13&adata=18&adata=21&adata=23&adata=24&adata=36&adata=38&adata=50&adata=59&adata=62&adata=76&currentPage={}&exchange=&industryId=0&pageSize=100&SortKeyArr=MarketCap&SortDirectionArr=1&check=true&check_Cookie_Top=0'.format(current_page),
                          headers= {
                              "X-Requested-With": "XMLHttpRequest",
                              "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                              'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
                              "User-Agent":  random.choice(settings.get('USER_AGENT_LIST')),
                          },
                          meta= {
                              "currentPage": current_page,
                          }
                      )


    def parse_top_company(self, response):


        top_company = response.text
        s = soup(top_company, features='lxml').table
        for tr in s.find_all('tr'):
            cells = tr.findChildren('td')
            for i in range(0, len(cells)):
                data = {}
                data['Chung_khoan_name'] =  cells[0].find_all(['a'], recursive=False)[0].string
                data['San_giao_dich'] = cells[1].string
                data['Nganh'] = cells[2].string
                yield data
                break

        next_page =  response.meta["currentPage"] + 1
        if response.meta["currentPage"] <= 20:
            try:
                yield FormRequest('https://finance.tvsi.com.vn/tools/topCompanyPart',
                                  method="POST",
                                  callback= self.parse_top_company,
                                  body= 'adata=0&adata=1&adata=2&adata=3&adata=12&adata=13&adata=18&adata=21&adata=23&adata=24&adata=36&adata=38&adata=50&adata=59&adata=62&adata=76&currentPage={}&exchange=&industryId=0&pageSize=100&SortKeyArr=MarketCap&SortDirectionArr=1&check=true&check_Cookie_Top=0'.format(next_page),
                                  headers= {
                                      "X-Requested-With": "XMLHttpRequest",
                                      "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                      'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
                                      "User-Agent":  random.choice(settings.get('USER_AGENT_LIST')),
                                  },
                                  meta= {
                                      "currentPage": next_page
                                  }
                              )
            except:
                pass