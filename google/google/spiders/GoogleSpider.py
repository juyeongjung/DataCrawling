import scrapy
from google.items import GoogleItem

class GoogleSpider(scrapy.Spider):
    name="google"

    def start_requests(self):
        for i in range(0,5,1):
            yield scrapy.Request("https://www.kookmin.ac.kr/site/ecampus/notice/all/?&pn=%d" %i, self.parse_google)

    def parse_google(self,response):
        for sel in response.xpath('//tbody/tr'):
            item=GoogleItem()
            item['category']=sel.xpath('td[1]/text()').extract()
            item['title']=sel.xpath('td[2]/a/text()').extract()
            #item['link']=sel.xpath('td[2]/a/@href').extract()
            yield item

        # // *[ @ id = "content_body"] /section / div[1] / table / tbody / tr[1] / td[1]
