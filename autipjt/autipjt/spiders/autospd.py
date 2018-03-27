# -*- coding: utf-8 -*-
import scrapy
from autipjt.items import AutipjtItem
from scrapy.http import Request

class AutospdSpider(scrapy.Spider):
    name = 'autospd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cid4011029.html']

    def parse(self, response):

        item =AutipjtItem()
        #通过xpath分别提取商品名称，价格，评论，链接
        #商品姓名
        item['name'] = response.xpath('//div[@class="con shoplist"]/div/ul/li/a/@title').extract()
        #商品价格
        item['price'] = response.xpath('//span[@class="price_n"]/text()').extract()
        #商品链接
        item['link'] = response.xpath('//a[@class="pic"]/@href').extract()
        #商品评价
        item['comnum'] = response.xpath('//p[@class="star"]/a/text()').extract()
        #提取玩后返回item
        yield item
        #通过循环自动爬去20页数据
        for i in range(1, 21):
            #通过总结的网址格式构造要爬取的网址
            #     http://category.dangdang.com/pg2-cid4011029.html
            url = "http://category.dangdang.com/pg" + str(i) + "-cid4011029.html"
            #通过yield返回Request,并指定要爬取的网址和回调函数
            #实现自动爬取
            yield Request(url, callback=self.parse)