# -*- coding: utf-8 -*-

import scrapy
from scrapy.utils.url import urljoin_rfc,re
import urllib

class TplinkSpider(scrapy.Spider):
    handle_httpstatus_list = [401]
    name = "tp-link"
    start_urls = ["http://1.52.79.73:8081/",
        "http://1.55.106.14:8081/",
        "http://1.52.107.211:8081/",
        "http://182.129.150.164:8069",
        "http://182.129.150.164:8069",
    ]

    def parse(self, response):
        ser = response.headers['Server']

        if (ser == "Router Webserver" or ser == "TP-LINK Router"):
            version = response.headers['WWW-Authenticate']
            ver = re.search('[Tt][Pp]-.*',version).group()
        else:
            ver = "Not Found!"


        yield{
        "url":response.url,
        "Server":ser,
        "Version":ver,
        }
