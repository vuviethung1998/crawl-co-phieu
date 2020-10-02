import json
from scrapy.spiders import CrawlSpider
from scrapy import Request, FormRequest
import random
from crawl_cp_finance_stock.import_setting import *
from crawl_cp_finance_stock.config.ListStock import *


class FinanceStockCongTyLienKetSpider(CrawlSpider):
    name = "finance_stock_cong_ty_lien_ket"

    def __init__(self, **kwargs):
        super(FinanceStockCongTyLienKetSpider, self).__init__(**kwargs)
        self.allowed_domains = ['finance.vietstock.vn']

        self.lst_cp =  HOSE + HNX

        self.start_urls = ['https://finance.vietstock.vn']
        settings['CRAWLER_COLLECTION'] = "CONG_TY_LIEN_KET"

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, callback=self.parse, meta={"ck_index" : 0})

    def parse(self, response):
        isShowLogin = "isShowLogin=true"
        language =  response.headers.getlist('Set-Cookie')[0].decode("utf-8").split(";")[0]
        ASP_sessionId = response.headers.getlist('Set-Cookie')[1].decode("utf-8").split(";")[0]
        verifyToken =  response.headers.getlist('Set-Cookie')[4].decode("utf-8").split(";")[0]

        ck_index = response.meta["ck_index"]

        print(self.lst_cp[ck_index])

        yield FormRequest('https://finance.vietstock.vn/data/associatesdetails',
                              method="POST",
                              callback= self.parse_cong_ty_lien_ket,
                              formdata={
                                  "Code": self.lst_cp[ck_index],
                                  "page": "1"
                              },
                              headers= {
                                  "X-Requested-With": "XMLHttpRequest",
                                  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                  'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
                                  "User-Agent":  random.choice(settings.get('USER_AGENT_LIST')),
                                  "Cookie": "language=vi-VN; isShowLogin=true; ASP.NET_SessionId=ewd2tsio3v1ty54w1crcovoo; __RequestVerificationToken=14JcMYut0_NcTmKkFBhMQtfUAnoCprQd5Q1GacqraocLNmAHUa2upWnyrRiMe1F7s3_H0C7JVavI9cozLU_Q2Ruq_fk7v6Xx5W8I-dndRAA1; vts_usr_lg=5AD3F33BA6D795DA1EDD8C789770DDF6D900D8920D311217CC1724FA47674B0EA46EA49FCFF6FD0624E3DE12D11D5FAB56CE06E26494FC7D0D49B204F5083054C45CE0E4D2120617E9BC8EB15C319F72AADF209EF7B2A1FCD3907016FFF4DE2EAC629B010351743BF438D6587E31677F5DF63416EA0236F9E05B1DD7939508DDF7B90B14F68F0449282EEA91F7100640;"
                              },
                              meta= {
                                  "ck_name": self.lst_cp[ck_index],
                                  "ck_index": ck_index,
                                  "isShowLogin": isShowLogin,
                                  "language": language,
                                  "ASP_sessionId": ASP_sessionId,
                                  "verifyToken": verifyToken
                              }
                          )

    def parse_cong_ty_lien_ket(self, response):
        isShowLogin = response.meta["isShowLogin"]
        language = response.meta["language"]
        ASP_sessionId = response.meta["ASP_sessionId"]
        verifyToken = response.meta["verifyToken"]

        cong_ty_lien_ket_lst = json.loads(response.body)[0]["Details"]

        for cong_ty_lien_ket in cong_ty_lien_ket_lst:
            obj = {}
            obj["Chung_khoan_name"] = response.meta["ck_name"]
            obj["CompanyID"] = cong_ty_lien_ket["CompanyID"]
            obj["Associates"] = cong_ty_lien_ket["Associates"]
            obj["Associates_VN"] = cong_ty_lien_ket["Associates_VN"]
            obj["CharteredCapital"] = cong_ty_lien_ket["CharteredCapital"]
            obj["OwnerRatio"] = cong_ty_lien_ket["OwnerRatio"]
            obj["Industry"] = cong_ty_lien_ket["Industry"]

            yield  obj

        # quay lai parse
        # neu page_number < 7 thi chuyen trang
        # neu page_number > 7 thi chuyen co phieu

        ck_index =  response.meta["ck_index"]
        try:
            yield FormRequest('https://finance.vietstock.vn/data/associatesdetails',
                                  method="POST",
                                  callback= self.parse_cong_ty_lien_ket,
                                  formdata={
                                      "Code": self.lst_cp[ck_index+1],
                                      "page": "1"
                                  },
                                  headers= {
                                      "X-Requested-With": "XMLHttpRequest",
                                      "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                      'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
                                      "User-Agent":  random.choice(settings.get('USER_AGENT_LIST')),
                                      "Cookie": "language=vi-VN; isShowLogin=true; ASP.NET_SessionId=ewd2tsio3v1ty54w1crcovoo; __RequestVerificationToken=14JcMYut0_NcTmKkFBhMQtfUAnoCprQd5Q1GacqraocLNmAHUa2upWnyrRiMe1F7s3_H0C7JVavI9cozLU_Q2Ruq_fk7v6Xx5W8I-dndRAA1; vts_usr_lg=5AD3F33BA6D795DA1EDD8C789770DDF6D900D8920D311217CC1724FA47674B0EA46EA49FCFF6FD0624E3DE12D11D5FAB56CE06E26494FC7D0D49B204F5083054C45CE0E4D2120617E9BC8EB15C319F72AADF209EF7B2A1FCD3907016FFF4DE2EAC629B010351743BF438D6587E31677F5DF63416EA0236F9E05B1DD7939508DDF7B90B14F68F0449282EEA91F7100640;"
                                  },
                                  meta= {
                                      "ck_name": self.lst_cp[ck_index+1],
                                      "ck_index": ck_index+1,
                                      "isShowLogin": isShowLogin,
                                      "language": language,
                                      "ASP_sessionId": ASP_sessionId,
                                      "verifyToken": verifyToken
                                  }
                              )
        except:
            pass