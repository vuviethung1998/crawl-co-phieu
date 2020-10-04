import json
from scrapy.spiders import CrawlSpider
from scrapy import Request, FormRequest
import random
from crawl_cp_finance_stock.import_setting import *
from crawl_cp_finance_stock.config.ListStock import *

class FinanceStockLuuChuyenTienTeSpider(CrawlSpider):
    name = "finance_stock_luu_chuyen_tien_te"

    def __init__(self, **kwargs):
        super(FinanceStockLuuChuyenTienTeSpider, self).__init__(**kwargs)
        self.allowed_domains = ['finance.vietstock.vn']

        self.lst_cp =  HOSE + HNX

        self.start_urls = ['https://finance.vietstock.vn']
        settings['CRAWLER_COLLECTION'] = "LUU_CHUYEN_TIEN_TE"

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
                                   "ReportType":"LCTT",
                                   "ReportTermType": "1",
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
        luu_chuyen_tien_te = json.loads(response.body)[1]

        for i in range(0,4):
            try:
                obj = {}
                obj["Chung_khoan_name"] = response.meta["ck_name"]
                obj["Quarter"] = thong_tin[i]["TermCode"]
                obj["Year"] = thong_tin[i]["YearPeriod"]
                obj["ID_Chung_khoan"] = thong_tin[i]["CompanyID"]
                obj["Lưu chuyển tiền tệ"] = luu_chuyen_tien_te["Lưu chuyển tiền tệ gián tiếp"][46]["Value{}".format(str(4-i))]
                obj["Tăng giảm các khoản phải thu"] = luu_chuyen_tien_te["Lưu chuyển tiền tệ gián tiếp"][13]["Value{}".format(str(4-i))]
                obj["Tăng giảm hàng tồn kho"] = luu_chuyen_tien_te["Lưu chuyển tiền tệ gián tiếp"][14]["Value{}".format(str(4-i))]
                obj["Tăng giảm các khoản phải trả"] = luu_chuyen_tien_te["Lưu chuyển tiền tệ gián tiếp"][15]["Value{}".format(str(4-i))]
                obj["Lưu chuyển tiền từ hoạt động kinh doanh"] = luu_chuyen_tien_te["Lưu chuyển tiền tệ gián tiếp"][22]["Value{}".format(str(4-i))]
                obj["Mua sắm TSCĐ"] =  luu_chuyen_tien_te["Lưu chuyển tiền tệ gián tiếp"][24]["Value{}".format(str(4-i))]
                obj["Tiền chi đầu tư góp vốn vào đơn vị khác"] = luu_chuyen_tien_te["Lưu chuyển tiền tệ gián tiếp"][28]["Value{}".format(str(4-i))]
                obj["Tiền thu lãi vay, cổ tức và lợi nhuận được chia"] = luu_chuyen_tien_te["Lưu chuyển tiền tệ gián tiếp"][30]["Value{}".format(str(4-i))]
                obj["Lưu chuyển tiền từ hoạt động đầu tư"] = luu_chuyen_tien_te["Lưu chuyển tiền tệ gián tiếp"][35]["Value{}".format(str(4-i))]
                obj["Tiền vay ngắn hạn, dài hạn nhận được"] = luu_chuyen_tien_te["Lưu chuyển tiền tệ gián tiếp"][39]["Value{}".format(str(4-i))]
                obj["Tiền chi trả nợ gốc vay"] = luu_chuyen_tien_te["Lưu chuyển tiền tệ gián tiếp"][40]["Value{}".format(str(4-i))]
                obj["Cổ tức, lợi nhuận đã trả cho chủ sở hữu"] = luu_chuyen_tien_te["Lưu chuyển tiền tệ gián tiếp"][42]["Value{}".format(str(4-i))]
                obj["Lưu chuyển tiền thuần từ hoạt động tài chính"] = luu_chuyen_tien_te["Lưu chuyển tiền tệ gián tiếp"][45]["Value{}".format(str(4-i))]
                # print(obj)
                yield(obj)
            except:
                pass

        # quay lai parse
        # neu page_number < 7 thi chuyen trang
        # neu page_number > 7 thi chuyen co phieu
        page_number = response.meta["page_number"]
        ck_index =  response.meta["ck_index"]

        if response.meta["page_number"] <= 5:
            try:
                yield FormRequest('https://finance.vietstock.vn/data/financeinfo',
                                      method="POST",
                                      callback= self.parse_bao_cao,
                                      formdata={
                                          "Code": self.lst_cp[ck_index],
                                          "ReportType":"LCTT",
                                          "ReportTermType": "1",
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
                                          "ReportType":"LCTT",
                                          "ReportTermType": "1",
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
