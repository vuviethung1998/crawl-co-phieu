import json
from scrapy.spiders import CrawlSpider
from scrapy import Request, FormRequest
import random
from crawl_cp_cafef.import_setting import *
from crawl_cp_cafef.config.ListStock import *
from bs4 import BeautifulSoup as soup

class CafefLichSuGiaoDichSpider(CrawlSpider):
    name = "cafef_lich_su_giao_dich"

    def __init__(self, **kwargs):
        super(CafefLichSuGiaoDichSpider, self).__init__(**kwargs)
        self.allowed_domains = ['cafef.vn']

        self.lst_cp = HOSE + HNX + UPCOM

        self.start_urls = ['https://s.cafef.vn']
        settings['CRAWLER_COLLECTION'] = 'LICH_SU_GIAO_DICH'

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, callback=self.parse, meta={
                "ck_index" : 0,
                "page_number": 1
            })

    def parse(self, response):
        # ASP_sessionId = response.headers.getlist('Set-Cookie')[0].decode("utf-8").split(";")[0]
        # print(ASP_sessionId)
        ck_index = response.meta["ck_index"]
        page_number = response.meta['page_number']
        print(self.lst_cp[ck_index])

        # ReportTermType: 2 -> month
        # ReportTermType: 1 -> year
        yield Request('https://s.cafef.vn/Lich-su-giao-dich-VIC-1.chn',
                              method="POST",
                              callback= self.parse_lich_su_giao_dich,
                              body="ctl00%24ContentPlaceHolder1%24scriptmanager=ctl00%24ContentPlaceHolder1%24ctl03%24panelAjax%7Cctl00%24ContentPlaceHolder1%24ctl03%24pager2&__EVENTTARGET=ctl00%24ContentPlaceHolder1%24ctl03%24pager2&__EVENTARGUMENT={}&__VIEWSTATE=%2FwEPDwUKMTU2NzY0ODUyMGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFKGN0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkY3RsMDMkYnRTZWFyY2jJnyPYjjwDsOatyCQBZar0ZSQygQ%3D%3D&ctl00%24ContentPlaceHolder1%24ctl03%24txtKeyword={}&ctl00%24ContentPlaceHolder1%24ctl03%24dpkTradeDate1%24txtDatePicker=&ctl00%24ContentPlaceHolder1%24ctl03%24dpkTradeDate2%24txtDatePicker=&ctl00%24UcFooter2%24hdIP=&__VIEWSTATEGENERATOR=2E2252AF&__ASYNCPOST=true&".format(page_number, self.lst_cp[ck_index]),
                              headers= {
                                  "X-Requested-With": "XMLHttpRequest",
                                  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                  'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
                                  "User-Agent":  random.choice(settings.get('USER_AGENT_LIST')),
                                  "Cookie":  '__IP=2885510353;',
                                  "X-MicrosoftAjax": "Delta=true"
                              },
                              meta= {
                                  "ck_name": self.lst_cp[ck_index],
                                  "ck_index": ck_index,
                                  "page_number": page_number,
                                  # "ASP_sessionId": ASP_sessionId
                              }
                          )

    def parse_lich_su_giao_dich(self, response):
        # ASP_sessionId = response.meta["ASP_sessionId"]
        ck_index =  response.meta["ck_index"]
        page_number = response.meta["page_number"]

        lich_su_giao_dich = response.text
        print("----------------" + lich_su_giao_dich)
        s = soup(lich_su_giao_dich, features='lxml').table
        start = 0
        for tr in s.find_all('tr', recursive=False):
            if start > 1:
                data = {}
                data['Chung_khoan_name'] = self.lst_cp[ck_index]
                if self.lst_cp[ck_index] in HOSE:
                    data['San Chung Khoan'] = 'HOSE'
                elif self.lst_cp[ck_index] in HNX:
                    data['San Chung Khoan'] = 'HNX'
                else:
                    data['San Chung Khoan'] = 'UPCOM'
                for i, td in enumerate(tr.find_all('td', recursive=False)):
                    if i % 15 == 0:
                        data['Ngày'] =  td.text.replace(u'\xa0', u'')
                    elif i % 15 == 1:
                        try:
                            data['Giá Điều Chỉnh'] =  float(td.text.replace(u'\xa0', u''))
                        except:
                            data['Giá Điều Chỉnh'] = 0
                    elif i % 15 == 2:
                        try:
                            data['Giá Đóng Cửa'] =  float(td.text.replace(u'\xa0', u''))
                        except:
                            data['Giá Điều Chỉnh'] = 0
                    elif i % 15 == 3:
                        try:
                            txt = td.text.replace(u'\xa0', u'').replace(',', '')
                            data['Thay Đổi'] = float(txt.split('(')[0])
                            data["Thay Đổi Theo %"] = float(txt.split('(')[1].strip()[:-2])
                        except:
                            data['Thay Đổi'] = 0
                            data["Thay Đổi Theo %"] = 0
                    elif i % 15 == 5:
                        try:
                            data['KL GD Khớp Lệnh'] =  int(td.text.replace(u'\xa0', u'').replace(',', ''))
                        except:
                            data['KL GD Khớp Lệnh']  =0
                    elif i % 15 == 6:
                        try:
                            data['GT GD Khớp Lệnh'] =  int(td.text.replace(u'\xa0', u'').replace(',', ''))
                        except:
                            data['GT GD Khớp Lệnh']  = 0
                    elif i % 15 == 7:
                        try:
                            data['KL GD Thỏa Thuận'] =  int(td.text.replace(u'\xa0', u'').replace(',', ''))
                        except:
                            data['KL GD Thỏa Thuận'] = 0
                    elif i % 15 == 8:
                        try:
                            data['GT GD Thỏa Thuận'] =  int(td.text.replace(u'\xa0', u'').replace(',', ''))
                        except:
                            data['GT GD Thỏa Thuận'] = 0
                    # elif i % 15 == 9:
                    #     try:
                    #         data['Giá Mở Cửa'] =  float(td.text.replace(u'\xa0', u''))
                    #     except:
                    #         data['Giá Mở Cửa'] = 0
                    elif i % 15 == 10:
                        try:
                            data['Giá Cao Nhất'] =  float(td.text.replace(u'\xa0', u''))
                        except:
                            data['Giá Cao Nhất'] = 0
                    elif i % 15 == 11:
                        try:
                            data['Giá Thấp Nhất'] =  float(td.text.replace(u'\xa0', u''))
                        except:
                            data['Giá Thấp Nhất'] = 0
                data['Giá Mở Cửa'] =  data['Giá Đóng Cửa'] - data['Thay Đổi']
                # print(data)
                yield data

            start += 1

        # quay lai parse

        if response.meta["page_number"] < 10:
            try:
                yield Request('https://s.cafef.vn/Lich-su-giao-dich-VIC-1.chn',
                                  method="POST",
                                  callback= self.parse_lich_su_giao_dich,
                                  body="ctl00%24ContentPlaceHolder1%24scriptmanager=ctl00%24ContentPlaceHolder1%24ctl03%24panelAjax%7Cctl00%24ContentPlaceHolder1%24ctl03%24pager2&__EVENTTARGET=ctl00%24ContentPlaceHolder1%24ctl03%24pager2&__EVENTARGUMENT={}&__VIEWSTATE=%2FwEPDwUKMTU2NzY0ODUyMGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFKGN0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkY3RsMDMkYnRTZWFyY2jJnyPYjjwDsOatyCQBZar0ZSQygQ%3D%3D&ctl00%24ContentPlaceHolder1%24ctl03%24txtKeyword={}&ctl00%24ContentPlaceHolder1%24ctl03%24dpkTradeDate1%24txtDatePicker=&ctl00%24ContentPlaceHolder1%24ctl03%24dpkTradeDate2%24txtDatePicker=&ctl00%24UcFooter2%24hdIP=&__VIEWSTATEGENERATOR=2E2252AF&__ASYNCPOST=true&".format(page_number+1, self.lst_cp[ck_index]),
                                  headers= {
                                      "X-Requested-With": "XMLHttpRequest",
                                      "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                      'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
                                      "User-Agent":  random.choice(settings.get('USER_AGENT_LIST')),
                                      "Cookie":  "__IP=2885510353;",
                                      "X-MicrosoftAjax": "Delta=true"
                                  },
                                  meta= {
                                      "ck_name": self.lst_cp[ck_index],
                                      "ck_index": ck_index,
                                      # "ASP_sessionId": ASP_sessionId,
                                      "page_number": page_number + 1,
                                  }
                              )

            except:
                pass
        else:
            try:
                yield Request('https://s.cafef.vn/Lich-su-giao-dich-VIC-1.chn',
                                  method="POST",
                                  callback= self.parse_lich_su_giao_dich,
                                  body="ctl00%24ContentPlaceHolder1%24scriptmanager=ctl00%24ContentPlaceHolder1%24ctl03%24panelAjax%7Cctl00%24ContentPlaceHolder1%24ctl03%24pager2&__EVENTTARGET=ctl00%24ContentPlaceHolder1%24ctl03%24pager2&__EVENTARGUMENT={}&__VIEWSTATE=%2FwEPDwUKMTU2NzY0ODUyMGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFKGN0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkY3RsMDMkYnRTZWFyY2jJnyPYjjwDsOatyCQBZar0ZSQygQ%3D%3D&ctl00%24ContentPlaceHolder1%24ctl03%24txtKeyword={}&ctl00%24ContentPlaceHolder1%24ctl03%24dpkTradeDate1%24txtDatePicker=&ctl00%24ContentPlaceHolder1%24ctl03%24dpkTradeDate2%24txtDatePicker=&ctl00%24UcFooter2%24hdIP=&__VIEWSTATEGENERATOR=2E2252AF&__ASYNCPOST=true&".format(1, self.lst_cp[ck_index+1]),
                                  headers= {
                                      "X-Requested-With": "XMLHttpRequest",
                                      "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                      'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
                                      "User-Agent":  random.choice(settings.get('USER_AGENT_LIST')),
                                      "Cookie":  "__IP=2885510353;",
                                      "X-MicrosoftAjax": "Delta=true"
                                  },
                                  meta= {
                                      "ck_name": self.lst_cp[ck_index+1],
                                      "ck_index": ck_index+1,
                                      # "ASP_sessionId": ASP_sessionId,
                                      "page_number": 1,
                                  }
                              )
            except:
                pass