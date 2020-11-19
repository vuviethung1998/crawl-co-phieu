from scrapy.spiders import CrawlSpider
from scrapy import Request, FormRequest
import random
import json
from crawl_cp_finance_stock.import_setting import *
from crawl_cp_finance_stock.config.ListStock import *

class FinanceStockVonHoaThiTruongSpider(CrawlSpider):
    name = "finance_stock_von_hoa_thi_truong_spider"

    def __init__(self, **kwargs):
        super(FinanceStockVonHoaThiTruongSpider, self).__init__(**kwargs)
        self.allowed_domains = ['finance.vietstock.vn']
        self.lst_cp =  HOSE + HNX
        self.start_urls = ['https://finance.vietstock.vn']
        settings['CRAWLER_COLLECTION'] = "VON_HOA_THI_TRUONG"

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, callback=self.parse, meta={"ck_index" : 0})

    def parse(self, response):
        isShowLogin = "isShowLogin=true"
        language =  response.headers.getlist('Set-Cookie')[0].decode("utf-8").split(";")[0]
        ASP_sessionId = response.headers.getlist('Set-Cookie')[1].decode("utf-8").split(";")[0]
        verifyToken =  response.headers.getlist('Set-Cookie')[4].decode("utf-8").split(";")[0]

        ck_index = response.meta["ck_index"]
        # print(ck_index)
        yield FormRequest('https://finance.vietstock.vn/company/tradinginfo',
                              method="POST",
                              callback= self.parse_von_hoa_thi_truong,
                              formdata={
                                  "code": self.lst_cp[ck_index],
                                  "s": "0",
                                  "t": ""
                              },
                              headers= {
                                  "X-Requested-With": "XMLHttpRequest",
                                  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                  'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
                                  "User-Agent":  random.choice(settings.get('USER_AGENT_LIST')),
                                  "Cookie": "language=vi-VN; isShowLogin=true; ASP.NET_SessionId={}; __RequestVerificationToken={};".format(ASP_sessionId, verifyToken)
                                  # "Cookie": "language=vi-VN; isShowLogin=true; ASP.NET_SessionId=lfo13ld1jyvakcbsab2agj5p; __RequestVerificationToken=gnb5Z1m2K0v3k4tZKZ2sqAJ7Lxr1kJh5Co4aH29cfTnkZL1-XgoAcpWwdAGSeMP6dxv91VH7ZhxQa3eS2F6hv3zfxLP_AbsBojeguoaZzJ01; "
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

    def parse_von_hoa_thi_truong(self, response):
        isShowLogin = response.meta["isShowLogin"]
        language = response.meta["language"]
        ASP_sessionId = response.meta["ASP_sessionId"]
        verifyToken = response.meta["verifyToken"]

        von_hoa_thi_truong= json.loads(response.body)

        # print(von_hoa_thi_truong_dct)
        # for von_hoa_thi_truong in von_hoa_thi_truong_dct:
        obj = {}
        obj["Chung_khoan_name"] = response.meta["ck_name"]
        obj["CompanyID"] = von_hoa_thi_truong["StockCode"]
        obj["Khoi Luong Co Phieu Niem Yet"] = von_hoa_thi_truong["KLCPNY"]
        obj['Gia Dong'] = von_hoa_thi_truong["PriorClosePrice"]
        obj['MarketCapital'] = von_hoa_thi_truong['MarketCapital']
        yield obj
            
        ck_index = response.meta["ck_index"]
        try:
            yield FormRequest('https://finance.vietstock.vn/company/tradinginfo',
                                  method="POST",
                                  callback= self.parse_von_hoa_thi_truong,
                                  formdata={
                                      "code": self.lst_cp[ck_index+1],
                                      "s": "0",
                                      "t": ""
                                  },
                                  headers= {
                                      "X-Requested-With": "XMLHttpRequest",
                                      "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                      'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
                                      "User-Agent":  random.choice(settings.get('USER_AGENT_LIST')),
                                      "Cookie": "language=vi-VN; isShowLogin=true; ASP.NET_SessionId={}; __RequestVerificationToken={};".format(ASP_sessionId, verifyToken)
                                      # "Cookie": "language=vi-VN; isShowLogin=true; ASP.NET_SessionId=lfo13ld1jyvakcbsab2agj5p; __RequestVerificationToken=gnb5Z1m2K0v3k4tZKZ2sqAJ7Lxr1kJh5Co4aH29cfTnkZL1-XgoAcpWwdAGSeMP6dxv91VH7ZhxQa3eS2F6hv3zfxLP_AbsBojeguoaZzJ01;"
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