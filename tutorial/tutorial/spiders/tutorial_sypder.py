import scrapy
from tutorial.items import Kookminitem
class TutorialSpider(scrapy.Spider): #가져올 경로 설정
    name= "kookmin"
    allowed_domains=["kookmin.ac.kr"]
    start_urls=[ #리스트 형태로 추가가능. start_requests는 콜백함수, 사이트 로그인할 때 사용
        "https://www.kookmin.ac.kr/site/ecampus/notice/academic/"
        #크롤링 할 때 저작권, robots.txt 항목을 검사하고 크롤링하자
    ]
    
    def parse(self, response): #스파이더가 동작하는 부분. response=응답을 받아 처리함.
        for sel in response.xpath('//tr/td'): #//는 뒤에 오는 태그를 모두 들고오라는 의미.
            item=Kookminitem()
            item['title']=sel.xpath('a/text()').extract()
            item['link']=sel.xpath('a/@href').extract()
            yield item #아이템에 쌓아주게 하는 함수
            
#             print(title,link)
#             //*[@id="content_body"]/section/div[1]/table/tbody/tr[8]/td[2]/a 이것이 xpath.
#         filename=response.url.split("/")[-2] # 이렇게 하면 페이지 전체를 가져옴
#         with open(filename,'wb') as f:
#             f.write(response.body)


# xpath를 통해 데이터를 가져오는 방법
# response.xpath('//xxxx/()')
# css를 통해 데이터를 가져오는 방법
# response.css('title::text')
# extract()를 사용하면 태그의 특정 데이터나 부분만 가져올 수 있음