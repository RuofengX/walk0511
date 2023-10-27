from typing import Iterable
import scrapy
from scrapy.http import Request


def url_generator(start: int):
    start_url = "https://bbs.my0511.com/viewthread.php?tid={}"
    while True:
        yield start_url.format(start)
        start += 1


class I2ratorSpider(scrapy.Spider):
    name = "i2rator"
    allowed_domains = ["bbs.my0511.com"]
    start_tid = 8572503

    def start_requests(self) -> Iterable[Request]:
        for url in url_generator(self.start_tid):
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response.url)
