import json
from scrapy.spiders import CrawlSpider
from scrapy import Request, FormRequest
import random
from crawl_cp_tvsi.import_setting import *
from crawl_cp_tvsi.config.ListStock import *
from bs4 import BeautifulSoup as soup

class TvsiStockTopCompanySpider(CrawlSpider):
    name = "tvsi_stock_chi_tieu_quan_trong"

    def __init__(self, **kwargs):
        super(TvsiStockTopCompanySpider, self).__init__(**kwargs)
        self.allowed_domains = ['finance.tvsi.com.vn']

        self.lst_cp =  HOSE + HNX

        self.start_urls = ['https://finance.tvsi.com.vn'] # /tools/topCompanyPart
        settings['CRAWLER_COLLECTION'] = "CHI_TIEU_QUAN_TRONG"

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, callback=self.parse, meta={
                "ck_index" : 0,
                # "currentPage" : 1
            })

    def parse(self, response):
        # current_page = response.meta['currentPage']
        ck_index = response.meta["ck_index"]

        yield Request('https://finance.tvsi.com.vn/Enterprises/ChiTieuQuanTrong?symbol={}&period=1&currentPage=1&_=1607647761883'.format(self.lst_cp[ck_index]),
                      method="GET",
                      callback= self.parse_chi_tieu_quan_trong,
                      headers= {
                          "X-Requested-With": "XMLHttpRequest",
                          # "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                          'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
                          "User-Agent":  random.choice(settings.get('USER_AGENT_LIST')),
                      },
                      meta= {
                          "ck_index": ck_index,
                      }
                      )

    def parse_chi_tieu_quan_trong(self, response):

        chi_tieu_quan_trong = response.text
        s = soup(chi_tieu_quan_trong, features='lxml').table

        rows = s.find_all('tr')
        lst_data = []

        for i in range(5):
            data = {"Chung_khoan_name": self.lst_cp[response.meta["ck_index"]],'Năm': 0, 'Tổng tài sản': 0, "Vốn chủ sở hữu": 0,
                    "Doanh thu thuần": 0, "Lợi nhuận gộp": 0, "LN từ hoạt động SXKD": 0,
                    "Lợi nhuận sau thuế": 0, "Lợi ích cổ đông công ty mẹ": 0,
                    "Biên lãi gộp (trailing 4 quý) %": 0, "EPS (trailing 4 quý)": 0,
                    "ROA (trailing 4 quý) %": 0, "ROE (trailing 4 quý) %": 0}
            lst_data.append(data)

        for irow in range(len(rows)):
            cols = rows[irow].find_all("td")

            if irow == 0:
                for icol in range(len(cols)):
                    if icol > 1:
                        lst_data[icol-2]['Năm'] = cols[icol].text.split('(')[0]
            elif irow == 1:
                for icol in range(len(cols)):
                    if icol > 1:
                        lst_data[icol-2]['Tổng tài sản'] = cols[icol].string
            elif irow == 2:
                for icol in range(len(cols)):
                    if icol > 1:
                        lst_data[icol-2]['Vốn chủ sở hữu'] = cols[icol].string
            elif irow == 3:
                for icol in range(len(cols)):
                    if icol > 1:
                        lst_data[icol-2]['Doanh thu thuần'] = cols[icol].string
            elif irow == 4:
                for icol in range(len(cols)):
                    if icol > 1:
                        lst_data[icol-2]['Lợi nhuận gộp'] = cols[icol].string
            elif irow == 5:
                for icol in range(len(cols)):
                    if icol > 1:
                        lst_data[icol-2]['LN từ hoạt động SXKD'] = cols[icol].string
            elif irow == 6:
                for icol in range(len(cols)):
                    if icol > 1:
                        lst_data[icol-2]['Lợi nhuận sau thuế'] = cols[icol].string
            elif irow == 7:
                for icol in range(len(cols)):
                    if icol > 1:
                        lst_data[icol-2]['Lợi ích cổ đông công ty mẹ'] = cols[icol].string
            elif irow == 8:
                for icol in range(len(cols)):
                    if icol > 1:
                        lst_data[icol-2]['Biên lãi gộp (trailing 4 quý) %'] = cols[icol].string
            elif irow == 9:
                for icol in range(len(cols)):
                    if icol > 1:
                        lst_data[icol-2]['EPS (trailing 4 quý)'] = cols[icol].string
            elif irow == 10:
                for icol in range(len(cols)):
                    if icol > 1:
                        lst_data[icol-2]['ROA (trailing 4 quý) %'] = cols[icol].string
            elif irow == 11:
                for icol in range(len(cols)):
                    if icol > 1:
                        lst_data[icol-2]['ROE (trailing 4 quý) %'] = cols[icol].string

        #move data to DB
        for data in lst_data:
            yield data


        ck_index =  response.meta["ck_index"] + 1

        try:
            yield Request('https://finance.tvsi.com.vn/Enterprises/ChiTieuQuanTrong?symbol={}&period=1&currentPage=1&_=1607647761883'.format(self.lst_cp[ck_index]),
                              method="GET",
                              callback= self.parse_chi_tieu_quan_trong,
                              headers= {
                                  "X-Requested-With": "XMLHttpRequest",
                                  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                  'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
                                  "User-Agent":  random.choice(settings.get('USER_AGENT_LIST')),
                              },
                              meta= {
                                  "ck_index": ck_index+1
                              }
                          )
        except:
            pass
