# -*- coding: utf-8 -*-
import scrapy
import time



class IfengZxSpider(scrapy.Spider):
    name = 'ifeng_zx'
    allowed_domains = ['ifeng.com']
    start_urls = ['http://ifeng.com/']

    def parse(self, response):
        print(response.text)
        pass

    @classmethod
    def init_start_urls(cls):
        localtime = time.strftime("%Y%m%d")
        month = time.strftime("%Y%m00")
        today = int(localtime) - int(month)
        for i in range(today, 0, -1):
                cls.start_urls.append("http://news.ifeng.com/listpage/11502/"
                                      + str(int(month)+i)
                                      + "/1/rtlist.shtml")
        print(cls.start_urls)
        pass


IfengZxSpider.init_start_urls()
