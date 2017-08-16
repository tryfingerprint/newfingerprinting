# -*- coding: utf-8 -*-

import scrapy
from scrapy.utils.url import urljoin_rfc,re
import urllib

class JuniperSpider(scrapy.Spider):
    handle_httpstatus_list = [401]
    name = "juniper"
    start_urls = [
    "http://182.48.182.58/",
    "http://90.169.25.129/",
    "http://90.147.180.3/",
    "http://90.147.33.5/",
    "http://90.182.129.186/",
    ]

    def parse(self, response):
        version = response.xpath('//strong/text()').extract_first()
        if(version):
            ver = version.strip(' \t\n\r')[0:-5]
        else:
            ver = "Not Found!"

        yield{
        "url":response.url,
        "version":ver,
        }
