import scrapy
from ..items import AmazoncrawlItem

class AmazonSpidersSpider(scrapy.Spider):
    name = 'amazon_spiders'
    page_number = 2
    start_urls = ['https://www.amazon.in/s?k=clothing&rh=n%3A1571271031%2Cn%3A1953173031&dc&qid=1639767598&rnid=3576079031&ref=sr_nr_n_2']

    def parse(self, response):
        items = AmazoncrawlItem()
        p_brand = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "s-line-clamp-1", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "a-color-base", " " ))]').xpath('text()').getall()
        p_name = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "a-size-base-plus", " " )) and contains(concat( " ", @class, " " ), concat( " ", "a-text-normal", " " ))]').xpath('text()').getall()
        o_price = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "a-text-price", " " ))]//span').xpath('text()').getall()
        s_price = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "a-price-whole", " " ))]').xpath('text()').getall()
        image = response.css('.s-image').css('::attr(src)').getall()
        url = response.url
        category = response.xpath('//*[(@id = "departments")]//*[contains(concat( " ", @class, " " ), concat( " ", "a-text-bold", " " ))]').xpath('text()').getall()

        items['p_brand'] = p_brand
        items['p_name'] = p_name
        items['o_price'] = o_price
        items['s_price'] = s_price
        items['image'] = image
        items['url'] = url
        items['category'] = category

        yield items

        next_page = 'https://www.amazon.in/s?k=clothing&i=apparel&rh=n%3A1571271031%2Cn%3A1953173031&dc&page=' + str(AmazonSpidersSpider.page_number) + '&qid=1648063354&rnid=3576079031&ref=sr_pg_' + str(AmazonSpidersSpider.page_number)
        if AmazonSpidersSpider.page_number <= 334:
            yield response.follow(next_page, callback=self.parse)
            AmazonSpidersSpider.page_number += 1

pass
