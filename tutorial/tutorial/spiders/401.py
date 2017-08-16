# -*- coding: utf-8 -*-

import scrapy
from scrapy.utils.url import urljoin_rfc,re
import urllib

class basicSpider(scrapy.Spider):
    handle_httpstatus_list = [401]
    name = "401"
    start_urls = [
        "http://41.188.56.222:5009/",
        "http://14.187.131.122:1901/",
        "http://14.230.98.164:1901/",
        "http://14.192.240.209:1901/",
        "http://14.192.243.104:190/",
        "http://182.129.150.164:8069",
    ]

    def parse(self, response):
        if(response.status == 401):
            version = response.headers['WWW-Authenticate']
        if(re.match('Basic realm',version)!= None):
            ver = version[13:-1]

        yield{
        "url":response.url,
        "Server":ver,
        }
