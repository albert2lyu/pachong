#coding:utf-8

import scrapy
from pachong.items import PachongItem

class QuotesSpider(scrapy.Spider):
    name =  'pachong'
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        base_url = 'http://quotes.toscrape.com'
        item = PachongItem()
        divs = response.xpath('//div[@class="quote"]')
        for div in divs:
            item['name'] = div.xpath('span[@class="text"]/text()').extract()[0]
            item['url'] = base_url+div.xpath('span/a/@href').extract()[0]
            item['tags'] = div.xpath('div[@class="tags"]/a/text()').extract()
            item['author'] = div.xpath('span/small[@class="author"]/text()').extract()[0]
            print(item)
            yield item