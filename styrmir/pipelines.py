# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import PyRSS2Gen
import datetime
from os.path import expanduser,join
from collections import OrderedDict

class StyrmirPipeline(object):
    def __init__(self):
        self.items = {}

    def is_date_in_item(self, date):
        if date in self.items:
            return self.is_date_in_item(date + datetime.timedelta(0, 1))
        return date

    def process_item(self, item, spider):
        date = self.is_date_in_item(item['date'])

        self.items[date] = (
            PyRSS2Gen.RSSItem(
                title=item['title'],
                link=item['link'],
                description=item['blog'],
                guid=PyRSS2Gen.Guid(item['link']),
                pubDate=item['date'])
        )

    def close_spider(self, spider):
        self.items = OrderedDict(sorted(self.items.items(), key=lambda t: t[0], reverse=True))
        rss = PyRSS2Gen.RSS2(
            title='Styrmir.is',
            link='http://www.styrmir.is',
            description='Fréttir af forsíðu Styrmir.is',
            lastBuildDate=datetime.datetime.now(),

            items=[v for k,v in self.items.items()])

        rss.write_xml(open(join(expanduser('~'), 'html/styrmir.xml'), 'w'), encoding='utf-8')
