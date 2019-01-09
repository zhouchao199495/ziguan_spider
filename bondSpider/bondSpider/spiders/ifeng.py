# -*- coding: utf-8 -*-
import scrapy
import time
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import BondspiderItem


# 凤凰网
class IfengSpider(CrawlSpider):
    name = 'ifeng'
    allowed_domains = ['ifeng.com']
    start_urls = []
    start_indexes = []

    rules = (
        # 获取这个列表里的链接，依次发送请求，并且继续跟进，调用指定回调函数处理
        Rule(LinkExtractor(allow=(), allow_domains=('ifeng.com'), restrict_xpaths=("//div[@class='m_page']")),
             callback="parse_items", follow=True),
        Rule(LinkExtractor(allow=r'0.shtml'),
             callback="parse_item", follow=False),
    )

    def parse_item(self, response):
        item = BondspiderItem()

        # 新闻链接
        item['url'] = response._url
        page_selector_list = response.xpath("//meta[@name='og:category ']/@content")
        if len(page_selector_list) > 0:
            page_type = page_selector_list[0].root
        else:
            page_type = "新时代新气象"
        print(page_type)

        if page_type == "新时代新气象":
            """新时代新气象页面"""
            # 发布日期
            publish_date = response.xpath("//div[@class='yc_tit']/p/span/text()")
            item['publish_date'] = str(IfengSpider.get_chn_date(publish_date.extract_first()))

            # 文章标题
            vc_title = response.xpath("//div[@class='yc_tit']/h1/text()")
            item['title'] = vc_title.extract_first()

            # 发布内容
            contexts = response.xpath("//div[@id='yc_con_txt']/p/text()")
            content_body = ""
            for context in contexts:
                content_body += context.extract()
            item['news_context'] = content_body
        elif page_type == "凤凰资讯":
            """凤凰网资讯页面"""
            # 发布日期
            publish_date = response.xpath("//span[@itemprop='datePublished']/text()")
            item['publish_date'] = publish_date.extract_first()
            if len(item['publish_date']) > 18:
                item['publish_date'] = str(item['publish_date'])[0:17]

            # 文章标题
            vc_title = response.xpath("//div[@id='artical']//h1[@id='artical_topic']/text()")
            item['title'] = vc_title.extract_first()

            # 发布内容
            contexts = response.xpath("//div[@id='main_content']/p/text()")
            content_body = ""
            for context in contexts:
                content_body += context.extract()
            item['news_context'] = content_body
        elif page_type == "凤凰评论":
            print("这是凤凰评论页面")
        else:
            raise Exception(str(page_type) + ",无法识别的页面！")
            pass

        return item

    @classmethod
    def init_start_urls(cls):
        localtime = time.strftime("%Y%m%d")
        month = time.strftime("%Y%m00")
        today = int(localtime) - int(month)
        for i in range(today, 0, -1):
            cls.start_urls.append("http://news.ifeng.com/listpage/11502/"
                                  + str(int(month) + i)
                                  + "/1/rtlist.shtml")
        print(cls.start_urls)
        pass

    @classmethod
    def get_chn_date(cls, str_time_stamp, formatter="%Y-%m-%d %H:%M:%S"):
        time_obj = time.strptime(str_time_stamp, formatter)
        year = time_obj.tm_year
        month = time_obj.tm_mon
        day = time_obj.tm_mday
        hour = time_obj.tm_hour
        minute = time_obj.tm_min
        str_date = str(year) + "年" + str(month) + "月" + str(day) + "日 " + str(hour) + ":" + str(minute)
        return str_date

IfengSpider.init_start_urls()
