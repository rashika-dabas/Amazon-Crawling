# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazoncrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    p_brand = scrapy.Field() # product brand
    p_name = scrapy.Field() # product name
    o_price = scrapy.Field() # product original price
    s_price = scrapy.Field() # product selling price
    image = scrapy.Field() # product image
    url = scrapy.Field() # product url
    category = scrapy.Field() # product category
    pass
