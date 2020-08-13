from scrapy.spiders import CrawlSpider
from scrapy import Request
from datetime import datetime

class CategoryDetailSpider(CrawlSpider):
    name =  'categorydetail'
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.allowed_domains = ['www.cophieu68.vn']

        lst_type = ['^bds', '^caosu', '^ck', '^congnghe', '^dichvu', '^dvci', '^duocpham', '^giaoduc', '^hk', '^khoangsan',
                    '^nangluong', '^nganhang', '^thep', '^daukhi', '^nhua', '^phanbon', '^sxkd', '^thucpham', '^thuongmai', '^thuysan',
                    '^vantai', '^vlxd', '^xaydung', '^dtpt', '^dtxd']
        self.start_urls = ['http://www.cophieu68.vn/categorylist_detail.php?category={}'.format(str) for str in lst_type ]


    def start_requests(self):
        yield Request(self.start_urls, callback=self.parse)

    def parse(self,response ):
        lst_obj = []
        root_path = '//*[@id="begin_header"]/table//tr/td/table[2]//tr'
        length_row = len(response.xpath(root_path).extract() )
        for i in range(2,length_row + 1):
            obj = {}
            now = datetime.now() # current date and time
            obj['cur_date'] = now.strftime("%d/%m/%Y")
            # ----------------------------
            nhom_nganh = response.xpath(root_path + '[{}]/td[2]/a/strong/text()'.format(i)).extract()
            if len(nhom_nganh) > 1:
                obj['nhom_nganh'] = nhom_nganh[0]
                obj['id'] = nhom_nganh[1]
            else:
                obj['nhom_nganh'] = ''
                obj['id'] = ''
            # ----------------------------
            tang_truong = response.xpath(root_path +'[' + str(i) + ']/td[3]/span/text()').extract()
            if len(tang_truong) > 0:
                obj['diem'] = tang_truong[0]
                obj['tang_truong'] = tang_truong[1][1:-1]
            else:
                obj['diem'] = 0
                obj['tang_truong'] = 0
            # ----------------------------
            earning_per_share = response.xpath(root_path +'[' + str(i) + ']/td[4]/text()').extract()
            if len(earning_per_share) > 0:
                obj['earning_per_share'] = earning_per_share[0]
            else:
                obj['earning_per_share'] = 0
            # ----------------------------
            price_to_earnings = response.xpath(root_path +'[' + str(i) + ']/td[5]/text()').extract()
            if len(price_to_earnings) > 0:
                obj['price_to_earnings'] = price_to_earnings[0]
            else:
                obj['price_to_earnings'] = 0
            # ----------------------------
            return_on_assets = response.xpath(root_path +'[' + str(i) + ']/td[6]/text()').extract()
            if len(return_on_assets) > 0:
                obj['return_on_assets'] = return_on_assets[0]
            else:
                obj['return_on_assets'] = 0
            # ----------------------------
            return_on_equity = response.xpath(root_path +'[' + str(i) + ']/td[7]/text()').extract()
            if len(return_on_equity) > 0:
                obj['return_on_equity'] = return_on_equity[0]
            else:
                obj['return_on_equity'] = 0
            # --------------------------    --
            average_price = response.xpath(root_path +'[' + str(i) + ']/td[8]/text()').extract()
            if len(average_price) > 0:
                obj['average_price'] = average_price[0]
            else:
                obj['average_price'] = 0
            #---------------------------
            price_to_book = response.xpath(root_path +'[' + str(i) + ']/td[10]/text()').extract()
            if len(price_to_book) > 0:
                obj['price_to_book'] = price_to_book[0]
            else:
                obj['price_to_book'] = 0
            #---------------------------
            tong_khoi_luong = response.xpath(root_path +'[' + str(i) + ']/td[12]/text()').extract()
            if len(tong_khoi_luong) > 0:
                obj['tong_khoi_luong'] = tong_khoi_luong[0]
            else:
                obj['tong_khoi_luong'] = 0
            #---------------------------
            kl_nn_so_huu = response.xpath(root_path +'[' + str(i) + ']/td[13]/text()').extract()
            if len(kl_nn_so_huu) > 0:
                obj['kl_nn_so_huu'] = kl_nn_so_huu[0]
            else:
                obj['kl_nn_so_huu'] = 0
            #---------------------------
            von_tt = response.xpath(root_path +'[' + str(i) + ']/td[14]/text()').extract()
            if len(von_tt) > 0:
                obj['von_tt'] = von_tt[0]
            else:
                obj['von_tt'] = 0

            lst_obj.append(obj)
        yield {'list_category': lst_obj}






