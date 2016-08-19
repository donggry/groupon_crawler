# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GrouponItem(scrapy.Item):
    # define the fields for your item here like:
    id=scrapy.Field()
    name = scrapy.Field()
    contents1=scrapy.Field()
    contents2=scrapy.Field()
    time=scrapy.Field()
    nutshell = scrapy.Field()
    category = scrapy.Field()

    pass
