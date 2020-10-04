import json
from scrapy.spiders import CrawlSpider
from scrapy import Request, FormRequest
import random
from crawl_cp_finance_stock.import_setting import *
from crawl_cp_finance_stock.config.ListStock import *
from datetime import datetime

class FinanceStockChiSoTaiChinhSpider(CrawlSpider):
    name = "finance_stock_lich_su_giao_dich"

    def __init__(self, **kwargs):
        super(FinanceStockChiSoTaiChinhSpider, self).__init__(**kwargs)
        self.allowed_domains = ['finance.vietstock.vn']

        self.lst_cp =  HOSE + HNX

        self.start_urls = ['https://finance.vietstock.vn']
        settings['CRAWLER_COLLECTION'] = 'LICH_SU_GIAO_DICH'

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, callback=self.parse, meta={
                "ck_index" : 0
            })

    def parse(self, response):
        isShowLogin = "isShowLogin=true"
        language =  response.headers.getlist('Set-Cookie')[0].decode("utf-8").split(";")[0]
        ASP_sessionId = response.headers.getlist('Set-Cookie')[1].decode("utf-8").split(";")[0]
        verifyToken =  response.headers.getlist('Set-Cookie')[4].decode("utf-8").split(";")[0]

        ck_index = response.meta["ck_index"]
        print(self.lst_cp[ck_index])

        # ReportTermType: 2 -> month
        # ReportTermType: 1 -> year
        yield FormRequest('https://finance.vietstock.vn/data/gettradingresult',
                              method="POST",
                              callback= self.parse_bao_cao,
                              formdata={
                                  "Code": self.lst_cp[ck_index],
                                  "OrderBy": "",
                                  "OrderDirection": "desc",
                                  "PageIndex": "1",
                                  "FromDate": "2019-10-04",
                                  "ToDate": "2020-10-04",
                                  "ExportType": "default",
                                  "Cols": "Room%2CRoomCL%2CRoomCLPT%2CKL_M_GDKL%2CKL_MPT_GDKL%2CGT_M_GDKL%2CGT_MPT_GDKL%2CKL_B_GDKL%2CKL_BPT_GDKL%2CGT_B_GDKL%2CGT_BPT_GDKL%2CCL_GT_MB%2CCL_KL_MB",
                                  "ExchangeID": "7",
                                  "PageSize": "251"
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

        lich_su_giao_dich = json.loads(response.body)["Data"]

        for row in lich_su_giao_dich:
            try:
                obj = {}
                obj["Chung_khoan_name"] = response.meta["ck_name"]
                obj['Ngày Giao Dịch'] = datetime.utcfromtimestamp(int(row['TradingDate'][6:-2]) / 1000 ).strftime('%Y/%m/%d')
                obj['Khối Lượng Cổ Phần Lưu Hành'] = row['KLCPLH']
                obj['Khối Lượng Cổ Phần Niêm Yết'] = row['KLCPNY']
                obj['Giá Đóng'] = row['ClosePrice']
                obj['Giá Đóng Ngày Trước'] = row['PriorClosePrice']
                obj['Giá Trần'] = row['CeilingPrice']
                obj['Giá Sàn'] = row['FloorPrice']
                obj['Tổng Khối Lượng Giao Dịch'] = row['TotalVol']
                obj['Tổng Giá Trị Giao Dịch'] = row['TotalVal']
                obj['Giá Trị Vốn Hóa Thị Trường'] = row['MarketCapital']
                obj['Giá Cao Nhất Ngày'] = row['HighestPrice']
                obj['Giá Thấp Nhất Ngày'] = row['LowestPrice']
                obj['Khác Biệt Cao Thấp'] = row['DiffHighLow']
                obj['Giá Mở'] = row['OpenPrice']
                obj['Giá Đóng'] = row['LastPrice']
                obj['Giá Điều Chỉnh'] = row['AdjustPrice']
                obj['Khối Lượng Điều Chỉnh'] = row['AdjustVolume']
                obj['Khối Lượng Mua Trung Bình'] = row['BuyAvg']
                obj['Khối Lượng Bán Trung Bình'] = row['SellAvg']
                obj['Số Lệnh Đặt Mua'] = row['TotalBuyTrade']
                obj['Số Lệnh Đặt Bán'] = row['TotalSellTrade']
                obj['Khác Biệt Số Lệnh Mua Bán'] = row['DiffBuySellTrade']
                obj['Tổng Khối Lượng Mua'] = row['TotalBuyVol']
                obj['Tổng Khối Lượng Bán'] = row['TotalSellVol']
                obj['Khác Biệt Khối Lượng Mua Bán'] = row['DiffBuySellVol']
                obj['Tổng Khối Lượng Giao Dịch Khớp Lệnh'] = row['MT_TotalVol']
                obj['Tổng Giá Trị Giao Dịch Khớp Lệnh'] = row['MT_TotalVal']
                obj['Tổng Khối Lượng Giao Dịch Thỏa Thuận'] = row['PT_TotalVol']
                obj['Tổng Giá Trị Giao Dịch Thỏa Thuận'] = row['PT_TotalVal']
                obj['Owned Ratio'] = row['OwnedRatio']
                obj['Dividend'] = row['Dividend']
                obj['EPS'] = row['EPS']
                obj['P/E'] = row['PE']
                obj['FEPS'] = row['FEPS']
                obj['BVPS'] = row['BVPS']
                obj['PB'] = row['PB']
                obj['Khối Lượng Nước Ngoài Mua'] = row['ForeignBuyVol']
                obj['Giá Trị Nước Ngoài Mua'] = row['ForeignBuyVal']
                obj['Khối Lượng Nước Ngoài Bán'] = row['ForeignSellVol']
                obj['Giá Trị Nước Ngoài Bán'] = row['ForeignSellVal']
                # print(obj)
                yield(obj)
            except:
                pass

        # quay lai parse
        ck_index =  response.meta["ck_index"]

        try:
            yield FormRequest('https://finance.vietstock.vn/data/gettradingresult',
                                  method="POST",
                                  callback= self.parse_bao_cao,
                                  formdata={
                                      "Code": self.lst_cp[ck_index+1],
                                      "OrderBy": "",
                                      "OrderDirection": "desc",
                                      "PageIndex": "1",
                                      "FromDate": "2019-10-04",
                                      "ToDate": "2020-10-04",
                                      "ExportType": "default",
                                      "Cols": "Room%2CRoomCL%2CRoomCLPT%2CKL_M_GDKL%2CKL_MPT_GDKL%2CGT_M_GDKL%2CGT_MPT_GDKL%2CKL_B_GDKL%2CKL_BPT_GDKL%2CGT_B_GDKL%2CGT_BPT_GDKL%2CCL_GT_MB%2CCL_KL_MB",
                                      "ExchangeID": "7",
                                      "PageSize": "251"
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
                                      "ck_index": ck_index + 1,
                                      "isShowLogin": isShowLogin,
                                      "language": language,
                                      "ASP_sessionId": ASP_sessionId,
                                      "verifyToken": verifyToken
                                  }
                              )
        except:
            pass