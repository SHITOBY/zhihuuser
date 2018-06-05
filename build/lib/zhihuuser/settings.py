# -*- coding: utf-8 -*-

# Scrapy settings for zhihuuser project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihuuser'

SPIDER_MODULES = ['zhihuuser.spiders']
NEWSPIDER_MODULE = 'zhihuuser.spiders'


SCHEDULER = "scrapy_redis.scheduler.Scheduler"

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 300
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'zhihuuser (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'cookie': 'd_c0 = "APBhkUN9mw2PTngn2kOaD9i5zLs_RUWXMAU=|1526553010"; _zap=2b2a9c63-b0f3-4ee0-a1d1-abf26e413162; q_c1=d96b9a95c9df4f26b4165090d259b57d|1526650312000|1526650312000; capsion_ticket="2|1:0|10:1526873354|14:capsion_ticket|44:ZDE4ODFjZWNjYmY2NDJkYWFjYzM3YTdlNjVkZjNiNTQ=|2538eed98d1f4c28e525d1b577651dca7573f52d073dc548c66afee86131d234"; z_c0="2|1:0|10:1526873355|4:z_c0|92:Mi4xekhETUFnQUFBQUFBOEdHUlEzMmJEU1lBQUFCZ0FsVk5DNHZ2V3dESE9wZFIxcHhEQWVwS2RKN0YyYVQ5ekZRdFdR|cbf54353be5e4ecefc58fa3d4aca7d513296b171a6af4626caeee5f687a9861b"; tgw_l7_route=8605c5a961285724a313ad9c1bbbc186; _xsrf=dab29d90-0243-457c-b60e-bc58a6d3b2d5',


    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20',#没登录时才显示
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'zhihuuser.middlewares.ZhihuuserSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'zhihuuser.middlewares.ZhihuuserDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'zhihuuser.pipelines.ZhihuuserPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
