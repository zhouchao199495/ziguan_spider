# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BondspiderItem(scrapy.Item):

    # url
    url = scrapy.Field()

    # 发布日期
    publish_date = scrapy.Field()

    # 标题
    title = scrapy.Field()

    # 新闻内容
    news_context = scrapy.Field()

    def show(self):
        print("发布日期：" + self.publish_date + ",标题：" + self.title + ",新闻内容:" + self.news_context)
    pass
