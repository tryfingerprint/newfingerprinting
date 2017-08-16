# -*- coding: utf-8 -*-

import scrapy
from scrapy.utils.url import urljoin_rfc,re
import urllib

class CiscoSpider(scrapy.Spider):
    handle_httpstatus_list = [401]
    name = "cisco"
    start_urls = [
    "http://72.39.181.193:7547",
    ]

    def parse(self, response):
        print response.headers
