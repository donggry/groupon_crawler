# -*- coding: utf-8 -*-
import scrapy

from groupon.items import GrouponItem

f=open('output.txt','w')

class Grouponspider(scrapy.Spider):
    name = "groupon"#컴파일 이름 scrapy crawl groupon 하면 된다->output.txt.에 결과 저장됨
    allowed_domains = ["groupon.com"]
    start_url_1 = "https://www.groupon.com/goods/electronics?category=electronics&page=" #다른 카테고리를 크롤링 할떄는
    #electronics대신 다른 카테고리 명을 치면 됨!!
    start_urls = []
    for i in range(1, 5):
        start_url_2 = start_url_1 + str(i)
        start_urls.append(start_url_2)
    #크롤링할 주소들을 저장! 형식은 https://www.groupon.com/goods/electronics?page=1,2,3,,,이런식으로 증가!

    def parse(self, response):#시작주소에서 링크로 타고 넘어가기
        # 시작주소에는 30개의 아이템이 있다 각각의 30개의 아이ㅣ템에 걸린 링크를 타고 넘어간뒤에 크롤링 해주기 위함
        for href in response.css("div.browse-deals > figure > a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):

        item = GrouponItem()
        item['name']=response.xpath('//hgroup/h1/text()').extract()
        item['nutshell'] = response.xpath('//div[@class="nutshell highlights "]/p/text()').extract()#nutshell
        item['category'] = response.xpath('//section[@class="breadcrumbs"]//a/text()').extract()#category

        if item['nutshell']!=None: #nutshell이 없는것은 크로링하지 않기,output.txt에 저장하기.
            #print item['nutshell'][0]
            #aa=str(item['nutshell'][0].encode('utf-8'))
            print item['name']
            for a in item['name']:
                f.write(a.encode('utf-8'))
                f.write('-')
            f.write('+++')
            #f.write(item['name'][0].encode('utf-8'))
            f.write(item['nutshell'][0].encode('utf-8'))
            f.write("||")
            f.write(item['category'][1].encode('utf-8'))
            f.write(" > ")
            f.write(item['category'][2].encode('utf-8'))
            f.write(" > ")
            f.write(item['category'][3].encode('utf-8'))
            f.write("\n")


