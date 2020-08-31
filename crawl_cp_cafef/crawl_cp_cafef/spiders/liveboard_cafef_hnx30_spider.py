from scrapy_splash import SplashRequest
from scrapy.spiders import CrawlSpider
from datetime import datetime, date
import time
from crawl_cp_cafef.config.ListStock import *
from crawl_cp_cafef.import_setting import *

class LiveCafefSpider(CrawlSpider):
    name = "liveboard_cafef_hnx30"
    def __init__(self, **kwargs):
        super(LiveCafefSpider, self).__init__(**kwargs)
        self.allowed_domains = ['cafef.vn']
        self.start_urls = ['http://liveboard.cafef.vn/?center=2']
        str_date = str(date.today().strftime("%d-%m-%y"))
        settings['CRAWLER_COLLECTION'] = 'CRAWLER_CAFEF_LIVEBOARD_HNX30_{}'.format(str_date)

    script = """
        function main(splash, args)
          assert(splash:go(args.url))
          assert(splash:wait(1))
          return {
            html = splash:html()
          }
        end
        """

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                endpoint='execute',
                args={'lua_source': self.script}
            )

    def parse(self, response):
        # check neu co ma POW la VN30
        # neu co ma SHB la HNX30
        lst_cp = HNX30
        print(lst_cp)
        for cp in lst_cp:
            obj ={}
            now = datetime.now()
            obj['timestamp'] = time.time()

            # ----------------------------
            ma_ck = response.xpath('//*[@id="{}_a"]/label/text()'.format(cp)).extract()
            if len(ma_ck) > 0:
                obj['ma_ck'] = ma_ck[0]
            
                
            # ----------------------------
            gia_tham_chieu = response.xpath('//*[@id="{}_b"]/text()'.format(cp)).extract()
            if len(gia_tham_chieu) > 0:
                obj['gia_tham_chieu'] = gia_tham_chieu[0]
            
                
            # ----------------------------
            gia_tran = response.xpath('//*[@id="{}_c"]/text()'.format(cp)).extract()
            if len(gia_tran) > 0:
                obj['gia_tran'] = gia_tran[0]
            
                
            # ----------------------------
            gia_san = response.xpath('//*[@id="{}_d"]/text()'.format(cp)).extract()
            if len(gia_san) > 0:
                obj['gia_san'] = gia_san[0]
            
                
            # ----------------------------
            gia_3_buy = response.xpath('//*[@id="{}_e"]/text()'.format(cp)).extract()
            if len(gia_3_buy) > 0:
                obj['gia_3_buy'] = gia_3_buy[0]
            
                
            # ----------------------------
            kl_3_buy = response.xpath('//*[@id="{}_f"]/text()'.format(cp)).extract()
            if len(kl_3_buy) > 0:
                obj['kl_3_buy'] = ma_ck[0]
            
                
            # ----------------------------
            gia_2_buy = response.xpath('//*[@id="{}_g"]/text()'.format(cp)).extract()
            if len(gia_2_buy) > 0:
                obj['gia_2_buy'] = gia_2_buy[0]
            
                
            # ----------------------------
            kl_2_buy = response.xpath('//*[@id="{}_h"]/text()'.format(cp)).extract()
            if len(kl_2_buy) > 0:
                obj['kl_2_buy'] = kl_2_buy[0]
            
                
            # ----------------------------
            gia_1_buy = response.xpath('//*[@id="{}_i"]/text()'.format(cp)).extract()
            if len(gia_1_buy) > 0:
                obj['gia_1_buy'] = gia_1_buy[0]
            
                
            # ----------------------------
            kl_1_buy = response.xpath('//*[@id="{}_j"]/text()'.format(cp)).extract()
            if len(kl_1_buy) > 0:
                obj['kl_1_buy'] = kl_1_buy[0]
            
                
            # ----------------------------
            tang_giam = response.xpath('//*[@id="{}_k"]/text()'.format(cp)).extract()
            if len(tang_giam) > 0:
                obj['tang_giam'] = tang_giam[0]
            
                
            # ----------------------------
            gia = response.xpath('//*[@id="{}_l"]/text()'.format(cp)).extract()
            if len(gia) > 0:
                obj['gia_khop_lenh'] = gia[0]
            
                
            # ----------------------------
            khoi_luong = response.xpath('//*[@id="{}_m"]/text()'.format(cp)).extract()
            if len(khoi_luong) > 0:
                obj['khoi_luong_khop_lenh'] = khoi_luong[0]
            
                
            # ----------------------------
            tong_kl = response.xpath('//*[@id="{}_n"]/text()'.format(cp)).extract()
            if len(tong_kl) > 0:
                obj['tong_kl'] = tong_kl[0]
            
                
            # ----------------------------
            gia_1_sell = response.xpath('//*[@id="{}_o"]/text()'.format(cp)).extract()
            if len(gia_1_sell) > 0:
                obj['gia_1_sell'] = gia_1_sell[0]
            
                
            # ----------------------------
            kl_1_sell = response.xpath('//*[@id="{}_p"]/text()'.format(cp)).extract()
            if len(kl_1_sell) > 0:
                obj['kl_1_sell'] = kl_1_sell[0]
            
                
            # ----------------------------
            gia_2_sell = response.xpath('//*[@id="{}_q"]/text()'.format(cp)).extract()
            gia_2_sell = response.xpath('//*[@id="{}_q"]/text()'.format(cp)).extract()
            if len(gia_2_sell) > 0:
                obj['gia_2_sell'] = gia_2_sell[0]
            
                
            # ----------------------------
            kl_2_sell = response.xpath('//*[@id="{}_r"]/text()'.format(cp)).extract()
            if len(kl_2_sell) > 0:
                obj['kl_2_sell'] = kl_2_sell[0]
            
                
            # ----------------------------
            gia_3_sell = response.xpath('//*[@id="{}_s"]/text()'.format(cp)).extract()
            if len(gia_3_sell) > 0:
                obj['gia_3_sell'] = gia_3_sell[0]
            
                
            # ----------------------------
            kl_3_sell = response.xpath('//*[@id="{}_t"]/text()'.format(cp)).extract()
            if len(kl_3_sell) > 0:
                obj['kl_3_sell'] = kl_3_sell[0]
            
                
            # ----------------------------
            gia_cao = response.xpath('//*[@id="{}_v"]/text()'.format(cp)).extract()
            if len(gia_cao) > 0:
                obj['gia_cao'] = gia_cao[0]
            
                
            # ----------------------------
            gia_thap = response.xpath('//*[@id="{}_w"]/text()'.format(cp)).extract()
            if len(gia_thap) > 0:
                obj['gia_thap'] = gia_thap[0]
            
                
            # ----------------------------
            dtnn_mua = response.xpath('//*[@id="{}_x"]/text()'.format(cp)).extract()
            if len(dtnn_mua) > 0:
                obj['dtnn_mua'] = dtnn_mua[0]

            yield obj