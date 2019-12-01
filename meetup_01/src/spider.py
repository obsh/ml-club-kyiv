import scrapy


class LunSpider(scrapy.Spider):
    name = 'lun_spider'
    start_urls = ['https://flatfy.lun.ua/uk/%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6-%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80-%D0%BA%D0%B8%D1%97%D0%B2?page={}'.format(page) for page in range(1, 101)]

    def parse(self, response):
        for article in response.css('article.jss140'):
            record = {
                'street': article.css('a.jss159 ::text').get(),
                'district': article.css('a.jss166 ::text').getall(),
                'price': article.css('div.jss171 ::text').get(),
                'short_description': article.css('div.jss179 ::text').get(),
                'image': article.css('picture > source::attr(srcset)').get(),
                'attributes': [],
            }
            for ul in article.css('ul.jss174'):
                record['attributes'].append(ul.css('li.jss175 ::text').getall())

            yield record
