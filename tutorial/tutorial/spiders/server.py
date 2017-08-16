# -*- coding: utf-8 -*-

import scrapy
from scrapy.utils.url import urljoin_rfc,re
import urllib

class ServerSpider(scrapy.Spider):
    handle_httpstatus_list = [401]
    name = "server"
    start_urls = [
        "http://www.cmda.net/",
        "http://www.chinastar1.com/",
        "http://182.239.56.107/",
        "http://www.metroproduction.com.hk/",
        "http://www.seeyon.com/",
        "http://www.zhongoo.cn/",
        "http://1.53.110.127:8081/",
        "http://37.123.244.206:1901/"
        "http://1.53.110.127:8081/",
        "http://37.123.244.206:1901/",
        "http://1.52.79.73:8081/",
        "http://1.55.106.14:8081/",
        "http://1.52.107.211:8081/",
        "http://182.129.150.164:8069",
        "http://173.17.98.118:8069",
    ]

    def parse(self, response):
        ser = response.headers['Server']

        if (ser):
            ser_result = ser
        else:
            ser_result = "Not Found."

        yield{
        "url":response.url,
        "Server":ser_result,
        }
