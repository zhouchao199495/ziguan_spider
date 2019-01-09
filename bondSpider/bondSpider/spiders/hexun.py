# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class HexunSpider(CrawlSpider):
    name = 'hexun'
    allowed_domains = ['hexun.com']
    start_urls = ['http://bond.hexun.com/jrdd/index.html']

    rules = (
        Rule(LinkExtractor(allow='jrdd/index-[1-9]*.html'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow='jrdd/index-[1-9]*.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
