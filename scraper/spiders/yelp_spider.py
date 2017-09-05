import scrapy
from lxml import html


class YelpSpider(scrapy.Spider):
    name = 'yelper'

    custom_settings = {
        'USER_AGENT': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/60.0.3112.101 Safari/537.36')
    }

    def start_requests(self):
        urls = [
            'https://www.yelp.com/search?find_desc=coffee&find_loc=Berkeley%2C+CA&ns=1'
        ]
        for url in urls:
            req = scrapy.Request(url=url, callback=self.parse)
            yield req

    def parse(self, response):
        html_tree = html.fromstring(str(response.body, 'utf-8'))

        for listing in html_tree.findall('.//div[@class="biz-listing-large"]'):
            name = listing.find(
                './/a[@data-analytics-label="biz-name"]/span').text.strip()
            phone = listing.find('.//span[@class="biz-phone"]').text.strip()

            yield {'name': name, 'phone': phone}
            
        """
        next_page = html_tree.find(
            './/a[@class="u-decoration-none next pagination-links_anchor"]')
        if (next_page):
            next_page = response.urljoin(next_page.get('href'))
            yield scrapy.Request(url=next_page, callback=self.parse)
        """
