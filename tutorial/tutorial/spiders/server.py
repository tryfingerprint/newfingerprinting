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
        "http://182.48.182.58/",
        "http://90.169.25.129/",
        "http://90.147.180.3/",
        "http://90.147.33.5/",
        "http://90.182.129.186/",
        "http://www.ncepubbs.com",
        "http://blog.viewfin.com/",
        "http://www.eika.cn",
        "http://www.sdzzj.net/",
        "http://www.tjibm.com/",
        "http://37.123.244.206:1901/",
        "http://1.52.79.73:8081/",
        "http://1.55.106.14:8081/",
        "http://1.52.107.211:8081/",
    ]

    def parse(self, response):
        ser = response.headers['Server']
        router = ""
        cms = ""

        '''
        TP-LINK
        '''
        if (ser==0):
            ser = "Server Not Found."
        elif (ser == "Router Webserver" or ser == "TP-LINK Router"):
            version = response.headers['WWW-Authenticate']
            ver = re.search('[Tt][Pp]-.*',version).group()
            router = ver
        '''
        juniper
        '''
        juniper = response.xpath('//strong/text()').extract_first()
        if (juniper):
            router = juniper.strip(' \t\n\r')[0:-5]

        '''
        discuz
        '''
        res = response.xpath('//meta[@name="generator"]/@content').extract_first()
        urls = urljoin_rfc(response.url,"robots.txt")
        t = urllib.urlopen(urls)
        a = re.findall("[Dd]iscuz.*",t.read())
        if(res):
            cms = res
        elif(a):
            cms = a
        else:
            cms = ""

        yield{
        "url":response.url,
        "response_headers":response.headers,
        "response_body":response.body,
        "Server":ser,
        "Router":router,
        "CMS":cms,
        }
