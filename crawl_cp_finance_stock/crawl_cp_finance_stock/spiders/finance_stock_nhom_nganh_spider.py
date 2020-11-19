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
        vts_usr_lg="77361D345F93AEA2C62B58C5DEBB8F2CD2D924A26F6CAA591F2712AA9F26EFF8BF1073ECEE48B612FD86204B088DDF2DBC42352C6E73304FA2C9F51A4C6039A5F687CCDFFF27A8C8D7FF838DFE5F47C53C23BFE4CB634DB6551B494BE5C6F39CD3722DC1EF98331090E8036EE3A48B42312E68031DEC8E51671155FAD33CBFFB1648928A0F110A7F6D0F43FC75570F30"

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
                                  "Cookie": "language=vi-VN; isShowLogin=true;  ASP.NET_SessionId=rywvhzyai4ffxqkne4crvlje; __RequestVerificationToken=cC6zL47mdjaUyeLGF-VH3hAI-gdTK92KyZ1bwwWNdCmfDjhG9x0vetRKFqePiHHtYRloTdynYukg_XZNO0cc25_L8jYkN2aDOsGJpyr2sRo1; vts_usr_lg=77361D345F93AEA2C62B58C5DEBB8F2CD2D924A26F6CAA591F2712AA9F26EFF8BF1073ECEE48B612FD86204B088DDF2DBC42352C6E73304FA2C9F51A4C6039A5F687CCDFFF27A8C8D7FF838DFE5F47C53C23BFE4CB634DB6551B494BE5C6F39CD3722DC1EF98331090E8036EE3A48B42312E68031DEC8E51671155FAD33CBFFB1648928A0F110A7F6D0F43FC75570F30;"
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
                                          "Cookie": "language=vi-VN; isShowLogin=true;  ASP.NET_SessionId=rywvhzyai4ffxqkne4crvlje; __RequestVerificationToken=cC6zL47mdjaUyeLGF-VH3hAI-gdTK92KyZ1bwwWNdCmfDjhG9x0vetRKFqePiHHtYRloTdynYukg_XZNO0cc25_L8jYkN2aDOsGJpyr2sRo1; vts_usr_lg=77361D345F93AEA2C62B58C5DEBB8F2CD2D924A26F6CAA591F2712AA9F26EFF8BF1073ECEE48B612FD86204B088DDF2DBC42352C6E73304FA2C9F51A4C6039A5F687CCDFFF27A8C8D7FF838DFE5F47C53C23BFE4CB634DB6551B494BE5C6F39CD3722DC1EF98331090E8036EE3A48B42312E68031DEC8E51671155FAD33CBFFB1648928A0F110A7F6D0F43FC75570F30;"
                                      },
                                      meta= {
                                          "page_number": page_number+1,
                                          "isShowLogin": isShowLogin,
                                          "language": language,
                                          "ASP_sessionId": ASP_sessionId,
                                          "verifyToken": verifyToken,
                                          "vts_usr_lg":"77361D345F93AEA2C62B58C5DEBB8F2CD2D924A26F6CAA591F2712AA9F26EFF8BF1073ECEE48B612FD86204B088DDF2DBC42352C6E73304FA2C9F51A4C6039A5F687CCDFFF27A8C8D7FF838DFE5F47C53C23BFE4CB634DB6551B494BE5C6F39CD3722DC1EF98331090E8036EE3A48B42312E68031DEC8E51671155FAD33CBFFB1648928A0F110A7F6D0F43FC75570F30"
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
                                          "Cookie": "language=vi-VN; isShowLogin=true;  ASP.NET_SessionId=rywvhzyai4ffxqkne4crvlje; __RequestVerificationToken=cC6zL47mdjaUyeLGF-VH3hAI-gdTK92KyZ1bwwWNdCmfDjhG9x0vetRKFqePiHHtYRloTdynYukg_XZNO0cc25_L8jYkN2aDOsGJpyr2sRo1; vts_usr_lg=77361D345F93AEA2C62B58C5DEBB8F2CD2D924A26F6CAA591F2712AA9F26EFF8BF1073ECEE48B612FD86204B088DDF2DBC42352C6E73304FA2C9F51A4C6039A5F687CCDFFF27A8C8D7FF838DFE5F47C53C23BFE4CB634DB6551B494BE5C6F39CD3722DC1EF98331090E8036EE3A48B42312E68031DEC8E51671155FAD33CBFFB1648928A0F110A7F6D0F43FC75570F30;"
                                      },
                                      meta= {
                                          "page_number": page_number+1,
                                          "isShowLogin": isShowLogin,
                                          "language": language,
                                          "ASP_sessionId": ASP_sessionId,
                                          "verifyToken": verifyToken,
                                          "vts_usr_lg": "77361D345F93AEA2C62B58C5DEBB8F2CD2D924A26F6CAA591F2712AA9F26EFF8BF1073ECEE48B612FD86204B088DDF2DBC42352C6E73304FA2C9F51A4C6039A5F687CCDFFF27A8C8D7FF838DFE5F47C53C23BFE4CB634DB6551B494BE5C6F39CD3722DC1EF98331090E8036EE3A48B42312E68031DEC8E51671155FAD33CBFFB1648928A0F110A7F6D0F43FC75570F30"
                                      }
                                  )
            except:
                pass