import json
from scrapy.spiders import CrawlSpider
from scrapy import Request, FormRequest
import random
from crawl_cp_cafef.import_setting import *
from crawl_cp_cafef.config.ListStock import *
from bs4 import BeautifulSoup as soup

class CafefLichSuGiaoDichSpider(CrawlSpider):
    name = "cafef_giao_dich_khoi_ngoai"

    def __init__(self, **kwargs):
        super(CafefLichSuGiaoDichSpider, self).__init__(**kwargs)
        self.allowed_domains = ['cafef.vn']

        self.lst_cp = HOSE + HNX

        self.start_urls = ['https://s.cafef.vn']
        settings['CRAWLER_COLLECTION'] = 'GIAO_DICH_KHOI_NGOAI'

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, callback=self.parse, meta={
                "ck_index" : 0,
                "page_number": 1
            })

    def parse(self, response):
        ASP_sessionId = response.headers.getlist('Set-Cookie')[0].decode("utf-8").split(";")[0]
        print(ASP_sessionId)
        ck_index = response.meta["ck_index"]
        page_number = response.meta['page_number']
        print(self.lst_cp[ck_index])

        # ReportTermType: 2 -> month
        # ReportTermType: 1 -> year
        yield Request('https://s.cafef.vn/Lich-su-giao-dich-VIC-3.chn',
                          method="POST",
                          callback= self.parse_giao_dich_khoi_ngoai,
                          body="ctl00%24ContentPlaceHolder1%24scriptmanager=ctl00%24ContentPlaceHolder1%24ctl03%24panelAjax%7Cctl00%24ContentPlaceHolder1%24ctl03%24pager1&ctl00%24ContentPlaceHolder1%24ctl03%24txtKeyword={}&ctl00%24ContentPlaceHolder1%24ctl03%24dpkTradeDate1%24txtDatePicker=&ctl00%24ContentPlaceHolder1%24ctl03%24dpkTradeDate2%24txtDatePicker=&ctl00%24UcFooter2%24hdIP=&__EVENTTARGET=ctl00%24ContentPlaceHolder1%24ctl03%24pager1&__EVENTARGUMENT={}&__VIEWSTATE=%2FwEPDwUKMTU2NzY0ODUyMGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFKGN0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkY3RsMDMkYnRTZWFyY2jJnyPYjjwDsOatyCQBZar0ZSQygQ%3D%3D&__VIEWSTATEGENERATOR=2E2252AF&__ASYNCPOST=true&".format(self.lst_cp[ck_index], page_number),
                          headers= {
                              "X-Requested-With": "XMLHttpRequest",
                              "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                              'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
                              "User-Agent":  random.choice(settings.get('USER_AGENT_LIST')),
                              "Cookie":  ASP_sessionId,
                              "X-MicrosoftAjax": "Delta=true"
                          },
                          meta= {
                              "ck_name": self.lst_cp[ck_index],
                              "ck_index": ck_index,
                              "page_number": page_number,
                              "ASP_sessionId": ASP_sessionId
                          }
                      )


    def parse_giao_dich_khoi_ngoai(self, response):
        ASP_sessionId = response.meta["ASP_sessionId"]
        ck_index =  response.meta["ck_index"]
        page_number = response.meta["page_number"]

        giao_dich_khoi_ngoai = response.text
        s = soup(giao_dich_khoi_ngoai, features='lxml').table
        start = 0
        for tr in s.find_all('tr', recursive=False):
            if start > 1:
                data = {}
                data['Chung_khoan_name'] = self.lst_cp[ck_index]
                for i, td in enumerate(tr.find_all('td', recursive=False)):
                    if i % 10 == 0:
                        data['Ngày'] =  td.text.replace(u'\xa0', u'')
                    elif i % 10 == 1:
                        try:
                            data['KL Giao Dịch Ròng Khối Ngoại'] =   int(td.text.replace(u'\xa0', u'').replace(',', ''))
                        except:
                            data['KL Giao Dịch Ròng Khối Ngoại'] =   0
                    elif i % 10 == 2:
                        try:
                            data['KL Giao Dịch Ròng Khối Ngoại'] =   int(td.text.replace(u'\xa0', u'').replace(',', ''))
                        except:
                            data['GT Giao Dịch Ròng Khối Ngoại'] = 0
                    elif i % 10 == 3:
                        try:
                            data['Thay Đổi'] = float(td.text.split('(')[0])
                            data["Thay Đổi Theo %"] = float(td.text.split('(')[1].strip()[:-2])
                        except:
                            data['Thay Đổi'] =  0
                            data["Thay Đổi Theo %"] = 0
                    elif i % 10 == 4:
                        try:
                            data['KL đặt mua khối ngoại'] =  int(td.text.replace(u'\xa0', u'').replace(',', ''))
                        except:
                            data['KL đặt mua khối ngoại'] = 0
                    elif i % 10 == 5:
                        try:
                            data['GT đặt mua khối ngoại'] =   int(td.text.replace(u'\xa0', u'').replace(',', ''))
                        except:
                            data['GT đặt mua khối ngoại'] = 0
                    elif i % 10 == 6:
                        try:
                            data['KL đặt bán khối ngoại'] = int(td.text.replace(u'\xa0', u'').replace(',', ''))
                        except:
                            data['KL đặt bán khối ngoại'] = 0
                    elif i % 10 == 7:
                        try:
                            data['GT đặt bán khối ngoại'] =  int(td.text.replace(u'\xa0', u'').replace(',', ''))
                        except:
                            data['GT đặt bán khối ngoại'] = 0
                    elif i % 10 == 8:
                        try:
                            data['Room còn lại'] =  int(td.text.replace(u'\xa0', u'').replace(',', ''))
                        except:
                            data['Room còn lại'] = 0
                    elif i % 10 == 9:
                        try:
                            data['Room đang sở hữu'] =  float(td.text.replace(u'\xa0', u'').strip()[:-1])
                        except:
                            data['Room còn lại'] = 0
                yield data
            start += 1

        # quay lai parse

        if response.meta["page_number"] <= 2:
            try:
                yield Request('https://s.cafef.vn/Lich-su-giao-dich-VIC-3.chn',
                                  method="POST",
                                  callback= self.parse_giao_dich_khoi_ngoai,
                                  body="ctl00%24ContentPlaceHolder1%24scriptmanager=ctl00%24ContentPlaceHolder1%24ctl03%24panelAjax%7Cctl00%24ContentPlaceHolder1%24ctl03%24pager1&ctl00%24ContentPlaceHolder1%24ctl03%24txtKeyword={}&ctl00%24ContentPlaceHolder1%24ctl03%24dpkTradeDate1%24txtDatePicker=&ctl00%24ContentPlaceHolder1%24ctl03%24dpkTradeDate2%24txtDatePicker=&ctl00%24UcFooter2%24hdIP=&__EVENTTARGET=ctl00%24ContentPlaceHolder1%24ctl03%24pager1&__EVENTARGUMENT={}&__VIEWSTATE=%2FwEPDwUKMTU2NzY0ODUyMGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFKGN0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkY3RsMDMkYnRTZWFyY2jJnyPYjjwDsOatyCQBZar0ZSQygQ%3D%3D&__VIEWSTATEGENERATOR=2E2252AF&__ASYNCPOST=true&".format(self.lst_cp[ck_index], page_number+1),
                                  headers= {
                                      "X-Requested-With": "XMLHttpRequest",
                                      "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                      'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
                                      "User-Agent":  random.choice(settings.get('USER_AGENT_LIST')),
                                      "Cookie":  ASP_sessionId,
                                      "X-MicrosoftAjax": "Delta=true"
                                  },
                                  meta= {
                                      "ck_name": self.lst_cp[ck_index],
                                      "ck_index": ck_index,
                                      "page_number": page_number+1,
                                      "ASP_sessionId": ASP_sessionId
                                  }
                              )


            except:
                pass
        else:
            try:
                yield Request('https://s.cafef.vn/Lich-su-giao-dich-VIC-3.chn',
                                  method="POST",
                                  callback= self.parse_giao_dich_khoi_ngoai,
                                  body="ctl00%24ContentPlaceHolder1%24scriptmanager=ctl00%24ContentPlaceHolder1%24ctl03%24panelAjax%7Cctl00%24ContentPlaceHolder1%24ctl03%24pager1&ctl00%24ContentPlaceHolder1%24ctl03%24txtKeyword={}&ctl00%24ContentPlaceHolder1%24ctl03%24dpkTradeDate1%24txtDatePicker=&ctl00%24ContentPlaceHolder1%24ctl03%24dpkTradeDate2%24txtDatePicker=&ctl00%24UcFooter2%24hdIP=&__EVENTTARGET=ctl00%24ContentPlaceHolder1%24ctl03%24pager1&__EVENTARGUMENT={}&__VIEWSTATE=%2FwEPDwUKMTU2NzY0ODUyMGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFKGN0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkY3RsMDMkYnRTZWFyY2jJnyPYjjwDsOatyCQBZar0ZSQygQ%3D%3D&__VIEWSTATEGENERATOR=2E2252AF&__ASYNCPOST=true&".format(self.lst_cp[ck_index+1], 1),
                                  headers= {
                                      "X-Requested-With": "XMLHttpRequest",
                                      "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                      'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
                                      "User-Agent":  random.choice(settings.get('USER_AGENT_LIST')),
                                      "Cookie":  ASP_sessionId,
                                      "X-MicrosoftAjax": "Delta=true"
                                  },
                                  meta= {
                                      "ck_name": self.lst_cp[ck_index+1],
                                      "ck_index": ck_index+1,
                                      "page_number": 1,
                                      "ASP_sessionId": ASP_sessionId
                                  }
                              )
            except:
                pass
