import scrapy


class AuthorsSpider(scrapy.Spider):
    name = "authors"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]
    custom_settings = {
        'FEED_URI': 'authors.json',
        'FEED_FORMAT': 'json'
    }

    BASE_URL = 'https://quotes.toscrape.com'

    def parse(self, response,):
        autors_url = response.xpath('//a[contains(text(), "(about)")]/@href').getall()
        for autors in autors_url:
            yield response.follow(autors, callback=self.parse_autor_page)

        next_link = response.xpath("//li[@class='next']/a/@href").get()
        if next_link:
            yield scrapy.Request(url=self.start_urls[0] + next_link)

    def parse_autor_page(self, response):
        yield {
            "fullname": response.xpath('//h3[@class="author-title"]/text()').get(),
            "born_date": response.xpath('//span[@class="author-born-date"]/text()').get(),
            "born_location": response.xpath('//span[@class="author-born-location"]/text()').get(),
            "description": response.xpath('//div[@class="author-description"]/text()').get().replace(u'\n', u'')
        }



