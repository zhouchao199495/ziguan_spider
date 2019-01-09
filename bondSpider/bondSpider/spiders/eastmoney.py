# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import BondspiderItem


class EastmoneySpider(CrawlSpider):
    name = 'eastmoney'
    allowed_domains = ['eastmoney.com']

    # 要闻
    # 国内经济
    # 债券新闻
    # 债券分析
    # 银行间债券评述
    # 海外债市评述
    # 债券公告
    start_urls = ['http://finance.eastmoney.com/a/cywjh.html',
                  'http://finance.eastmoney.com/a/cgnjj.html',
                  'http://bond.eastmoney.com/a/czsfx.html',
                  'http://bond.eastmoney.com/a/czqxw.html',
                  'http://bond.eastmoney.com/a/cjyszsps.html',
                  'http://bond.eastmoney.com/a/cyhjzsps.html',
                  'http://bond.eastmoney.com/a/czqgg.html']

    rules = (
        # 获取这个列表里的链接，依次发送请求，并且继续跟进，调用指定回调函数处理
        Rule(LinkExtractor(allow=("cywjh_[1-9]*.html|cgnjj_[1-9]*.html|czsfx_[1-9]*.html|czqxw_[1-9]*.html|cjyszsps_[1-9]*.html|cyhjzsps_[1-9]*.html|czqgg_[1-9]*.html")),
             callback="parse_news", follow=True),
        Rule(LinkExtractor(allow=(), allow_domains=('eastmoney.com'), restrict_xpaths=("//p[@class='title']")),
             callback="parse_bond", follow=False),
    )

    def parse_bond(self, response):
        item = BondspiderItem()
        item['url'] = response._url
        aa = response.xpath("//div[@class='time']/text()")
        # 发布日期
        item['publish_date'] = aa.extract_first()

        # 文章标题
        vc_title = response.xpath("//div[@class='newsContent']/h1/text()")
        item['title'] = vc_title.extract_first()

        # 发布内容
        contexts = response.xpath("//div[@id='ContentBody']/p/text()")
        content_body = ""
        for context in contexts:
            content_body += context.extract()
        item['news_context'] = content_body

        print("spider[" + self.name + "]抓取网页[" + response._url + "]完成！")
        yield item