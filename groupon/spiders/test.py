# -- coding: utf-8 --
import datetime
import scrapy
from groupon.items import GrouponItem
count=0
now = datetime.datetime.now()
nowTuple = now.timetuple()
day=nowTuple.tm_mday
hour=nowTuple.tm_hour
time=str(day)+"-"+str(hour)
global time
f=open('health_beauty.txt','w')
class Grouponspider(scrapy.Spider):
    temp = 0
    name = "groupon0"#컴파일 이름 scrapy crawl groupon 하면 된다->output.txt.에 결과 저장됨
    allowed_domains = ["groupon.com"]
    start_urls = []
    #고칠부분입니다. 원하는 유알엘 주소를 리스트로 넣은뒤 그갯수를
    start_url_list = ["https://www.groupon.com/goods?category=health-and-beauty",
"https://www.groupon.com/goods?category=health-and-beauty&category2=bath-and-body",
"https://www.groupon.com/goods?category=health-and-beauty&category3=v1-bath-accessories",
"https://www.groupon.com/goods?category=health-and-beauty&category3=bath-salts-and-bubble-baths",
"https://www.groupon.com/goods?category=health-and-beauty&category3=body-cleansers",
"https://www.groupon.com/goods?category=health-and-beauty&category3=body-moisturizers",
"https://www.groupon.com/goods?category=health-and-beauty&category3=body-scrubs-and-exfoliants",
"https://www.groupon.com/goods?category=health-and-beauty&category3=hands-and-feet",
"https://www.groupon.com/goods?category=health-and-beauty&category2=cosmetics",
"https://www.groupon.com/goods?category=health-and-beauty&category3=cosmetic-bags-and-cases",
"https://www.groupon.com/goods?category=health-and-beauty&category3=makeup-brushes-and-applicators",
"https://www.groupon.com/goods?category=health-and-beauty&category3=eye-makeup",
"https://www.groupon.com/goods?category=health-and-beauty&category3=face-makeup",
"https://www.groupon.com/goods?category=health-and-beauty&category3=lips",
"https://www.groupon.com/goods?category=health-and-beauty&category3=makeup-palettes",
"https://www.groupon.com/goods?category=health-and-beauty&category3=mirrors-and-cosmetic-tools",
"https://www.groupon.com/goods?category=health-and-beauty&category3=nails",
"https://www.groupon.com/goods?category=health-and-beauty&category2=fragrances",
"https://www.groupon.com/goods?category=health-and-beauty&category3=mens-cologne",
"https://www.groupon.com/goods?category=health-and-beauty&category3=perfume",
"https://www.groupon.com/goods?category=health-and-beauty&category2=v1-hair-care",
"https://www.groupon.com/goods?category=health-and-beauty&category3=hair-accessories",
"https://www.groupon.com/goods?category=health-and-beauty&category3=hair-color",
"https://www.groupon.com/goods?category=health-and-beauty&category3=shampoo-and-conditioner",
"https://www.groupon.com/goods?category=health-and-beauty&category3=hair-styling-products",
"https://www.groupon.com/goods?category=health-and-beauty&category3=hair-styling-tools",
"https://www.groupon.com/goods?category=health-and-beauty&category2=health-care",
"https://www.groupon.com/goods?category=health-and-beauty&category3=compression-products",
"https://www.groupon.com/goods?category=health-and-beauty&category3=independent-living-aids",
"https://www.groupon.com/goods?category=health-and-beauty&category3=first-aid",
"https://www.groupon.com/goods?category=health-and-beauty&category3=health-monitors",
"https://www.groupon.com/goods?category=health-and-beauty&category3=healthy-living",
"https://www.groupon.com/goods?category=health-and-beauty&category3=v2-humidifiers",
"https://www.groupon.com/goods?category=health-and-beauty&category3=medical-braces",
"https://www.groupon.com/goods?category=health-and-beauty&category3=medicine-cabinet-essentials",
"https://www.groupon.com/goods?category=health-and-beauty&category3=mobility-aids",
"https://www.groupon.com/goods?category=health-and-beauty&category3=pain-relief",
"https://www.groupon.com/goods?category=health-and-beauty&category3=sleep-aids",
"https://www.groupon.com/goods?category=health-and-beauty&category2=massage-and-relaxation",
"https://www.groupon.com/goods?category=health-and-beauty&category3=acupuncture-and-acupressure",
"https://www.groupon.com/goods?category=health-and-beauty&category3=foot-and-leg-massagers",
"https://www.groupon.com/goods?category=health-and-beauty&category3=handheld-massagers",
"https://www.groupon.com/goods?category=health-and-beauty&category3=head-massagers",
"https://www.groupon.com/goods?category=health-and-beauty&category3=massage-accessories",
"https://www.groupon.com/goods?category=health-and-beauty&category3=massage-oils-aromatherapy-and-lotions",
"https://www.groupon.com/goods?category=health-and-beauty&category3=pulse-massagers",
"https://www.groupon.com/goods?category=health-and-beauty&category3=total-body-massages",
"https://www.groupon.com/goods?category=health-and-beauty&category2=v1-personal-care",
"https://www.groupon.com/goods?category=health-and-beauty&category3=body-treatments",
"https://www.groupon.com/goods?category=health-and-beauty&category3=deodorants-and-antiperspirants",
"https://www.groupon.com/goods?category=health-and-beauty&category3=eye-care",
"https://www.groupon.com/goods?category=health-and-beauty&category3=feminine-care",
"https://www.groupon.com/goods?category=health-and-beauty&category3=foot-care",
"https://www.groupon.com/goods?category=health-and-beauty&category3=hair-removal-goods",
"https://www.groupon.com/goods?category=health-and-beauty&category3=incontinence-products",
"https://www.groupon.com/goods?category=health-and-beauty&category3=v1-dental-care",
"https://www.groupon.com/goods?category=health-and-beauty&category3=pregnancy-and-fertility",
"https://www.groupon.com/goods?category=health-and-beauty&category3=sexual-health",
"https://www.groupon.com/goods?category=health-and-beauty&category3=v1-shaving",
"https://www.groupon.com/goods?category=health-and-beauty&category2=v1-sexual-health",
"https://www.groupon.com/goods?category=health-and-beauty&category3=sex-toys-for-couples",
"https://www.groupon.com/goods?category=health-and-beauty&category3=male-sex-toys",
"https://www.groupon.com/goods?category=health-and-beauty&category3=female-sex-toys",
"https://www.groupon.com/goods?category=health-and-beauty&category3=anal-toys",
"https://www.groupon.com/goods?category=health-and-beauty&category3=bondage-and-fetish-kits",
"https://www.groupon.com/goods?category=health-and-beauty&category3=sex-games-and-mood-setters",
"https://www.groupon.com/goods?category=health-and-beauty&category3=intimate-apparel-and-hosiery",
"https://www.groupon.com/goods?category=health-and-beauty&category3=lubricant-and-massage-oil",
"https://www.groupon.com/goods?category=health-and-beauty&category3=novelties",
"https://www.groupon.com/goods?category=health-and-beauty&category3=sexual-supplements",
"https://www.groupon.com/goods?category=health-and-beauty&category2=v1-skin-care",
"https://www.groupon.com/goods?category=health-and-beauty&category3=cellulite-and-stretch-marks",
"https://www.groupon.com/goods?category=health-and-beauty&category3=cleanse",
"https://www.groupon.com/goods?category=health-and-beauty&category3=v1-hair-removal",
"https://www.groupon.com/goods?category=health-and-beauty&category3=moisturizer",
"https://www.groupon.com/goods?category=health-and-beauty&category3=suncare-and-tanning",
"https://www.groupon.com/goods?category=health-and-beauty&category3=skin-treatments-and-serum",
"https://www.groupon.com/goods?category=health-and-beauty&category2=v3-vitamins-and-supplements",

]
                          
    for j in range(0,len(start_url_list)):#여기에 숫자를 반영하시면 됩니다.(고칠부분입니다.)
        start_url_1 = start_url_list[j]
        start_urls.append(start_url_1)
        for i in range(1,20):
            start_url_0 = start_url_list[j] + "&page=" + str(i)
            start_urls.append(start_url_0)

    def parse(self, response):#시작주소에서 링크로 타고 넘어가기
        # 시작주소에는 30개의 아이템이 있다 각각의 30개의 아이ㅣ템에 걸린 링크를 타고 넘어간뒤에 크롤링 해주기 위함
        for href in response.css("div.browse-deals > figure > a::attr('href')"):
            url = response.urljoin(href.extract())

            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        item = GrouponItem()
        item['id'] = response.css('div.options-metadata > meta').xpath('@content').extract()  # id
        item['nutshell'] = response.xpath('//div[@class="nutshell highlights "]/p/text()').extract()  # nutshell
        item['category'] = response.xpath('//section[@class="breadcrumbs"]//a/text()').extract()  # category
        item['name'] = response.xpath('//hgroup/h1/text()').extract()
        item['contents1'] = response.xpath('//div[@itemprop="description"]/p/text()').extract()
        item['contents2'] = response.xpath('//div[@itemprop="description"]/ul/li/text()').extract()

        f.write(str(item['id'][1]))
        f.write('||')
        #f.write(str(response))
        #f.write('||')

        f.write(item['name'][0].strip().encode('utf-8'))
        f.write(" ")
        if len(item['nutshell'])>=1:
            tmp_str = str(item['nutshell'][0].encode('utf-8'))
            tmp_str = tmp_str.replace('é', 'e')
            tmp_str = tmp_str.replace('\n', ' ')
            tmp_str = tmp_str.replace('\t', ' ')
            item['nutshell'][0] = tmp_str

            f.write(item['nutshell'][0] + ' ')


        if item['contents1'] != None:
            for b in item['contents1']:
                b = b.replace("\n", '')
                if len(b) <= 1:
                    continue
                f.write(b.encode('utf-8'))
                f.write(' ')
        if item['contents2'] != None:
            for a in item['contents2']:

                if '\n' in a:
                    continue
                if len(a) <= 3:
                    continue
                else:
                    f.write(a.encode('utf-8'))
                    f.write(' ')


        f.write("||")
        count=0
        for a in item['category']:
            if count==1:
                f.write(a)
            elif count==2:
                f.write(" > ")
                f.write(a)
            elif count==3:
                if len(a)<=1:
                    break
                f.write(" > ")
                f.write(a)
            count=count+1

        f.write("\n")


