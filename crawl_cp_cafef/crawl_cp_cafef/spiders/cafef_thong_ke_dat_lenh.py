import json
from scrapy.spiders import CrawlSpider
from scrapy import Request, FormRequest
import random
from crawl_cp_cafef.import_setting import *
from crawl_cp_cafef.config.ListStock import *
from bs4 import BeautifulSoup as soup

class CafefLichSuGiaoDichSpider(CrawlSpider):
    name = "cafef_thong_ke_dat_lenh"

    def __init__(self, **kwargs):
        super(CafefLichSuGiaoDichSpider, self).__init__(**kwargs)
        self.allowed_domains = ['cafef.vn']

        self.lst_cp = VN30 + HNX30

        self.start_urls = ['https://s.cafef.vn']
        settings['CRAWLER_COLLECTION'] = 'THONG_KE_DAT_LENH'

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
        yield Request('https://s.cafef.vn/Lich-su-giao-dich-VIC-2.chn',
                              method="POST",
                              callback= self.thong_ke_dat_lenh,
                              body="ctl00%24ContentPlaceHolder1%24scriptmanager=ctl00%24ContentPlaceHolder1%24ctl03%24panelAjax%7Cctl00%24ContentPlaceHolder1%24ctl03%24pager1&__EVENTTARGET=ctl00%24ContentPlaceHolder1%24ctl03%24pager1&__EVENTARGUMENT={}&__VIEWSTATE=%2FwEPDwUKMTU2NzY0ODUyMGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFKGN0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkY3RsMDMkYnRTZWFyY2jJnyPYjjwDsOatyCQBZar0ZSQygQ%3D%3D&ctl00%24ContentPlaceHolder1%24ctl03%24txtKeyword={}&ctl00%24ContentPlaceHolder1%24ctl03%24dpkTradeDate1%24txtDatePicker=&ctl00%24ContentPlaceHolder1%24ctl03%24dpkTradeDate2%24txtDatePicker=&ctl00%24UcFooter2%24hdIP=&__VIEWSTATEGENERATOR=2E2252AF&__ASYNCPOST=true&".format(page_number, self.lst_cp[ck_index]),
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

    def thong_ke_dat_lenh(self, response):
        ASP_sessionId = response.meta["ASP_sessionId"]
        ck_index =  response.meta["ck_index"]
        page_number = response.meta["page_number"]

        thong_ke_dat_lenh = response.text
        s = soup(thong_ke_dat_lenh, features='lxml').table
        start = 0
        for tr in s.find_all('tr', recursive=False):
            if start >= 1:
                data = {}
                for i, td in enumerate(tr.find_all('td', recursive=False)):
                    if i % 9 == 0:
                        data['Ngày'] =  td.text.replace(u'\xa0', u'')
                    elif i % 9 == 1:
                        data['Thay Đổi'] = float(td.text.split('(')[0])
                        data["Thay Đổi Theo %"] = float(td.text.split('(')[1].strip()[:-2])
                    elif i % 9 == 2:
                        data['Số lệnh mua'] =   int(td.text.replace(u'\xa0', u'').replace(',', ''))
                    elif i % 9 == 3:
                        data['Khối lượng đặt mua'] = int(td.text.replace(u'\xa0', u'').replace(',', ''))
                    elif i % 9 == 4:
                        data['KLTB 1 lệnh mua'] =  int(td.text.replace(u'\xa0', u'').replace(',', ''))
                    elif i % 9 == 5:
                        data['Số lệnh bán'] =   int(td.text.replace(u'\xa0', u'').replace(',', ''))
                    elif i % 9 == 6:
                        data['Khối lượng đặt bán'] = int(td.text.replace(u'\xa0', u'').replace(',', ''))
                    elif i % 9 == 7:
                        data['KLTB 1 lệnh bán'] =  int(td.text.replace(u'\xa0', u'').replace(',', ''))
                    elif i % 9 == 8:
                        data['Chênh lệch KL đặt mua - đặt bán'] =  int(td.text.replace(u'\xa0', u'').replace(',', ''))
                yield data
            start += 1

        # quay lai parse

        if response.meta["page_number"] <= 80:
            try:
                yield Request('https://s.cafef.vn/Lich-su-giao-dich-VIC-2.chn',
                                  method="POST",
                                  callback= self.thong_ke_dat_lenh,
                                  body="ctl00%24ContentPlaceHolder1%24scriptmanager=ctl00%24ContentPlaceHolder1%24ctl03%24panelAjax%7Cctl00%24ContentPlaceHolder1%24ctl03%24pager1&__EVENTTARGET=ctl00%24ContentPlaceHolder1%24ctl03%24pager1&__EVENTARGUMENT={}&__VIEWSTATE=%2FwEPDwUKMTU2NzY0ODUyMGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFKGN0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkY3RsMDMkYnRTZWFyY2jJnyPYjjwDsOatyCQBZar0ZSQygQ%3D%3D&ctl00%24ContentPlaceHolder1%24ctl03%24txtKeyword={}&ctl00%24ContentPlaceHolder1%24ctl03%24dpkTradeDate1%24txtDatePicker=&ctl00%24ContentPlaceHolder1%24ctl03%24dpkTradeDate2%24txtDatePicker=&ctl00%24UcFooter2%24hdIP=&__VIEWSTATEGENERATOR=2E2252AF&__ASYNCPOST=true&".format(page_number+1, self.lst_cp[ck_index]),
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
                                      "page_number": page_number + 1,
                                      "ASP_sessionId": ASP_sessionId
                                  }
                              )


            except:
                pass
        else:
            try:
                yield Request('https://s.cafef.vn/Lich-su-giao-dich-VIC-2.chn',
                                  method="POST",
                                  callback= self.thong_ke_dat_lenh,
                                  body="ctl00%24ContentPlaceHolder1%24scriptmanager=ctl00%24ContentPlaceHolder1%24ctl03%24panelAjax%7Cctl00%24ContentPlaceHolder1%24ctl03%24pager1&__EVENTTARGET=ctl00%24ContentPlaceHolder1%24ctl03%24pager1&__EVENTARGUMENT={}&__VIEWSTATE=%2FwEPDwUKMTU2NzY0ODUyMGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFKGN0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkY3RsMDMkYnRTZWFyY2jJnyPYjjwDsOatyCQBZar0ZSQygQ%3D%3D&ctl00%24ContentPlaceHolder1%24ctl03%24txtKeyword={}&ctl00%24ContentPlaceHolder1%24ctl03%24dpkTradeDate1%24txtDatePicker=&ctl00%24ContentPlaceHolder1%24ctl03%24dpkTradeDate2%24txtDatePicker=&ctl00%24UcFooter2%24hdIP=&__VIEWSTATEGENERATOR=2E2252AF&__ASYNCPOST=true&".format(1, self.lst_cp[ck_index+1]),
                                  headers= {
                                      "X-Requested-With": "XMLHttpRequest",
                                      "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                      'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
                                      "User-Agent":  random.choice(settings.get('USER_AGENT_LIST')),
                                      "Cookie":  ASP_sessionId,
                                      "X-MicrosoftAjax": "Delta=true"
                                  },
                                  meta= {
                                      "ck_name": self.lst_cp[ck_index+ 1],
                                      "ck_index": ck_index + 1,
                                      "page_number": 1,
                                      "ASP_sessionId": ASP_sessionId
                                  }
                              )
            except:
                pass