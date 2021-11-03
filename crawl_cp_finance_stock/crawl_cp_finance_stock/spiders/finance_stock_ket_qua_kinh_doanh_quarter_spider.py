import json
from scrapy.spiders import CrawlSpider
from scrapy import Request, FormRequest
import random
from crawl_cp_finance_stock.import_setting import *
from crawl_cp_finance_stock.config.ListStock import *

class FinanceStockKetQuaKinhDoanhQuarterSpider(CrawlSpider):
    name = "finance_stock_ket_qua_kinh_doanh_quarter"

    def __init__(self, **kwargs):
        super(FinanceStockKetQuaKinhDoanhQuarterSpider, self).__init__(**kwargs)
        self.allowed_domains = ['finance.vietstock.vn']

        self.lst_cp =  HOSE + HNX + UPCOM

        self.start_urls = ['https://finance.vietstock.vn']
        settings['CRAWLER_COLLECTION'] = "KET_QUA_KINH_DOANH_QUARTER"

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
                                   "ReportType":"KQKD",
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
        ket_qua_kinh_doanh = json.loads(response.body)[1]

        for i in range(0,4):
            try:
                obj = {}
                obj["Chung_khoan_name"] = response.meta["ck_name"]
                obj["Quarter"] = thong_tin[i]["TermCode"]
                obj["Year"] = thong_tin[i]["YearPeriod"]
                obj["ID_Chung_khoan"] = thong_tin[i]["CompanyID"]
                obj["Doanh thu thuần từ hoạt động kinh doanh"] = ket_qua_kinh_doanh["Kết quả kinh doanh"][2]["Value{}".format(str(4-i))]
                obj["Giá vốn bán hàng"] = ket_qua_kinh_doanh["Kết quả kinh doanh"][3]["Value{}".format(str(4-i))]
                obj["Chi phí bán hàng"] = ket_qua_kinh_doanh["Kết quả kinh doanh"][9]["Value{}".format(str(4-i))]
                obj["Chi phí quản lý doanh nghiệp"] = ket_qua_kinh_doanh["Kết quả kinh doanh"][10]["Value{}".format(str(4-i))]
                obj["Lợi nhuận từ hoạt động kinh doanh"] = ket_qua_kinh_doanh["Kết quả kinh doanh"][11]["Value{}".format(str(4-i))]
                obj["Doanh thu từ hoạt động tài chính"] =  ket_qua_kinh_doanh["Kết quả kinh doanh"][5]["Value{}".format(str(4-i))]
                obj["Chi phí tài chính"] = ket_qua_kinh_doanh["Kết quả kinh doanh"][6]["Value{}".format(str(4-i))]
                obj["Chi phí lãi vay"] = ket_qua_kinh_doanh["Kết quả kinh doanh"][7]["Value{}".format(str(4-i))]
                obj["Lợi nhuận từ công ty liên kết"] = ket_qua_kinh_doanh["Kết quả kinh doanh"][8]["Value{}".format(str(4-i))]
                obj["Doanh thu từ thu nhập khác"] = ket_qua_kinh_doanh["Kết quả kinh doanh"][12]["Value{}".format(str(4-i))]
                obj["Lợi nhuận từ thu nhập khác"] = ket_qua_kinh_doanh["Kết quả kinh doanh"][14]["Value{}".format(str(4-i))]
                obj["Tổng lợi nhuận trước thuế"] = ket_qua_kinh_doanh["Kết quả kinh doanh"][16]["Value{}".format(str(4-i))]
                obj["Lợi nhuận sau thuế"] = ket_qua_kinh_doanh["Kết quả kinh doanh"][17]["Value{}".format(str(4-i))]
                obj["Tổng doanh thu"] = int(obj["Doanh thu thuần từ hoạt động kinh doanh"]) + int(obj["Doanh thu từ hoạt động tài chính"]) + int(obj["Doanh thu từ thu nhập khác"])
                yield(obj)
            except:
                pass

        # quay lai parse
        # neu page_number < 7 thi chuyen trang
        # neu page_number > 7 thi chuyen co phieu
        page_number = response.meta["page_number"]
        ck_index =  response.meta["ck_index"]

        if response.meta["page_number"] <= 40:
            try:
                yield FormRequest('https://finance.vietstock.vn/data/financeinfo',
                                      method="POST",
                                      callback= self.parse_bao_cao,
                                      formdata={
                                          "Code": self.lst_cp[ck_index],
                                          "ReportType":"KQKD",
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
                                          "ReportType":"KQKD",
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