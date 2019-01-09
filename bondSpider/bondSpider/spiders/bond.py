# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import BondspiderItem


class BondSpider(CrawlSpider):
    name = 'bond'
    spider_page_url = []
    bond_items = []
    # 债券新闻域名
    allowed_domains = ['ifeng.com/']

    # 债券新闻首页
    start_urls = ['http://news.ifeng.com/listpage/11502/20181208/1/rtlist.shtml']

    rules = (
        # 获取这个列表里的链接，依次发送请求，并且继续跟进，调用指定回调函数处理
        Rule(LinkExtractor(allow=r'listpage/11502/[1-9]*/[1-9]/rtlist.shtml'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=(), allow_domains=('eastmoney.com'), restrict_xpaths=("//p[@class='title']")),
             callback="parse_bond", follow=False),
    )

    def parse(self, response):
        # 提取新闻分页链接
        print(response.text)
        # page_extractor = LinkExtractor(allow=(), allow_domains=('ifeng.com'),
        #                    restrict_xpaths=("//div[@class='m_page']"))

        page_extractor = LinkExtractor(allow=r'0.shtml')
        page_links = page_extractor.extract_links(response)
        for page_link in page_links:
            if page_link.url not in self.spider_page_url:
                self.spider_page_url.append(page_link.url)
                # yield scrapy.Request(page_link.url, callback=self.parse_news)

    def parse_news(self, response):
        print(response.text)
        news_extractor = LinkExtractor(allow=(), allow_domains=('eastmoney.com'),
                                       restrict_xpaths=("//p[@class='title']"))
        news_links = news_extractor.extract_links(response)
        # for news_link in news_links:
        #     yield scrapy.Request(news_link.url, callback=self.parse_bond)

    def parse_bond(self, response):
        print(response.text)
        item = BondspiderItem()
        # aa = response.xpath("//div[@class='time'] ")
        # # 发布日期
        # item['publish_date'] = aa
        # print(item['publish_date'])
        #
        # # 文章标题
        # item['title'] = response.xpath("h1").extract()[0]
        # # 发布内容
        # item['news_context'] = response.xpath("./p[0]").extract()[0]
        # item.show()
        # self.bond_items.append(item)
        yield item
