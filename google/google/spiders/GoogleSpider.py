# 과도한 크롤링은 서버에 부하를 줄 수 있습니다. 적절한 딜레이를 통해 서버에 부담을 줄이셔야 함을 알립니다.

import scrapy
from google.items import GoogleItem
from datetime import datetime
import re #정규식 사용을 위해서 import함
import time

class GoogleSpider(scrapy.Spider):
    name="google"

    def start_requests(self):
        for i in range(0,5,1):
            yield scrapy.Request("https://www.kookmin.ac.kr/site/ecampus/notice/all/?&pn=%d" %i, self.parse_google)

    def parse_google(self,response):
        for sel in response.xpath('//tbody/tr'): #'//tbody/tr[@class="mytr"]' 이렇게 특정 클래스나 id를 지정해서 가져올 수 있음
            item=GoogleItem()
            item['category']=sel.xpath('td[1]/text()').extract()   #.extract()[0][2:] 대괄호 먼뜻인지 알아보자...
            item['title']=sel.xpath('td[2]/a/text()').extract()
            #item['link']=sel.xpath('td[2]/a/@href').extract()

            #date_now = datetime.now() 날짜 변환하는 법
            #date_str_tmp = sel.xpath('td[@class="date"]/text()').extract()[0]

            # prog = re.compile('[0-9]{2}:[0-9]{2}') 정규식을 통해 시간으로 변환
            # if prog.match(date_str_tmp):
            #     date_str = date_now.strftime('%y/%m/%d') + ' ' + date_str_tmp + ':00'
            # else:
            #     date_str = date_now.strftime('%y/') + date_str_tmp + ' ' + '00:00:00'
            #
            # dateTmp = datetime.strptime(date_str, "%y/%m/%d %H:%M:%S")

            #time.sleep(1) #delay를 주어 서버의 과부하를 막는다.
            yield item

        # // *[ @ id = "content_body"] /section / div[1] / table / tbody / tr[1] / td[1] 이게 xpath
