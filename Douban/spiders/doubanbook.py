# -*- coding: utf-8 -*-
import re

import scrapy
from Douban.items import DoubanItem

class DoubanbookSpider(scrapy.Spider):
    name = 'doubanbook'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/subject/25985021/']

    def parse(self, response):
        item = DoubanItem()
        author = response.xpath("//div[@id='info']/span[contains(./text(), '作者:')]/following-sibling::a[1]/text()").extract()[0]
        item["author"] = re.sub("\s","",string=author)
        item["publish_house"] = response.xpath("//div[@id='info']/span[contains(./text(), '出版社:')]/following::text()[1]").extract()[0]
        item["publish_date"] = response.xpath("//div[@id='info']/span[contains(./text(), '出版年:')]/following::text()[1]").extract()[0]
        item["page_num"] = response.xpath("//div[@id='info']/span[contains(./text(), '页数:')]/following::text()[1]").extract()[0]
        item["package"] = response.xpath("//div[@id='info']/span[contains(./text(), '装帧:')]/following::text()[1]").extract()[0]
        item["ISBN"] = response.xpath("//div[@id='info']/span[contains(./text(), 'ISBN:')]/following::text()[1]").extract()[0]
        item["price"] = response.xpath("//div[@id='info']/span[contains(./text(), '定价:')]/following::text()[1]").extract()[0]
        item["remark"] = response.xpath("//strong[@class='ll rating_num ']/text()").extract()[0]
        item["tags"] = response.xpath("//a[@class='  tag']/text()").extract()
        yield item
        # 返回下一个链接
        url_list = response.xpath("//div[@class='content clearfix']/dl/dd/a/@href").extract()
        for url in url_list:
            yield scrapy.Request(url=url,callback=self.parse)

