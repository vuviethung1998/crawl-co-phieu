from scrapy.spiders import CrawlSpider
from datetime import datetime,date
from scrapy import Request, FormRequest
from crawl_cp_68.config.ListStock import *
from crawl_cp_68.import_setting import *
import os

class StockDataDownloaderSpider(CrawlSpider):
    name = "stock_downloader_cafe_68"


    def __init__(self, **kwargs):
        super(StockDataDownloaderSpider, self).__init__(**kwargs)
        self.allowed_domains = ['www.cophieu68.vn']

        # lst_cp = VN30 + HNX30
        lst_cp = ['TVC']
        self.start_urls = ["https://www.cophieu68.vn/export/metastock.php?id={}".format(cp) for cp in lst_cp ]
        str_date = str(date.today().strftime("%d-%m-%y"))
        settings['CRAWLER_COLLECTION'] = 'CRAWLER_CATEGORY_DETAIL_{}'.format(str_date)

    def start_requests(self):
        url = 'https://www.cophieu68.vn/account/login.php'
        formdata = {
            'username': 'vuviethung.98.hust@gmail.com',
            'tpassword': 'vuviethung',
            'ajax': '1',
            'login': '1'
        }
        yield FormRequest(url=url, formdata=formdata, callback=self.after_login)

    def after_login(self):
        for url in self.start_urls:
            yield Request(
                url=url,
                callback=self.parse
            )

    def parse(self,response):
        url = response.url
        stock_name = url.split("=")[1]
        file_dir = os.getcwd() + "/crawl_cp_68/data/lich_su_giao_dich/{}.txt".format(stock_name)
        print("FILE-DIR: "  + file_dir)
        with open(file_dir, 'wb') as f:
            print("---------------------")
            print(response.body)
            f.write(response.body)

