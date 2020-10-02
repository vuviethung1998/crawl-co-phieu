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
        vts_usr_lg="93074A90D244461C383BBFE9EB4D475015C158ADC7C6CCF075E44C9654E4377A94F1A704C5F67B650E8482B3E1EB1612415557C39A61B6372E821969994DA7DDB46514ABCA15A3CB3C08F9EE9382AD7A28CF4E106308C2E4863C7A6D8A2F7D4FDD4B2A27DA32104F0D8F796836733F21AABC3D72BA8457746549A7EE8FA6F4A5451E03CC55A3703D2D55A40DB56E5D2E"

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
                                  "pageSize": "20"
                              },
                              headers= {
                                  "X-Requested-With": "XMLHttpRequest",
                                  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                  'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
                                  "User-Agent":  random.choice(settings.get('USER_AGENT_LIST')),
                                  "Cookie": "language=vi-VN; isShowLogin=true;  ASP.NET_SessionId=rywvhzyai4ffxqkne4crvlje; __RequestVerificationToken=cC6zL47mdjaUyeLGF-VH3hAI-gdTK92KyZ1bwwWNdCmfDjhG9x0vetRKFqePiHHtYRloTdynYukg_XZNO0cc25_L8jYkN2aDOsGJpyr2sRo1; vts_usr_lg=93074A90D244461C383BBFE9EB4D475015C158ADC7C6CCF075E44C9654E4377A94F1A704C5F67B650E8482B3E1EB1612415557C39A61B6372E821969994DA7DDB46514ABCA15A3CB3C08F9EE9382AD7A28CF4E106308C2E4863C7A6D8A2F7D4FDD4B2A27DA32104F0D8F796836733F21AABC3D72BA8457746549A7EE8FA6F4A5451E03CC55A3703D2D55A40DB56E5D2E;"
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

        if response.meta["page_number"] <= 160:
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
                                          "pageSize": "20"
                                      },
                                      headers= {
                                          "X-Requested-With": "XMLHttpRequest",
                                          "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                          'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
                                          "User-Agent":  random.choice(settings.get('USER_AGENT_LIST')),
                                          "Cookie": "language=vi-VN; isShowLogin=true;  ASP.NET_SessionId=rywvhzyai4ffxqkne4crvlje; __RequestVerificationToken=cC6zL47mdjaUyeLGF-VH3hAI-gdTK92KyZ1bwwWNdCmfDjhG9x0vetRKFqePiHHtYRloTdynYukg_XZNO0cc25_L8jYkN2aDOsGJpyr2sRo1; vts_usr_lg=93074A90D244461C383BBFE9EB4D475015C158ADC7C6CCF075E44C9654E4377A94F1A704C5F67B650E8482B3E1EB1612415557C39A61B6372E821969994DA7DDB46514ABCA15A3CB3C08F9EE9382AD7A28CF4E106308C2E4863C7A6D8A2F7D4FDD4B2A27DA32104F0D8F796836733F21AABC3D72BA8457746549A7EE8FA6F4A5451E03CC55A3703D2D55A40DB56E5D2E;"
                                      },
                                      meta= {
                                          "page_number": page_number+1,
                                          "isShowLogin": isShowLogin,
                                          "language": language,
                                          "ASP_sessionId": ASP_sessionId,
                                          "verifyToken": verifyToken,
                                          "vts_usr_lg":"93074A90D244461C383BBFE9EB4D475015C158ADC7C6CCF075E44C9654E4377A94F1A704C5F67B650E8482B3E1EB1612415557C39A61B6372E821969994DA7DDB46514ABCA15A3CB3C08F9EE9382AD7A28CF4E106308C2E4863C7A6D8A2F7D4FDD4B2A27DA32104F0D8F796836733F21AABC3D72BA8457746549A7EE8FA6F4A5451E03CC55A3703D2D55A40DB56E5D2E"
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
                                          "pageSize": "20"
                                      },
                                      headers= {
                                          "X-Requested-With": "XMLHttpRequest",
                                          "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                          'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
                                          "User-Agent":  random.choice(settings.get('USER_AGENT_LIST')),
                                          "Cookie": "language=vi-VN; isShowLogin=true;  ASP.NET_SessionId=rywvhzyai4ffxqkne4crvlje; __RequestVerificationToken=cC6zL47mdjaUyeLGF-VH3hAI-gdTK92KyZ1bwwWNdCmfDjhG9x0vetRKFqePiHHtYRloTdynYukg_XZNO0cc25_L8jYkN2aDOsGJpyr2sRo1; vts_usr_lg=93074A90D244461C383BBFE9EB4D475015C158ADC7C6CCF075E44C9654E4377A94F1A704C5F67B650E8482B3E1EB1612415557C39A61B6372E821969994DA7DDB46514ABCA15A3CB3C08F9EE9382AD7A28CF4E106308C2E4863C7A6D8A2F7D4FDD4B2A27DA32104F0D8F796836733F21AABC3D72BA8457746549A7EE8FA6F4A5451E03CC55A3703D2D55A40DB56E5D2E;"
                                      },
                                      meta= {
                                          "page_number": page_number+1,
                                          "isShowLogin": isShowLogin,
                                          "language": language,
                                          "ASP_sessionId": ASP_sessionId,
                                          "verifyToken": verifyToken,
                                          "vts_usr_lg": "93074A90D244461C383BBFE9EB4D475015C158ADC7C6CCF075E44C9654E4377A94F1A704C5F67B650E8482B3E1EB1612415557C39A61B6372E821969994DA7DDB46514ABCA15A3CB3C08F9EE9382AD7A28CF4E106308C2E4863C7A6D8A2F7D4FDD4B2A27DA32104F0D8F796836733F21AABC3D72BA8457746549A7EE8FA6F4A5451E03CC55A3703D2D55A40DB56E5D2E"
                                      }
                                  )
            except:
                pass