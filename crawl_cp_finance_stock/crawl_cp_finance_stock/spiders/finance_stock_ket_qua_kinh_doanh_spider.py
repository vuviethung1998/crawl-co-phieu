import json
from scrapy.spiders import CrawlSpider
from scrapy import Request, FormRequest
import random
from crawl_cp_finance_stock.import_setting import *
from crawl_cp_finance_stock.config.ListStock import *

class FinanceStockKetQuaKinhDoanhSpider(CrawlSpider):
    name = "finance_stock_ket_qua_kinh_doanh"

    def __init__(self, **kwargs):
        super(FinanceStockKetQuaKinhDoanhSpider, self).__init__(**kwargs)
        self.allowed_domains = ['finance.vietstock.vn']

        self.lst_cp =  HOSE + HNX

        self.start_urls = ['https://finance.vietstock.vn']
        settings['CRAWLER_COLLECTION'] = [cp for cp in self.lst_cp]

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
                                   "ReportType":"BCTT",
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
        bao_cao_tai_chinh = json.loads(response.body)[1]

        for i in range(0,4):
            try:
                obj = {}
                obj["Chung_khoan_name"] = response.meta["ck_name"]
                obj["Quarter"] = thong_tin[i]["TermCode"]
                obj["Year"] = thong_tin[i]["YearPeriod"]
                obj["ID_Chung_khoan"] = thong_tin[i]["CompanyID"]
                obj["Doanh thu thuần về bán hàng và cung cấp dịch vụ"] = bao_cao_tai_chinh["Kết quả kinh doanh"][0]["Value{}".format(str(4-i))]
                obj["Lợi nhuận gộp về bán hàng và cung cấp dịch vụ"] = bao_cao_tai_chinh["Kết quả kinh doanh"][2]["Value{}".format(str(4-i))]
                obj["Lợi nhuận thuần từ hoạt động kinh doanh"] = bao_cao_tai_chinh["Kết quả kinh doanh"][7]["Value{}".format(str(4-i))]
                obj["Tổng lợi nhuận kế toán trước thuế"] = bao_cao_tai_chinh["Kết quả kinh doanh"][10]["Value{}".format(str(4-i))]
                obj["Lợi nhuận sau thuế thu nhập doanh nghiệp"] = bao_cao_tai_chinh["Kết quả kinh doanh"][11]["Value{}".format(str(4-i))]
                obj["Lợi nhuận sau thuế của cổ đông Công ty mẹ"] =  bao_cao_tai_chinh["Kết quả kinh doanh"][12]["Value{}".format(str(4-i))]
                obj["Tài sản ngắn hạn"] = bao_cao_tai_chinh["Cân đối kế toán"][0]["Value{}".format(str(4-i))]
                obj["Hàng tồn kho"] = bao_cao_tai_chinh["Cân đối kế toán"][4]["Value{}".format(str(4-i))]
                obj["Tài sản dài hạn"] = bao_cao_tai_chinh["Cân đối kế toán"][6]["Value{}".format(str(4-i))]
                obj["Tài sản cố định"] = bao_cao_tai_chinh["Cân đối kế toán"][7]["Value{}".format(str(4-i))]
                obj["Bất động sản đầu tư"] = bao_cao_tai_chinh["Cân đối kế toán"][8]["Value{}".format(str(4-i))]
                obj["Các khoản đầu tư tài chính dài hạn"] = bao_cao_tai_chinh["Cân đối kế toán"][9]["Value{}".format(str(4-i))]
                obj["Tổng cộng tài sản"] = bao_cao_tai_chinh["Cân đối kế toán"][10]["Value{}".format(str(4-i))]
                obj["Nợ phải trả"] = bao_cao_tai_chinh["Cân đối kế toán"][11]["Value{}".format(str(4-i))]
                obj["Vốn chủ sở hữu"] = bao_cao_tai_chinh["Cân đối kế toán"][14]["Value{}".format(str(4-i))]
                obj["Vốn đầu tư của chủ sở hữu"] = bao_cao_tai_chinh["Cân đối kế toán"][15]["Value{}".format(str(4-i))]
                obj["Thặng dư vốn cổ phần"] =  bao_cao_tai_chinh["Cân đối kế toán"][16]["Value{}".format(str(4-i))]
                obj["Lợi nhuận sau thuế chưa phân phối"] = bao_cao_tai_chinh["Cân đối kế toán"][17]["Value{}".format(str(4-i))]
                obj["Tổng cộng nguồn vốn"] =  bao_cao_tai_chinh["Cân đối kế toán"][19]["Value{}".format(str(4-i))]
                obj["Thu nhập trên mỗi cổ phần của 4 quý gần nhất (EPS)"] = bao_cao_tai_chinh["Chỉ số tài chính"][0]["Value{}".format(str(4-i))]
                obj["Giá trị sổ sách của cổ phiếu (BVPS)"] =  bao_cao_tai_chinh["Chỉ số tài chính"][1]["Value{}".format(str(4-i))]
                obj["Chỉ số giá thị trường trên thu nhập (P/E)"] = bao_cao_tai_chinh["Chỉ số tài chính"][2]["Value{}".format(str(4-i))]
                obj["Chỉ số giá thị trường trên giá trị sổ sách (P/B)"] = bao_cao_tai_chinh["Chỉ số tài chính"][3]["Value{}".format(str(4-i))]
                obj["Tỷ suất lợi nhuận gộp biên"] = bao_cao_tai_chinh["Chỉ số tài chính"][4]["Value{}".format(str(4-i))]
                obj["Tỷ suất sinh lợi trên doanh thu thuần"] = bao_cao_tai_chinh["Chỉ số tài chính"][5]["Value{}".format(str(4-i))]
                obj["Tỷ suất lợi nhuận trên vốn chủ sở hữu bình quân (ROEA)"] = bao_cao_tai_chinh["Chỉ số tài chính"][6]["Value{}".format(str(4-i))]
                obj["Tỷ suất sinh lợi trên tổng tài sản bình quân (ROAA)"] = bao_cao_tai_chinh["Chỉ số tài chính"][7]["Value{}".format(str(4-i))]
                obj["Tỷ số thanh toán hiện hành (ngắn hạn)"] = bao_cao_tai_chinh["Chỉ số tài chính"][8]["Value{}".format(str(4-i))]
                obj["Khả năng thanh toán lãi vay"] = bao_cao_tai_chinh["Chỉ số tài chính"][9]["Value{}".format(str(4-i))]
                obj["Tỷ số Nợ trên Tổng tài sản"] = bao_cao_tai_chinh["Chỉ số tài chính"][10]["Value{}".format(str(4-i))]
                obj["Tỷ số Nợ vay trên Vốn chủ sở hữu"] = bao_cao_tai_chinh["Chỉ số tài chính"][11]["Value{}".format(str(4-i))]
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
                                          "ReportType":"BCTT",
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
                                          "ReportType":"BCTT",
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