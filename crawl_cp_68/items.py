# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy.spiders import CrawlSpider
# from scrapy.utils.project import get_project_settings
import re
import pprint
import datetime
from a.customize import glog
# from crawl_cp_68.customize.telegram_notify import GTeleBot
import pytz
from a.import_setting import *
from scrapy import Request

logger = glog.config_log()
# settings = get_project_settings()

class CrawlCp68Item(CrawlSpider):
    name = 'cophieu68_category'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.count = 0
        self.allowed_domains = ['www.cophieu68.vn']
        self.start_urls = [
            'http://www.cophieu68.vn/categorylist.php'
        ]

        settings['CRAWLER_COLLECTION'] = ('crawler.' + self.allowed_domains[0]).replace('www.', '')

    def parse(self, response):
        self.count += 1
        logger.info('crawl next pages: ' + response.url + ' - count: ' + str(self.count))
        try:
            pass

            for a_tag in response.xpath('//*[@id=\"ctl01\"]/div[5]/div[2]/div/div/div[1]/div[1]/div[1]/div[3]'):
                for link in a_tag.css('::attr(href)'):
                    if re.match('^.*-(ban|thue)-.*$', link.extract()):
                        yield response.follow(link, self.parse_document)

        except Exception:
            logger.exception(tele_bot.send_message('crawl parse pages error: ' + response.url) +
                             ' crawl parse pages error: ' + response.url,
                             exc_info=True, extra={'count_parse_pages_error': 1})

    def parse_document(self, response):
        try:
            domain = ''.join(self.allowed_domains)
            item = {'timestamp': datetime.datetime.now(tz=pytz.timezone('Asia/Ho_Chi_Minh'))
                .strftime(settings.get('DATETIME_FORMAT')),
                    'timestampISODate': datetime.datetime.now(tz=pytz.timezone('Asia/Ho_Chi_Minh')), 'domain': domain,
                    'url': normal(response.url)}

            item['street'] = ''.join(
                response.xpath('//*[@id="MainContent_ctlDetailBox_lblStreet"]/text()').extract()).strip()
            item['ward'] = ''.join(
                response.xpath('//*[@id=\"MainContent_ctlDetailBox_lblWard\"]/a/text()').extract()).strip()
            item['district'] = ''.join(
                response.xpath('//*[@id="MainContent_ctlDetailBox_lblDistrict"]/a/text()').extract()).strip()
            item['city'] = ''.join(
                response.xpath('//*[@id="MainContent_ctlDetailBox_lblCity"]/a/text()').extract()).strip()
            item['title'] = ''.join(response.css('div.nav-title > h1::text').extract()).strip()
            item['type'] = ''.join(response.css(
                '#ctl01 > div.body-content > div.jumbotron.head > div > div > div.col-lg-10.col-md-8.'
                'hidden-md.hidden-sm.hidden-xs > ol > li:nth-child(2) > a > p::text').extract()).strip()
            item['identity_number'] = ''.join(response.css('#MainContent_ctlDetailBox_lblId::text').extract()).strip()
            item['submission_date'] = ''.join(response.css('#MainContent_ctlDetailBox_lblDateCreated::text')
                                              .extract()).strip()

            item['updated_date'] = ''.join(response.css('#MainContent_ctlDetailBox_lblDateUpdated::text')
                                           .extract()).strip()

            item['contact'] = ''.join(response.css('#MainContent_ctlDetailBox_lblContactName::text')
                                      .extract()).strip()
            item['contact_id'] = ''.join(
                response.css('#MainContent_ctlDetailBox_lblContactPhone > a::attr(data-phoneext)').extract()
            ).strip()
            item['contact_phone_mask'] = ''.join(
                response.css('#MainContent_ctlDetailBox_lblContactPhone > a::text').extract()
            ).strip()
            item['contact_address'] = ''.join(
                response.css('#MainContent_ctlDetailBox_lblAddressContact::text').extract()
            ).strip()

            item['snippet'] = ''.join(
                response.css('div.col-md-8.col-xs-12.hidden-xs.padding-top-custom-devive::text').extract()).strip()

            item['number_of_rooms'] = ''.join(
                response.css('#MainContent_ctlDetailBox_lblBedRoom::text').extract()).strip()
            item['number_of_toilets'] = ''.join(
                response.css('#MainContent_ctlDetailBox_lblBathRoom::text').extract()).strip()
            item['surface_size'] = ''.join(response.css('#MainContent_ctlDetailBox_lblSurface::text').extract()).strip()
            item['legal'] = ''.join(response.css('#MainContent_ctlDetailBox_lblLegalStatus::text').extract()).strip()

            item['number_of_floors'] = ''.join(
                response.css('#MainContent_ctlDetailBox_lblFloor::text').extract()).strip()
            item['orientation'] = ''.join(
                response.css('#MainContent_ctlDetailBox_lblFengShuiDirection::text').extract()).strip()
            item['street_width'] = ''.join(
                response.css('#MainContent_ctlDetailBox_lblFrontRoadWidth::text').extract()).strip()
            item['of_project'] = ''.join(response.xpath('//*[@id=\"MainContent_ctlDetailBox_lblProject\"]/a/text()')
                                         .extract()).strip()
            item['content'] = ''.join(response.xpath('//*[@id="Description"]/text()').extract()).strip()
            item['image'] = response.css('ul.slides').css('img::attr(src)').extract()
            map_link = response.css('#MainContent_ctlDetailBox_lblMapLink > a::attr(href)').extract()

            if len(map_link) == 1:
                geolocation = re.findall("\d+.\d+", map_link[0])
                if len(geolocation) == 2:
                    item['geo_lat'] = geolocation[0]
                    item['geo_long'] = geolocation[1]

            item['price'] = ''.join(
                response.css('#MainContent_ctlDetailBox_lblPrice::text').extract()).strip()

            if 'city' in item and item['content'] != '':
                # remove key null
                remove_key = [k for k, v in item.items() if v is None or len(str(v)) == 0]
                for rk in remove_key:
                    item.pop(rk)

                if 'geo_lat' in item and 'geo_long' in item:
                    item['gps'] = {'lat': float(item.get('geo_lat')), 'lon': float(item.get('geo_long'))}

                # pprint.pprint(item)
                # print('====================')
                logger.info('crawl done: ' + response.url, extra={'count_field': len(item),
                                                                  'domain': self.allowed_domains,
                                                                  'count_crawl_done': 1, self.name: 1,
                                                                  'geoip': {'location': item.get('gps')}})
                return item
            else:
                logger.info('crawl not address: ' + response.url,
                            extra={'count_field': len(item), 'domain': self.allowed_domains,
                                   'count_crawl_not_address': 1})

        except Exception:
            logger.exception(tele_bot.send_message('crawl parse info error: ' + response.url) +
                             ' crawl error: ' + response.url,
                             exc_info=True, extra={'count_parse_info_error': 1, 'domain': self.allowed_domains[0]})
