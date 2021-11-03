import json
from scrapy.spiders import CrawlSpider
from scrapy import Request, FormRequest
import random
from crawl_cp_finance_stock.import_setting import *


class FinanceStockNhomNganhSpider(CrawlSpider):
    name = "finance_stock_nhom_nganh_spider"

    def __init__(self, **kwargs):
        super(FinanceStockNhomNganhSpider, self).__init__(**kwargs)
        self.allowed_domains = ['finance.vietstock.vn']

        self.start_urls = ['https://finance.vietstock.vn']
        settings['CRAWLER_COLLECTION'] = "NHOM_NGANH"

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, callback=self.parse, meta={
                "page_number": 1
            })

    def parse(self, response):
        isShowLogin = "isShowLogin=true"
        language =  response.headers.getlist('Set-Cookie')[0].decode("utf-8").split(";")[0]
        ASP_sessionId = response.headers.getlist('Set-Cookie')[1].decode("utf-8").split(";")[0]
        verifyToken =  response.headers.getlist('Set-Cookie')[4].decode("utf-8").split(";")[0]
        vts_usr_lg="25D50954A6867904662F0ADCCB0A07EC40673FD525967167788F119BFDC80751185C7B0B0F82A5F1AF77DDDD67F165C9DFD64D7E63EC7B478F4789FC47436901499764F120C1A36115D7D9CA6327E1D7A565C2C5CB788F86ACAF8E1F6A227F0EEA810A835E5A522DB1E080FE6DA53C7E2809CE0AFBF22313B120251676C9D9EBFFB9B46C6C628A4EB40CFF4B1FAF8759"

        page_number = response.meta['page_number']

        yield FormRequest('https://finance.vietstock.vn/data/corporateaz',
                              method="POST",
                              callback= self.parse_bao_cao,
                              formdata={
                                  "catID" : "0",
                                  "industryID": "0",
                                  "type": "0",
                                  "code": "",
                                  "businessTypeID": "0",
                                  "orderBy": "Code",
                                  "orderDir": "ASC",
                                  "page": str(page_number),
                                  "pageSize": "100"
                              },
                              headers= {
                                  "X-Requested-With": "XMLHttpRequest",
                                  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                  'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
                                  "User-Agent":  random.choice(settings.get('USER_AGENT_LIST')),
                                  "Cookie": "language=vi-VN; isShowLogin=true;  ASP.NET_SessionId=rywvhzyai4ffxqkne4crvlje; __RequestVerificationToken=cC6zL47mdjaUyeLGF-VH3hAI-gdTK92KyZ1bwwWNdCmfDjhG9x0vetRKFqePiHHtYRloTdynYukg_XZNO0cc25_L8jYkN2aDOsGJpyr2sRo1; vts_usr_lg={};".format(vts_usr_lg)
                              },
                              meta= {
                                  "page_number": page_number,
                                  "isShowLogin": isShowLogin,
                                  "language": language,
                                  "ASP_sessionId": ASP_sessionId,
                                  "verifyToken": verifyToken,
                                  "vts_usr_lg": vts_usr_lg
                              }
                          )


    def parse_bao_cao(self, response):
        page_number=  response.meta["page_number"]
        isShowLogin = response.meta["isShowLogin"]
        language =  response.meta["language"]
        ASP_sessionId = response.meta["ASP_sessionId"]
        verifyToken = response.meta["verifyToken"]
        vts_usr_lg = response.meta["vts_usr_lg"]

        # quay lai parse
        # neu page_number < 7 thi chuyen trang
        # neu page_number > 7 thi chuyen co phieu

        resp  = json.loads(response.body)
        print("------------------------------------")
        print(resp)

        for it in resp:
            obj = {}
            obj["ID"] = it["ID"]
            obj['Chung_khoan_code'] = it["Code"]
            obj['Chung_khoan_name'] = it["Name"]
            obj['Exchange'] = it["Exchange"]
            obj['IndustryName'] = it["IndustryName"]
            obj["TotalShares"] = it["TotalShares"]
            yield  obj

        if response.meta["page_number"] <= 33:
            try:
                yield FormRequest('https://finance.vietstock.vn/data/corporateaz',
                                      method="POST",
                                      callback= self.parse_bao_cao,
                                      formdata={
                                          "catID" : "0",
                                          "industryID": "0",
                                          "type": "0",
                                          "code": "",
                                          "businessTypeID": "0",
                                          "orderBy": "Code",
                                          "orderDir": "ASC",
                                          "page":  str(page_number+1),
                                          "pageSize": "100"
                                      },
                                      headers= {
                                          "X-Requested-With": "XMLHttpRequest",
                                          "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                          'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
                                          "User-Agent":  random.choice(settings.get('USER_AGENT_LIST')),
                                          "Cookie": "language=vi-VN; isShowLogin=true;  ASP.NET_SessionId={}; __RequestVerificationToken={}; vts_usr_lg={};".format(ASP_sessionId, verifyToken,vts_usr_lg)
                                      },
                                      meta= {
                                          "page_number": page_number+1,
                                          "isShowLogin": isShowLogin,
                                          "language": language,
                                          "ASP_sessionId": ASP_sessionId,
                                          "verifyToken": verifyToken,
                                          "vts_usr_lg" : vts_usr_lg
                                      }
                                  )
            except:
                pass
        else:
            try:
                yield FormRequest('https://finance.vietstock.vn/data/corporateaz',
                                      method="POST",
                                      callback= self.parse_bao_cao,
                                      formdata={
                                          "catID" : "0",
                                          "industryID": "0",
                                          "type": "0",
                                          "code": "",
                                          "businessTypeID": "0",
                                          "orderBy": "Code",
                                          "orderDir": "ASC",
                                          "page":  "1",
                                          "pageSize": "100"
                                      },
                                      headers= {
                                          "X-Requested-With": "XMLHttpRequest",
                                          "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                          'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
                                          "User-Agent":  random.choice(settings.get('USER_AGENT_LIST')),
                                          "Cookie": "language=vi-VN; isShowLogin=true;  ASP.NET_SessionId={}; __RequestVerificationToken={}; vts_usr_lg={};".format(ASP_sessionId, verifyToken,vts_usr_lg)
                                      },
                                      meta= {
                                          "page_number": page_number+1,
                                          "isShowLogin": isShowLogin,
                                          "language": language,
                                          "ASP_sessionId": ASP_sessionId,
                                          "verifyToken": verifyToken,
                                          "vts_usr_lg": vts_usr_lg
                                      }
                                  )
            except:
                pass