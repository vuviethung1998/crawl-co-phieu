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

        self.lst_cp = HOSE + HNX + UPCOM

        self.start_urls = ['https://s.cafef.vn']
        settings['CRAWLER_COLLECTION'] = 'THONG_KE_DAT_LENH'

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, callback=self.parse, meta={
                "ck_index" : 0,
                "page_number": 21
            })

    def parse(self, response):
        ck_index = response.meta["ck_index"]
        page_number = response.meta['page_number']

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
                                  "Cookie":  '__IP=2885510353;',
                                  "X-MicrosoftAjax": "Delta=true"
                              },
                              meta= {
                                  "ck_name": self.lst_cp[ck_index],
                                  "ck_index": ck_index,
                                  "page_number": page_number
                              }
                          )


    def thong_ke_dat_lenh(self, response):
        ck_index =  response.meta["ck_index"]
        page_number = response.meta["page_number"]

        thong_ke_dat_lenh = response.text
        s = soup(thong_ke_dat_lenh, features='lxml').table
        start = 0
        for tr in s.find_all('tr', recursive=False):
            if start >= 1:
                data = {}
                data['Chung_khoan_name'] = self.lst_cp[ck_index]
                if self.lst_cp[ck_index] in HOSE:
                    data['San Chung Khoan'] = 'HOSE'
                elif self.lst_cp[ck_index] in HNX:
                    data['San Chung Khoan'] = 'HNX'
                else:
                    data['San Chung Khoan'] = 'UPCOM'
                for i, td in enumerate(tr.find_all('td', recursive=False)):
                    if i % 9 == 0:
                        data['Ngày'] =  td.text.replace(u'\xa0', u'')
                    elif i % 9 == 1:
                        try:
                            data['Thay Đổi'] = float(td.text.split('(')[0])
                            data["Thay Đổi Theo %"] = float(td.text.split('(')[1].strip()[:-2])
                        except:
                            data['Thay Đổi'] =  0
                            data["Thay Đổi Theo %"] = 0
                    elif i % 9 == 2:
                        try:
                            data['Số lệnh mua Khớp Lệnh'] =   int(td.text.replace(u'\xa0', u'').replace(',', ''))
                        except:
                            data['Số lệnh mua Khớp Lệnh'] = 0
                    elif i % 9 == 3:
                        try:
                            data['Khối lượng đặt mua Khớp Lệnh'] = int(td.text.replace(u'\xa0', u'').replace(',', ''))
                        except:
                            data['Khối lượng đặt mua Khớp Lệnh']  = 0
                    elif i % 9 == 4:
                        try:
                            data['KLTB 1 lệnh mua Khớp Lệnh'] =  int(td.text.replace(u'\xa0', u'').replace(',', ''))
                        except:
                            data['KLTB 1 lệnh mua Khớp Lệnh'] = 0
                    elif i % 9 == 5:
                        try:
                            data['Số lệnh bán Khớp Lệnh'] =   int(td.text.replace(u'\xa0', u'').replace(',', ''))
                        except:
                            data['Số lệnh bán Khớp Lệnh'] = 0
                    elif i % 9 == 6:
                        try:
                            data['Khối lượng đặt bán Khớp Lệnh'] = int(td.text.replace(u'\xa0', u'').replace(',', ''))
                        except:
                            data['Khối lượng đặt bán Khớp Lệnh'] = 0
                    elif i % 9 == 7:
                        try:
                            data['KLTB 1 lệnh bán Khớp Lệnh'] =  int(td.text.replace(u'\xa0', u'').replace(',', ''))
                        except:
                            data['KLTB 1 lệnh bán Khớp Lệnh'] = 0
                    elif i % 9 == 8:
                        try:
                            data['Chênh lệch KL đặt mua - đặt bán'] =  int(td.text.replace(u'\xa0', u'').replace(',', ''))
                        except:
                            data['Chênh lệch KL đặt mua - đặt bán'] = 0
                print(data)
                yield data
            start += 1

        # quay lai parse

        if response.meta["page_number"] < 10:
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
                                      "X-MicrosoftAjax": "Delta=true"
                                  },
                                  meta= {
                                      "ck_name": self.lst_cp[ck_index],
                                      "ck_index": ck_index,
                                      "page_number": page_number + 1
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
                                      "Cookie":  '__IP=2885510353;',
                                      "X-MicrosoftAjax": "Delta=true"
                                  },
                                  meta= {
                                      "ck_name": self.lst_cp[ck_index+ 1],
                                      "ck_index": ck_index + 1,
                                      "page_number": 1
                                  }
                              )
            except:
                pass
