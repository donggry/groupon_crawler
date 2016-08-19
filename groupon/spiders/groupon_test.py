# -- coding: utf-8 --
import datetime
import scrapy
from groupon.items import GrouponItem
count=0
now = datetime.datetime.now()
nowTuple = now.timetuple()
day=nowTuple.tm_mday
hour=nowTuple.tm_hour
#time=str(day)+"-"+str(hour)
time = str(now)
global time
f=open('output.txt','w')
class Grouponspider(scrapy.Spider):
    f.write('\n')
    temp = 0
    name = "groupon3"#컴파일 이름 scrapy crawl groupon 하면 된다->output.txt.에 결과 저장됨
    allowed_domains = ["groupon.com"]
    start_urls = []
    start_url_list = ["https://www.groupon.com/goods/home-and-garden"
    ]
    for j in range(0,1):
        start_url_1 = start_url_list[j]
        start_urls.append(start_url_1)
        for i in range(1,2):
            start_url_0 = start_url_list[j] + "&page=" + str(i)
            start_urls.append(start_url_0)

    def parse(self, response):#시작주소에서 링크로 타고 넘어가기
        # 시작주소에는 30개의 아이템이 있다 각각의 30개의 아이ㅣ템에 걸린 링크를 타고 넘어간뒤에 크롤링 해주기 위함

            url="https://www.groupon.com/deals/gg-crystal-studs-with-swarovski-elements"
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        item = GrouponItem()
        #print response
        f.write(str(response))
        f.write('\n')

        #item['id'] = response.xpath('//div[@class="options-metadata"]/')
        item['id'] = response.css('div.options-metadata > meta').xpath('@content').extract()#id
        item['nutshell'] = response.xpath('//div[@class="nutshell highlights "]/p/text()').extract()#nutshell
        item['category'] = response.xpath('//section[@class="breadcrumbs"]//a/text()').extract()#category
        item['name']=response.xpath('//div[@itemprop="description"]/h4/text()').extract()
        item['contents1'] = response.xpath('//div[@itemprop="description"]/p/text()').extract()
        item['contents2']=response.xpath('//div[@itemprop="description"]/ul/li/text()').extract()
        print item['contents1']
        print"aaaaaaaaaaaaaaaaaaaaaaaaa"
        print item['contents2']

        f.write(item['id'][1])
        f.write('||')
        f.write(item['name'][0].encode('utf-8'))


        count=0
        #item['contents1']=item['contents1'].replace("\n",'-')
        if item['contents1']!=None:
            for b in item['contents1']:
                b=b.replace("\n",'')
                if len(b)<=1:
                    continue
                f.write(b.encode('utf-8'))
        f.write('\n')
        if item['contents2'] != None:
            for a in item['contents2']:
                #print a.xpath('ul/li/text()').extract()
            #f.write(len(a)+'\n')
                #f.write(str(len(a)))
                if '\n' in a:
                    count=count+1
                    continue
                if len(a)<=3:
                    count = count + 1
                    f.write("aaaaaaaaaaa")
                    continue
                else:
                    f.write(a.encode('utf-8'))
                    f.write('\n')
                    count=count+1


        #print item['id'][0]
        #print item['id'][1]


