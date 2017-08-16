# -*- coding: utf-8 -*-

import scrapy
from scrapy.utils.url import urljoin_rfc,re
import urllib

class TestSpider(scrapy.Spider):
    name = "test"
    start_urls = [
        "http://www.ncepubbs.com",
        "http://blog.viewfin.com/",
        "http://www.eika.cn",
        "http://www.sdzzj.net/",
        "http://www.tjibm.com/",
    ]

    def parse(self, response):
        res = response.xpath('//meta[@name="generator"]/@content').extract_first()
        urls = urljoin_rfc(response.url,"robots.txt")
        t = urllib.urlopen(urls)
        a = re.findall("[Dd]iscuz.*",t.read())
        if(res):
            result =  " Web application details : " + res
        elif(a):
            result = " Web application details : " + a
        else:
            result =  " Web application version not found!"
        yield{
        "url":response.url,
        "result":result,
        }
