import json
from scrapy.spiders import CrawlSpider
from scrapy import Request, FormRequest
import random
from crawl_cp_finance_stock.import_setting import *
from crawl_cp_finance_stock.config.ListStock import *

class FinanceStockChiSoTaiChinhQuarterSpider(CrawlSpider):
    name = "finance_stock_chi_so_tai_chinh_quarter"

    def __init__(self, **kwargs):
        super(FinanceStockChiSoTaiChinhQuarterSpider, self).__init__(**kwargs)
        self.allowed_domains = ['finance.vietstock.vn']

        self.lst_cp =  HOSE + HNX

        self.start_urls = ['https://finance.vietstock.vn']
        settings['CRAWLER_COLLECTION'] = "CHI_SO_TAI_CHINH_QUARTER"

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
                                callback= self.parse_chi_so_tai_chinh,
                                formdata={
                                   "Code": self.lst_cp[ck_index],
                                   "ReportType":"CSTC",
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


    def parse_chi_so_tai_chinh(self, response):
        isShowLogin = response.meta["isShowLogin"]
        language = response.meta["language"]
        ASP_sessionId = response.meta["ASP_sessionId"]
        verifyToken = response.meta["verifyToken"]

        thong_tin = json.loads(response.body)[0]
        chi_so_tai_chinh = json.loads(response.body)[1]

        for i in range(0,4):
            try:
                obj = {}
                obj["Chung_khoan_name"] = response.meta["ck_name"]
                obj["Quarter"] = thong_tin[i]["TermCode"]
                obj["Year"] = thong_tin[i]["YearPeriod"]
                obj["ID_Chung_khoan"] = thong_tin[i]["CompanyID"]


                obj["Thu nhập trên mỗi cổ phần của 4 quý gần nhất (EPS)"] = chi_so_tai_chinh["Nhóm chỉ số Định giá"][0]["Value{}".format(str(4-i))]
                obj["Giá trị sổ sách của cổ phiếu (BVPS)"] = chi_so_tai_chinh["Nhóm chỉ số Định giá"][1]["Value{}".format(str(4-i))]
                obj["Chỉ số giá thị trường trên thu nhập (P/E)"] = chi_so_tai_chinh["Nhóm chỉ số Định giá"][2]["Value{}".format(str(4-i))]
                obj["Chỉ số giá thị trường trên giá trị sổ sách (P/B)"] = chi_so_tai_chinh["Nhóm chỉ số Định giá"][3]["Value{}".format(str(4-i))]
                obj["Chỉ số giá thị trường trên doanh thu thuần (P/S)"] = chi_so_tai_chinh["Nhóm chỉ số Định giá"][4]["Value{}".format(str(4-i))]
                obj["Tỷ suất cổ tức"] =  chi_so_tai_chinh["Nhóm chỉ số Định giá"][5]["Value{}".format(str(4-i))]
                obj["Beta"] = chi_so_tai_chinh["Nhóm chỉ số Định giá"][6]["Value{}".format(str(4-i))]
                obj["Giá trị doanh nghiệp trên lợi nhuận trước thuế và lãi vay (EV/EBIT)"] = chi_so_tai_chinh["Nhóm chỉ số Định giá"][7]["Value{}".format(str(4-i))]
                obj["Giá trị doanh nghiệp trên lợi nhuận trước thuế, khấu hao và lãi vay (EV/EBITDA)"] = chi_so_tai_chinh["Nhóm chỉ số Định giá"][8]["Value{}".format(str(4-i))]

                obj["Tỷ suất lợi nhuận gộp biên"] = chi_so_tai_chinh["Nhóm chỉ số Sinh lợi"][0]["Value{}".format(str(4-i))]
                obj["Tỷ lệ lãi EBIT"] = chi_so_tai_chinh["Nhóm chỉ số Sinh lợi"][1]["Value{}".format(str(4-i))]
                obj["Tỷ lệ lãi EBITDA"] = chi_so_tai_chinh["Nhóm chỉ số Sinh lợi"][2]["Value{}".format(str(4-i))]
                obj["Tỷ suất sinh lợi trên doanh thu thuần"] = chi_so_tai_chinh["Nhóm chỉ số Sinh lợi"][3]["Value{}".format(str(4-i))]
                obj["Tỷ suất lợi nhuận trên vốn chủ sở hữu bình quân (ROEA)"] = chi_so_tai_chinh["Nhóm chỉ số Sinh lợi"][4]["Value{}".format(str(4-i))]
                obj["Tỷ suất sinh lợi trên vốn dài hạn bình quân (ROCE)"] = chi_so_tai_chinh["Nhóm chỉ số Sinh lợi"][5]["Value{}".format(str(4-i))]
                obj["Tỷ suất sinh lợi trên tổng tài sản bình quân (ROAA)"] = chi_so_tai_chinh["Nhóm chỉ số Sinh lợi"][6]["Value{}".format(str(4-i))]

                obj["Tăng trưởng  doanh thu thuần"] = chi_so_tai_chinh["Nhóm chỉ số Tăng trưởng"][0]["Value{}".format(str(4-i))]
                obj["Tăng trưởng  lợi nhuận gộp"] = chi_so_tai_chinh["Nhóm chỉ số Tăng trưởng"][1]["Value{}".format(str(4-i))]
                obj["Tăng trưởng lợi nhuận trước thuế"] = chi_so_tai_chinh["Nhóm chỉ số Tăng trưởng"][2]["Value{}".format(str(4-i))]
                obj["Tăng trưởng lợi nhuận sau thuế của CĐ công ty mẹ"] = chi_so_tai_chinh["Nhóm chỉ số Tăng trưởng"][3]["Value{}".format(str(4-i))]
                obj["Tăng trưởng tổng tài sản"] = chi_so_tai_chinh["Nhóm chỉ số Tăng trưởng"][4]["Value{}".format(str(4-i))]
                obj["Tăng trưởng nợ dài hạn"] = chi_so_tai_chinh["Nhóm chỉ số Tăng trưởng"][5]["Value{}".format(str(4-i))]
                obj["Tăng trưởng nợ phải trả"] = chi_so_tai_chinh["Nhóm chỉ số Tăng trưởng"][6]["Value{}".format(str(4-i))]
                obj["Tăng trưởng vốn điều lệ"] = chi_so_tai_chinh["Nhóm chỉ số Tăng trưởng"][7]["Value{}".format(str(4-i))]

                obj["Tỷ số thanh toán bằng tiền mặt"] = chi_so_tai_chinh["Nhóm chỉ số Thanh khoản"][0]["Value{}".format(str(4-i))]
                obj["Tỷ số thanh toán nhanh"] = chi_so_tai_chinh["Nhóm chỉ số Thanh khoản"][1]["Value{}".format(str(4-i))]
                obj["Tỷ số thanh toán nhanh  (Đã loại trừ HTK, Phải thu ngắn hạn - Tham khảo)"] = chi_so_tai_chinh["Nhóm chỉ số Thanh khoản"][2]["Value{}".format(str(4-i))]
                obj["Tỷ số thanh toán hiện hành (ngắn hạn)"] = chi_so_tai_chinh["Nhóm chỉ số Thanh khoản"][3]["Value{}".format(str(4-i))]
                obj["Khả năng thanh toán lãi vay"] = chi_so_tai_chinh["Nhóm chỉ số Thanh khoản"][4]["Value{}".format(str(4-i))]

                obj["Vòng quay phải thu khách hàng"] = chi_so_tai_chinh["Nhóm chỉ số Hiệu quả hoạt động"][0]["Value{}".format(str(4-i))]
                obj["Thời gian thu tiền khách hàng bình quân"] = chi_so_tai_chinh["Nhóm chỉ số Hiệu quả hoạt động"][1]["Value{}".format(str(4-i))]
                obj["Vòng quay hàng tồn kho"] = chi_so_tai_chinh["Nhóm chỉ số Hiệu quả hoạt động"][2]["Value{}".format(str(4-i))]
                obj["Thời gian tồn kho bình quân"] = chi_so_tai_chinh["Nhóm chỉ số Hiệu quả hoạt động"][3]["Value{}".format(str(4-i))]
                obj["Vòng quay phải trả nhà cung cấp"] = chi_so_tai_chinh["Nhóm chỉ số Hiệu quả hoạt động"][4]["Value{}".format(str(4-i))]
                obj["Thời gian trả tiền khách hàng bình quân"] = chi_so_tai_chinh["Nhóm chỉ số Hiệu quả hoạt động"][5]["Value{}".format(str(4-i))]
                obj["Vòng quay tài sản cố định (Hiệu suất sử dụng tài sản cố định)"] = chi_so_tai_chinh["Nhóm chỉ số Hiệu quả hoạt động"][6]["Value{}".format(str(4-i))]
                obj["Vòng quay tổng tài sản (Hiệu suất sử dụng toàn bộ tài sản)"] = chi_so_tai_chinh["Nhóm chỉ số Hiệu quả hoạt động"][7]["Value{}".format(str(4-i))]
                obj["Vòng quay vốn chủ sở hữu"] = chi_so_tai_chinh["Nhóm chỉ số Hiệu quả hoạt động"][8]["Value{}".format(str(4-i))]

                obj["Tỷ số Nợ ngắn hạn trên Tổng nợ phải trả"] = chi_so_tai_chinh["Nhóm chỉ số Đòn bẩy tài chính"][0]["Value{}".format(str(4-i))]
                obj["Tỷ số Nợ vay trên Tổng tài sản"] = chi_so_tai_chinh["Nhóm chỉ số Đòn bẩy tài chính"][1]["Value{}".format(str(4-i))]
                obj["Tỷ số Nợ vay trên Tổng tài sản"] = chi_so_tai_chinh["Nhóm chỉ số Đòn bẩy tài chính"][2]["Value{}".format(str(4-i))]
                obj["Tỷ số Vốn chủ sở hữu trên Tổng tài sản"] = chi_so_tai_chinh["Nhóm chỉ số Đòn bẩy tài chính"][3]["Value{}".format(str(4-i))]
                obj["Tỷ số Vốn chủ sở hữu trên Tổng tài sản"] = chi_so_tai_chinh["Nhóm chỉ số Đòn bẩy tài chính"][4]["Value{}".format(str(4-i))]
                obj["Tỷ số Nợ vay trên Vốn chủ sở hữu"] = chi_so_tai_chinh["Nhóm chỉ số Đòn bẩy tài chính"][5]["Value{}".format(str(4-i))]
                obj["Tỷ số Nợ trên Vốn chủ sở hữu"] = chi_so_tai_chinh["Nhóm chỉ số Đòn bẩy tài chính"][6]["Value{}".format(str(4-i))]

                obj["Tỷ số dòng tiền HĐKD trên doanh thu thuần"] = chi_so_tai_chinh["Nhóm chỉ số Dòng tiền"][0]["Value{}".format(str(4-i))]
                obj["Khả năng chi trả nợ ngắn hạn từ dòng tiền HĐKD"] = chi_so_tai_chinh["Nhóm chỉ số Dòng tiền"][1]["Value{}".format(str(4-i))]
                obj["Khả năng chi trả nợ ngắn hạn từ lưu chuyển tiền thuần trong kỳ"] = chi_so_tai_chinh["Nhóm chỉ số Dòng tiền"][2]["Value{}".format(str(4-i))]
                obj["Tỷ lệ dồn tích (Phương pháp Cân đối kế toán)"] = chi_so_tai_chinh["Nhóm chỉ số Dòng tiền"][3]["Value{}".format(str(4-i))]
                obj["Tỷ lệ dồn tích (Phương pháp Dòng tiền)"] = chi_so_tai_chinh["Nhóm chỉ số Dòng tiền"][4]["Value{}".format(str(4-i))]
                obj["Dòng tiền từ HĐKD trên Tổng tài sản"] = chi_so_tai_chinh["Nhóm chỉ số Dòng tiền"][5]["Value{}".format(str(4-i))]
                obj["Dòng tiền từ HĐKD trên Vốn chủ sở hữu"] = chi_so_tai_chinh["Nhóm chỉ số Dòng tiền"][6]["Value{}".format(str(4-i))]
                obj["Dòng tiền từ HĐKD trên Lợi nhuận thuần từ HĐKD"] = chi_so_tai_chinh["Nhóm chỉ số Dòng tiền"][7]["Value{}".format(str(4-i))]
                obj["Khả năng thanh toán nợ từ dòng tiền HĐKD"] = chi_so_tai_chinh["Nhóm chỉ số Dòng tiền"][8]["Value{}".format(str(4-i))]
                obj["Dòng tiền từ HĐKD trên mỗi cổ phần (CPS)"] = chi_so_tai_chinh["Nhóm chỉ số Dòng tiền"][9]["Value{}".format(str(4-i))]

                obj["Giá vốn hàng bán/Doanh thu thuần"] = chi_so_tai_chinh["Cơ cấu Chi phí"][0]["Value{}".format(str(4-i))]
                obj["Chi phí bán hàng/Doanh thu thuần"] = chi_so_tai_chinh["Cơ cấu Chi phí"][1]["Value{}".format(str(4-i))]
                obj["Chi phí quản lý doanh nghiệp/Doanh thu thuần"] = chi_so_tai_chinh["Cơ cấu Chi phí"][2]["Value{}".format(str(4-i))]
                obj["Chi phí lãi vay/Doanh thu thuần"] = chi_so_tai_chinh["Cơ cấu Chi phí"][3]["Value{}".format(str(4-i))]

                obj["Tài sản ngắn hạn/Tổng tài sản"] = chi_so_tai_chinh["Cơ cấu Tài sản ngắn hạn"][0]["Value{}".format(str(4-i))]
                obj["Tiền/Tài sản ngắn hạn"] = chi_so_tai_chinh["Cơ cấu Tài sản ngắn hạn"][1]["Value{}".format(str(4-i))]
                obj["Đầu tư tài chính ngắn hạn/Tài sản ngắn hạn"] = chi_so_tai_chinh["Cơ cấu Tài sản ngắn hạn"][2]["Value{}".format(str(4-i))]
                obj["Phải thu ngắn hạn/Tài sản ngắn hạn"] = chi_so_tai_chinh["Cơ cấu Tài sản ngắn hạn"][3]["Value{}".format(str(4-i))]
                obj["Hàng tồn kho/Tài sản ngắn hạn"] = chi_so_tai_chinh["Cơ cấu Tài sản ngắn hạn"][4]["Value{}".format(str(4-i))]
                obj["Tài sản ngắn hạn khác/Tài sản ngắn hạn"] = chi_so_tai_chinh["Cơ cấu Tài sản ngắn hạn"][5]["Value{}".format(str(4-i))]

                obj["Tài sản dài hạn/Tổng tài sản"] = chi_so_tai_chinh["Cơ cấu Tài sản dài hạn"][0]["Value{}".format(str(4-i))]
                obj["Tài sản cố định/Tổng tài sản"] = chi_so_tai_chinh["Cơ cấu Tài sản dài hạn"][1]["Value{}".format(str(4-i))]
                obj["Tài sản cố định hữu hình/Tài sản cố định"] = chi_so_tai_chinh["Cơ cấu Tài sản dài hạn"][2]["Value{}".format(str(4-i))]
                obj["Tài sản thuê tài chính/Tài sản cố định"] = chi_so_tai_chinh["Cơ cấu Tài sản dài hạn"][3]["Value{}".format(str(4-i))]
                obj["Tài sản vô hình/Tài sản cố định"] = chi_so_tai_chinh["Cơ cấu Tài sản dài hạn"][4]["Value{}".format(str(4-i))]
                obj["Xây dựng chuẩn bị trong quá trình/Tài sản cố định"] = chi_so_tai_chinh["Cơ cấu Tài sản dài hạn"][5]["Value{}".format(str(4-i))]
                print(obj)
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
                                      callback= self.parse_chi_so_tai_chinh,
                                      formdata={
                                          "Code": self.lst_cp[ck_index],
                                          "ReportType": "CSTC",
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
                                      callback= self.parse_chi_so_tai_chinh,
                                      formdata={
                                          "Code": self.lst_cp[ck_index+1],
                                          "ReportType":"CSTC",
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
