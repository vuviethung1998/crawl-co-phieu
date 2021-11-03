import json
from scrapy.spiders import CrawlSpider
from scrapy import Request, FormRequest
import random
from crawl_cp_finance_stock.import_setting import *
from crawl_cp_finance_stock.config.ListStock import *

class FinanceStockChiSoTaiChinhQuarterSpider(CrawlSpider):
    name = "finance_stock_can_doi_ke_toan_quarter"

    def __init__(self, **kwargs):
        super(FinanceStockChiSoTaiChinhQuarterSpider, self).__init__(**kwargs)
        self.allowed_domains = ['finance.vietstock.vn']
        # HOSE + HNX
        self.lst_cp  = UPCOM

        self.start_urls = ['https://finance.vietstock.vn']
        settings['CRAWLER_COLLECTION'] = 'CAN_DOI_KE_TOAN_QUARTER'

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

        # ReportTermType: 2 -> month
        # ReportTermType: 1 -> year
        yield FormRequest('https://finance.vietstock.vn/data/financeinfo',
                                method="POST",
                                callback= self.parse_bao_cao,
                                formdata={
                                   "Code": self.lst_cp[ck_index],
                                   "ReportType":"CDKT",
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
        can_doi_ke_toan = json.loads(response.body)[1]

        for i in range(0,4):
            try:
                obj = {}
                obj["Chung_khoan_name"] = response.meta["ck_name"]
                obj["Quarter"] = thong_tin[i]["TermCode"]
                obj["Year"] = thong_tin[i]["YearPeriod"]
                obj["ID_Chung_khoan"] = thong_tin[i]["CompanyID"]
                obj["Tài sản ngắn hạn"] = can_doi_ke_toan["Cân đối kế toán"][1]["Value{}".format(str(4-i))]
                obj["Tiền và tài sản tương đương tiền"] = can_doi_ke_toan["Cân đối kế toán"][2]["Value{}".format(str(4-i))]
                obj["Đầu tư tài chính ngắn hạn"] = can_doi_ke_toan["Cân đối kế toán"][5]["Value{}".format(str(4-i))]
                obj["Các khoản phải thu ngắn hạn"] = can_doi_ke_toan["Cân đối kế toán"][9]["Value{}".format(str(4-i))]
                obj["Hàng tồn kho"] = can_doi_ke_toan["Cân đối kế toán"][18]["Value{}".format(str(4-i))]
                obj["Tài sản dài hạn"] = can_doi_ke_toan["Cân đối kế toán"][27]["Value{}".format(str(4-i))]
                obj["Khoản phải thu dài hạn"] = can_doi_ke_toan["Cân đối kế toán"][28]["Value{}".format(str(4-i))]
                obj["Tài sản cố định hữu hình"] = can_doi_ke_toan["Cân đối kế toán"][37]["Value{}".format(str(4-i))]
                obj["Tài sản cố định vô hình"] = can_doi_ke_toan["Cân đối kế toán"][43]["Value{}".format(str(4-i))]
                obj["Bất động sản đầu tư"] = can_doi_ke_toan["Cân đối kế toán"][46]["Value{}".format(str(4-i))]
                obj["Tài sản dở dang dài hạn"] = can_doi_ke_toan["Cân đối kế toán"][49]["Value{}".format(str(4-i))]
                obj["Đầu tư tài chính dài hạn"] = can_doi_ke_toan["Cân đối kế toán"][52]["Value{}".format(str(4-i))]
                obj["Tổng cộng nguồn vốn"] = can_doi_ke_toan["Cân đối kế toán"][122]["Value{}".format(str(4-i))]
                obj["Nợ phải trả"] = can_doi_ke_toan["Cân đối kế toán"][67]["Value{}".format(str(4-i))]
                obj["Nợ ngắn hạn"] = can_doi_ke_toan["Cân đối kế toán"][68]["Value{}".format(str(4-i))]
                obj["Vay và nợ ngắn hạn"] = can_doi_ke_toan["Cân đối kế toán"][78]["Value{}".format(str(4-i))]
                obj["Phải trả người bán"] = can_doi_ke_toan["Cân đối kế toán"][69]["Value{}".format(str(4-i))]
                obj["Người mua trả tiền trước"] = can_doi_ke_toan["Cân đối kế toán"][70]["Value{}".format(str(4-i))]
                obj["Phải trả người lao động"] = can_doi_ke_toan["Cân đối kế toán"][72]["Value{}".format(str(4-i))]
                obj["Chi phí phải trả ngắn hạn"] = can_doi_ke_toan["Cân đối kế toán"][73]["Value{}".format(str(4-i))]
                obj["Doanh thu chưa thực hiện ngắn hạn"] = can_doi_ke_toan["Cân đối kế toán"][76]["Value{}".format(str(4-i))]
                obj["Nợ dài hạn"] = can_doi_ke_toan["Cân đối kế toán"][83]["Value{}".format(str(4-i))]
                obj["Vay và nợ dài hạn"] = can_doi_ke_toan["Cân đối kế toán"][91]["Value{}".format(str(4-i))]
                obj["Phải trả dài hạn người bán"] = can_doi_ke_toan["Cân đối kế toán"][84]["Value{}".format(str(4-i))]
                obj["Người mua trả tiền trước dài hạn"] = can_doi_ke_toan["Cân đối kế toán"][85]["Value{}".format(str(4-i))]
                obj["Doanh thu chưa thực hiện dài hạn"] = can_doi_ke_toan["Cân đối kế toán"][89]["Value{}".format(str(4-i))]
                obj["Vốn chủ sở hữu"] = can_doi_ke_toan["Cân đối kế toán"][98]["Value{}".format(str(4-i))]
                obj["Cổ phiếu phổ thông"] = can_doi_ke_toan["Cân đối kế toán"][101]["Value{}".format(str(4-i))]
                obj["Thặng dư vốn cổ phần"] = can_doi_ke_toan["Cân đối kế toán"][103]["Value{}".format(str(4-i))]
                obj["Cổ phiếu quỹ"] = can_doi_ke_toan["Cân đối kế toán"][106]["Value{}".format(str(4-i))]
                obj["Quỹ đầu tư phát triển"] = can_doi_ke_toan["Cân đối kế toán"][109]["Value{}".format(str(4-i))]
                obj["Lợi nhuận chưa phân phối"] = can_doi_ke_toan["Cân đối kế toán"][112]["Value{}".format(str(4-i))]

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
                                          "ReportType":"CDKT",
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
                                          "ReportType":"CDKT",
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