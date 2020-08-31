from scrapy_splash import SplashRequest
from scrapy.spiders import CrawlSpider
from datetime import datetime, date
import time
from crawl_cp_cafef.config.ListStock import *
from crawl_cp_cafef.import_setting import *

ind = 0 #  global variables  

class CafefLichSuGiaoDich(CrawlSpider):
    name = "cafef_trading_history"

    def __init__(self, **kwargs):
        super(CafefLichSuGiaoDich, self).__init__(**kwargs)
        self.allowed_domains = ['cafef.vn']

        # lst_cp =  HNX30 + VN30
        lst_cp =  ["TVC"]
        self.start_urls = ['http://s.cafef.vn/Lich-su-giao-dich-{}-2.chn'.format(cp) for cp in lst_cp ]
        # str_date = str(date.today().strftime("%d-%m-%y"))
        settings['CRAWLER_COLLECTION'] = 'TRADING_HISTORY_DAILY'

        self.script = self.get_script()


    def get_script(self):
        global ind 
        ind += 1 
        script = """
            function main(splash, args)
            assert(splash:go(args.url))
            assert(splash:wait(1))
            assert(splash:runjs("__doPostBack('ctl00$ContentPlaceHolder1$ctl03$pager1', '{ind}')"))
            return {{
                html = splash:html(),
                url = splash:url()
            }}
            end
            """
        return script.format(ind = ind)

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, 
                callback=self.parse,
                endpoint='render.html'
            )

    def parse(self, response):
        # bang co mac dinh 20 dong 

        # voi dong le thi _itemTR / dong chan thi _Tr1

        for i in range(1,21):
            obj = {}
            #  neu < 10 thi them 0 vao truoc string
            num_present = ''
            rand_num = ''
            if i < 10:
                num_present = '0' + str(i)
            else:
                num_present = str(i)
            #  root 
            if i % 2 == 1:
                rand_name = 'itemTR'
            else:
                rand_name = 'Tr1'
            
            root_xpath = '//*[@id="ctl00_ContentPlaceHolder1_ctl03_rptData_ctl{}_{}"]'.format(num_present, rand_name)

            date =  root_xpath + '/td[1]/text()'
            obj['date'] = response.xpath(date).extract()[0]
            
            price = root_xpath + '/td[2]/text()'
            obj['price'] = response.xpath(price).extract()[0]

            change = root_xpath + '/td[2]/span/text()'
            obj['change'] = response.xpath(change).extract()[0]

            so_lenh_mua = root_xpath + '/td[3]/text()'
            obj['so_lenh_mua'] = response.xpath(so_lenh_mua).extract()[0]

            khoi_luong_mua = root_xpath + '/td[4]/text()'
            obj['khoi_luong_mua'] = response.xpath(khoi_luong_mua).extract()[0]

            khoi_luong_trung_binh_tren_mua = root_xpath + '/td[5]/text()'
            obj['khoi_luong_trung_binh_tren_mua'] = response.xpath(khoi_luong_trung_binh_tren_mua).extract()[0]

            so_lenh_ban = root_xpath + '/td[6]/text()'
            obj['so_lenh_ban'] = response.xpath(so_lenh_ban).extract()[0]

            khoi_luong_ban = root_xpath + '/td[7]/text()' 
            obj['khoi_luong_ban'] = response.xpath(khoi_luong_ban).extract()[0]

            khoi_luong_trung_binh_tren_ban = root_xpath + '/td[8]/text()'
            obj['khoi_luong_trung_binh_tren_ban'] = response.xpath(khoi_luong_trung_binh_tren_ban).extract()[0]

            chenh_lech_khoi_luong_mua_ban =  root_xpath + '/td[9]/text()'
            obj['chenh_lech_khoi_luong_mua_ban'] = response.xpath(chenh_lech_khoi_luong_mua_ban).extract()[0]

            yield obj
        print("---------------------------------------")
        print(self.script)
        print("---------------------------------------")

        yield  SplashRequest(
            url=response.url,
            callback=self.parse,
            meta={
                "splash": {"endpoint": "execute", "args": {"lua_source": self.script}}
            }
        )




        