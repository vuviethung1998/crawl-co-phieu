LOG_LEVEL = 'INFO'
BOT_NAME = 'crawl_cp_68'
NEWSPIDER_MODULE = 'crawl_cp_68.spiders'
ROBOTSTXT_OBEY = True
FEED_EXPORT_ENCODING = 'utf-8'

# HTTP_PROXY = 'http://10.10.137.43:8118'
# # HTTP_PROXY = 'http://92.244.99.229:3128'
# TOR_HOST = '10.10.137.43'
# TOR_PORT = 9051
MONGODB_URI = 'mongodb://admin:admin@localhost:27017'
# ADDRESS_URL_COLLECTION = 'crawler.address.url'
# LOGSTASH_HOST = 'db'
# LOGSTASH_PORT = 5100
# ES_ADDRESS = ['db:9200']
# ES_CLUSTER_ADDRESS = ['hd01:9201', 'hd02:9201', 'hd03:9201']
# KAFKA_ADDRESS = ['hd02:6667', 'hd03:6667']
# KAFKA_TOPIC = 'g_crawl'

# LOGSTASH_HOST = '192.168.3.160'
# LOGSTASH_PORT = 5100

MONGODB_DATABASE = 'CRAWLER_CO_PHIEU_68'
# BLOOM_FILTER_MAX_SIZE = 100000000
# BLOOM_FILTER_ERROR_RATE = 0.0000001
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
# ES_CRAWL_INDEX = 'crawl_cp_68'
# ES_CRAWL_TYPE = 'doc'

SPLASH_URL = 'http://127.0.0.1:8050'
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
COOKIES_ENABLED = True
SPLASH_COOKIES_DEBUG = False


SPIDER_MODULES = [
    'crawl_cp_68.spiders'
]

USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0) Gecko/16.0 Firefox/16.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) '
    'Version/5.1.3 Safari/534.53.10',
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/41.0.2227.1 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; <64-bit tags>) AppleWebKit/<WebKit Rev> (KHTML, like Gecko) '
    'Chrome/<Chrome Rev> Safari/<WebKit Rev> Edge/<ECRAWLER_COLLECTIONdgeHTML Rev>.<Windows Build>',
]

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 400,
}

ITEM_PIPELINES = {
    'crawl_cp_68.pipelines.MongoDBPipeline': 1,
    # 'crawl_cp_68`.pipelines.KafkaPipeline': 2
}

# TELE_TOKEN = '1064700978:AAH7mQK8I2RqCcEfLhtFNzUlQORTEf2-gr4'
# TELE_CHAT_ID = '-340499601'

# ADDRESS_URL_PATH = 'data/crawler_address_url.json'
