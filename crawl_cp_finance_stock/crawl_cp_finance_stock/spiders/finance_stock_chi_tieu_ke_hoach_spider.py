import json
from scrapy.spiders import CrawlSpider
from scrapy import Request, FormRequest
import random
from crawl_cp_finance_stock.import_setting import *
from crawl_cp_finance_stock.config.ListStock import *

class FinanceStockChiTieuKeHoachSpider(CrawlSpider):
    name = "finance_stock_chi_tieu_ke_hoach"

    def __init__(self, **kwargs):
        super(FinanceStockChiTieuKeHoachSpider, self).__init__(**kwargs)
        self.allowed_domains = ['finance.vietstock.vn']

        self.lst_cp =  HOSE + HNX

        self.start_urls = ['https://finance.vietstock.vn']
        settings['CRAWLER_COLLECTION'] = "CHI_TIEU_KE_HOACH"

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, callback=self.parse, meta={
                "ck_index" : 0,
                "page_number": 1
            })

    def parse(self, response):
        isShowLogin = "isShowLogin=true"
        language =  response.headers.getlist('Set-Cookie')[0].decode("utf-8").split(";")[0]
        ASP_sessionId = response.headers.getlist('Set-Cookie')[1].decode("utf-8").split(";")[0]
        verifyToken =  response.headers.getlist('Set-Cookie')[4].decode("utf-8").split(";")[0]

        page_number = response.meta['page_number']
        ck_index = response.meta["ck_index"]

        print(self.lst_cp[ck_index])

        yield FormRequest('https://finance.vietstock.vn/data/financeinfo',
                          method="POST",
                          callback= self.parse_bao_cao,
                          formdata={
                              "Code": self.lst_cp[ck_index],
                              "ReportType":"CTKH",
                              "ReportTermType": "2",
                              "Unit": "1000000",
                              "Page": str(page_number),
                              "PageSize": "1"
                          },
                          headers= {
                              "X-Requested-With": "XMLHttpRequest",
                              "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                              'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
                              "User-Agent":  random.choice(settings.get('USER_AGENT_LIST')),
                              "Cookie": isShowLogin + "; " + language + "; " + ASP_sessionId + "; " + verifyToken + "; "
                          },
                          meta= {
                              "ck_name": self.lst_cp[ck_index],
                              "ck_index": ck_index,
                              "page_number": page_number,
                              "isShowLogin": isShowLogin,
                              "language": language,
                              "ASP_sessionId": ASP_sessionId,
                              "verifyToken": verifyToken
                          }
                          )


    def parse_bao_cao(self, response):
        isShowLogin = response.meta["isShowLogin"]
        language = response.meta["language"]
        ASP_sessionId = response.meta["ASP_sessionId"]
        verifyToken = response.meta["verifyToken"]

        thong_tin = json.loads(response.body)[0]
        chi_tieu_ke_hoach = json.loads(response.body)[1]

        for i in range(0,4):
            try:
                obj = {}
                obj["Chung_khoan_name"] = response.meta["ck_name"]
                obj["Quarter"] = thong_tin[i]["TermCode"]
                obj["Year"] = thong_tin[i]["YearPeriod"]
                obj["ID_Chung_khoan"] = thong_tin[i]["CompanyID"]
                try:
                    obj["Tổng doanh thu"] = chi_tieu_ke_hoach[0]["Value{}".format(str(4-i))]
                except:
                    obj["Tổng doanh thu"] = 0
                try:
                    obj["Doanh thu thuần"] = chi_tieu_ke_hoach[1]["Value{}".format(str(4-i))]
                except:
                    obj["Doanh thu thuần"] = 0
                try:
                    obj["Lợi nhuận trước thuế"] = chi_tieu_ke_hoach[2]["Value{}".format(str(4-i))]
                except:
                    obj["Lợi nhuận trước thuế"] = 0
                try:
                    obj["Lợi nhuận sau thuế"] = chi_tieu_ke_hoach[3]["Value{}".format(str(4-i))]
                except:
                    obj["Lợi nhuận sau thuế"] = 0
                try:
                    obj["Tỷ lệ cổ tức bằng tiền (% VĐL)"] = chi_tieu_ke_hoach[4]["Value{}".format(str(4-i))]
                except:
                    obj["Tỷ lệ cổ tức bằng tiền (% VĐL)"] = 0
                try:
                    obj["Tỷ lệ cổ tức bằng cổ phiếu (%VĐL)"] = chi_tieu_ke_hoach[5]["Value{}".format(str(4-i))]
                except:
                    obj["Tỷ lệ cổ tức bằng cổ phiếu (%VĐL)"] = 0
                try:
                    obj["Tỷ lệ cổ tức (%)"] = chi_tieu_ke_hoach[6]["Value{}".format(str(4-i))]
                except:
                    obj["Tỷ lệ cổ tức (%)"] = 0
                yield(obj)
            except:
                pass

        # quay lai parse
        # neu page_number < 7 thi chuyen trang
        # neu page_number > 7 thi chuyen co phieu
        page_number = response.meta["page_number"]
        ck_index =  response.meta["ck_index"]

        if response.meta["page_number"] <= 10:
            try:
                yield FormRequest('https://finance.vietstock.vn/data/financeinfo',
                                  method="POST",
                                  callback= self.parse_bao_cao,
                                  formdata={
                                      "Code": self.lst_cp[ck_index],
                                      "ReportType":"CTKH",
                                      "ReportTermType": "2",
                                      "Unit": "1000000",
                                      "Page": str(page_number+1),
                                      "PageSize": "1"
                                  },
                                  headers= {
                                      "X-Requested-With": "XMLHttpRequest",
                                      "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                      'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
                                      "User-Agent":  random.choice(settings.get('USER_AGENT_LIST')),
                                      "Cookie": isShowLogin + "; " + language + "; " + ASP_sessionId + "; " + verifyToken + "; "
                                  },
                                  meta= {
                                      "ck_name": self.lst_cp[ck_index],
                                      "ck_index": ck_index,
                                      "page_number": page_number+1,
                                      "isShowLogin": isShowLogin,
                                      "language": language,
                                      "ASP_sessionId": ASP_sessionId,
                                      "verifyToken": verifyToken
                                  }
                                  )
            except:
                pass
        else:
            try:
                yield FormRequest('https://finance.vietstock.vn/data/financeinfo',
                                  method="POST",
                                  callback= self.parse_bao_cao,
                                  formdata={
                                      "Code": self.lst_cp[ck_index+1],
                                      "ReportType":"CTKH",
                                      "ReportTermType": "2",
                                      "Unit": "1000000",
                                      "Page": "1",
                                      "PageSize": "1"
                                  },
                                  headers= {
                                      "X-Requested-With": "XMLHttpRequest",
                                      "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                      'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
                                      "User-Agent":  random.choice(settings.get('USER_AGENT_LIST')),
                                      "Cookie": isShowLogin + "; " + language + "; " + ASP_sessionId + "; " + verifyToken + "; "
                                  },
                                  meta= {
                                      "ck_name": self.lst_cp[ck_index+1],
                                      "ck_index": ck_index+1,
                                      "page_number": 1,
                                      "isShowLogin": isShowLogin,
                                      "language": language,
                                      "ASP_sessionId": ASP_sessionId,
                                      "verifyToken": verifyToken
                                  }
                                  )
            except:
                pass
