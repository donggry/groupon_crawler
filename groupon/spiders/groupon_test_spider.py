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
    name = "groupon2"#컴파일 이름 scrapy crawl groupon 하면 된다->output.txt.에 결과 저장됨
    allowed_domains = ["groupon.com"]
    start_urls = []
    start_url_list = ["https://www.groupon.com/goods/home-and-garden",
                      "https://www.groupon.com/goods/jewelry-and-watches",
                      "https://www.groupon.com/goods/women",
                      "https://www.groupon.com/goods/health-and-beauty",
                      "https://www.groupon.com/goods/electronics",
                      "https://www.groupon.com/goods/baby-kids-and-toys",
                      "https://www.groupon.com/goods/sports-and-outdoors",
                      "https://www.groupon.com/goods/entertainment-and-media",
                      "https://www.groupon.com/goods/men",
                      "https://www.groupon.com/goods/auto-and-home-improvement",
                      "https://www.groupon.com/goods/groceries-alcohol-and-tobacco",
                      "https://www.groupon.com/goods/collectibles"
    ]
    for j in range(0,12):
        start_url_1 = start_url_list[j]
        start_urls.append(start_url_1)
        for i in range(1,20):
            start_url_0 = start_url_list[j] + "&page=" + str(i)
            start_urls.append(start_url_0)

    def parse(self, response):#시작주소에서 링크로 타고 넘어가기
        # 시작주소에는 30개의 아이템이 있다 각각의 30개의 아이ㅣ템에 걸린 링크를 타고 넘어간뒤에 크롤링 해주기 위함
        for href in response.css("div.browse-deals > figure > a::attr('href')"):
            url = response.urljoin(href.extract())
            #url="https://www.groupon.com/deals/gg-wireless-bluetooth-controllers-for-sony-playstation-3"
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        item = GrouponItem()
        #print response
        f.write(str(response))
        f.write('\n')

        #item['id'] = response.xpath('//div[@class="options-metadata"]/')
        #item['id'] = response.css('div.options-metadata > meta').xpath('@content').extract()#id
        item['nutshell'] = response.xpath('//div[@class="nutshell highlights "]/p/text()').extract()#nutshell
        item['category'] = response.xpath('//section[@class="breadcrumbs"]//a/text()').extract()#category
        item['id']=response.xpath('//div[@itemprop="description"]/h4/text()').extract()
        item['contents1'] = response.xpath('//div[@itemprop="description"]/p/text()').extract()
        item['contents2']=response.xpath('//div[@itemprop="description"]/ul/li/text()').extract()

        print item['contents1']
        print item['id']
        f.write(item['id'][0].encode('utf-8'))
        f.write('||')

        count = 0
        # item['contents1']=item['contents1'].replace("\n",'-')
        if item['contents1'] != None:
            for b in item['contents1']:
                b = b.replace("\n", '')
                if len(b) <= 1:
                    continue
                f.write(b.encode('utf-8'))
        f.write('\n')
        if item['contents2'] != None:
            for a in item['contents2']:
                # print a.xpath('ul/li/text()').extract()
                # f.write(len(a)+'\n')
                # f.write(str(len(a)))
                if '\n' in a:
                    count = count + 1
                    continue
                if len(a) <= 3:
                    count = count + 1
                    f.write("aaaaaaaaaaa")
                    continue
                else:
                    f.write(a.encode('utf-8'))
                    f.write('\n')
                    count = count + 1

        #print item['id'][0]
        #print item['id'][1]

        """
        tmp_str = str(item['nutshell'][0])
        tmp_str.replace('é','e')
        tmp_str.replace('\n',' ')
        tmp_str.replace('\t', ' ')
        tmp_str.strip()
        item['nutshell'][0] = tmp_str

        tmp_str = str(item['category'][3])
        tmp_str.replace('é', 'e')
        item['category'][3] = tmp_str
        item['time']=time
        #yield item
        #item['url']=response.url

        #if item['nutshell']!=None: #nutshell이 없는것은 크로링하지 않기,output.txt에 저장하기."""