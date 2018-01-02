# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 出版社
    publish_house = scrapy.Field()
    # 出版年
    publish_date = scrapy.Field()
    # 页数
    page_num = scrapy.Field()
    # 装帧
    package = scrapy.Field()
    # ISBN
    ISBN = scrapy.Field()
    # 定价
    price = scrapy.Field()
    # 豆瓣评分
    remark = scrapy.Field()
    # 标签
    tags = scrapy.Field()

