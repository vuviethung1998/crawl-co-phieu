# from scrapy_splash import SplashRequest
from scrapy.spiders import CrawlSpider
from datetime import datetime
from crawl_cp_68.config.ListStock import *

class LiveCafefSpider(CrawlSpider):
    name = "liveboard_cafef"
    def __init__(self, **kwargs):
        super(LiveCafefSpider, self).__init__(**kwargs)
        self.allowed_domains = ['cafef.vn']
        self.start_urls = ['http://liveboard.cafef.vn/?center=1',
                           'http://liveboard.cafef.vn/?center=2']
        # settings['CRAWLER_COLLECTION'] = 'CRAWLER_CAFEF_LIVEBOARD'

    def start_requests(self):
        # for url in self.start_urls:
        #     yield SplashRequest(url, self.parse,
        #         endpoint='render.html',
        #         args={'wait': 1}
        #     )
        pass

    def parse(self, response):
        # check neu co ma POW la VN30
        # neu co ma SHB la HNX30
        lst_cp = []
        if(len(response.xpath('//*[@id="{}_a"]/label/text()'.format('PNJ')).extract()) != 0):
            lst_cp = VN30
        else:
            lst_cp = HNX30
        for cp in lst_cp:
            obj ={}
            now = datetime.now()
            obj['timestamp'] = now.strftime("%d/%m/%Y %H:%M:%S")

            # ----------------------------
            ma_ck = response.xpath('//*[@id="{}_a"]/label/text()'.format(cp)).extract()
            if len(ma_ck) > 0:
                obj['ma_ck'] = ma_ck[0]
            else:
                print("error")
            # ----------------------------
            gia_tham_chieu = response.xpath('//*[@id="{}_b"]/text()'.format(cp)).extract()
            if len(gia_tham_chieu) > 0:
                obj['gia_tham_chieu'] = gia_tham_chieu[0]
            else:
                print("error")
            # ----------------------------
            gia_tran = response.xpath('//*[@id="{}_c"]/text()'.format(cp)).extract()
            if len(gia_tran) > 0:
                obj['gia_tran'] = gia_tran[0]
            else:
                print("error")
            # ----------------------------
            gia_san = response.xpath('//*[@id="{}_d"]/text()'.format(cp)).extract()
            if len(gia_san) > 0:
                obj['gia_san'] = gia_san[0]
            else:
                print("error")
            # ----------------------------
            gia_3_buy = response.xpath('//*[@id="{}_e"]/text()'.format(cp)).extract()
            if len(gia_3_buy) > 0:
                obj['gia_3_buy'] = gia_3_buy[0]
            else:
                print("error")
            # ----------------------------
            kl_3_buy = response.xpath('//*[@id="{}_f"]/text()'.format(cp)).extract()
            if len(kl_3_buy) > 0:
                obj['kl_3_buy'] = ma_ck[0]
            else:
                print("error")
            # ----------------------------
            gia_2_buy = response.xpath('//*[@id="{}_g"]/text()'.format(cp)).extract()
            if len(gia_2_buy) > 0:
                obj['gia_2_buy'] = gia_2_buy[0]
            else:
                print("error")
            # ----------------------------
            kl_2_buy = response.xpath('//*[@id="{}_h"]/text()'.format(cp)).extract()
            if len(kl_2_buy) > 0:
                obj['kl_2_buy'] = kl_2_buy[0]
            else:
                print("error")
            # ----------------------------
            gia_1_buy = response.xpath('//*[@id="{}_i"]/text()'.format(cp)).extract()
            if len(gia_1_buy) > 0:
                obj['gia_1_buy'] = gia_1_buy[0]
            else:
                print("error")
            # ----------------------------
            kl_1_buy = response.xpath('//*[@id="{}_j"]/text()'.format(cp)).extract()
            if len(kl_1_buy) > 0:
                obj['kl_1_buy'] = kl_1_buy[0]
            else:
                print("error")
            # ----------------------------
            tang_giam = response.xpath('//*[@id="{}_k"]/text()'.format(cp)).extract()
            if len(tang_giam) > 0:
                obj['tang_giam'] = tang_giam[0]
            else:
                print("error")
            # ----------------------------
            gia = response.xpath('//*[@id="{}_l"]/text()'.format(cp)).extract()
            if len(gia) > 0:
                obj['gia'] = gia[0]
            else:
                print("error")
            # ----------------------------
            khoi_luong = response.xpath('//*[@id="{}_m"]/text()'.format(cp)).extract()
            if len(khoi_luong) > 0:
                obj['khoi_luong'] = khoi_luong[0]
            else:
                print("error")
            # ----------------------------
            tong_kl = response.xpath('//*[@id="{}_n"]/text()'.format(cp)).extract()
            if len(tong_kl) > 0:
                obj['tong_kl'] = tong_kl[0]
            else:
                print("error")
            # ----------------------------
            gia_1_sell = response.xpath('//*[@id="{}_o"]/text()'.format(cp)).extract()
            if len(gia_1_sell) > 0:
                obj['gia_1_sell'] = gia_1_sell[0]
            else:
                print("error")
            # ----------------------------
            kl_1_sell = response.xpath('//*[@id="{}_p"]/text()'.format(cp)).extract()
            if len(kl_1_sell) > 0:
                obj['kl_1_sell'] = kl_1_sell[0]
            else:
                print("error")
            # ----------------------------
            gia_2_sell = response.xpath('//*[@id="{}_q"]/text()'.format(cp)).extract()
            gia_2_sell = response.xpath('//*[@id="{}_q"]/text()'.format(cp)).extract()
            if len(gia_2_sell) > 0:
                obj['gia_2_sell'] = gia_2_sell[0]
            else:
                print("error")
            # ----------------------------
            kl_2_sell = response.xpath('//*[@id="{}_r"]/text()'.format(cp)).extract()
            if len(kl_2_sell) > 0:
                obj['kl_2_sell'] = kl_2_sell[0]
            else:
                print("error")
            # ----------------------------
            gia_3_sell = response.xpath('//*[@id="{}_s"]/text()'.format(cp)).extract()
            if len(gia_3_sell) > 0:
                obj['gia_3_sell'] = gia_3_sell[0]
            else:
                print("error")
            # ----------------------------
            kl_3_sell = response.xpath('//*[@id="{}_t"]/text()'.format(cp)).extract()
            if len(kl_3_sell) > 0:
                obj['kl_3_sell'] = kl_3_sell[0]
            else:
                print("error")
            # ----------------------------
            gia_cao = response.xpath('//*[@id="{}_v"]/text()'.format(cp)).extract()
            if len(gia_cao) > 0:
                obj['gia_cao'] = gia_cao[0]
            else:
                print("error")
            # ----------------------------
            gia_thap = response.xpath('//*[@id="{}_w"]/text()'.format(cp)).extract()
            if len(gia_thap) > 0:
                obj['gia_thap'] = gia_thap[0]
            else:
                print("error")
            # ----------------------------
            dtnn_mua = response.xpath('//*[@id="{}_x"]/text()'.format(cp)).extract()
            if len(tong_kl) > 0:
                obj['tong_kl'] = tong_kl[0]
            else:
                print("error")
        yield  obj


# if __name__ == "__main__":
#     process = CrawlerProcess({
#         'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
#     })
#
#     process.crawl("liveboard_cafef")
#     process.start() # the script will block here until the crawling is finished
