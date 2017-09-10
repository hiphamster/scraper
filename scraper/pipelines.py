# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests

class ScraperPipeline(object):

    def post_results(self, item):
        url = 'http://e2107693.ngrok.io/leads_scraped'
        requests.post(url, files={'file': str(item)})

    def process_item(self, item, spider):
        self.post_results(item)
        return item

    def close_spider(self, spider):
        pass
