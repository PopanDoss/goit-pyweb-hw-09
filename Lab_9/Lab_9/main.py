import scrapy
from scrapy.crawler import CrawlerProcess
from  spiders.authors import AuthorsSpider
from spiders.quotes import  QuotesSpider



if __name__=='__main__':
    
    process = CrawlerProcess()

    process.crawl(QuotesSpider)
    process.crawl(AuthorsSpider)

    process.start()