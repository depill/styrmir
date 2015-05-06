# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from ..items import StyrmirItem
from datetime import datetime, timedelta
import locale

class StyrmirSpider(CrawlSpider):
    name, start_urls = 'styrmir', ['http://www.styrmir.is']
    rules = (Rule(SgmlLinkExtractor(allow=('entry\.html\?entry_id=\d+$', ), ), callback="parse_items", follow=True), )

    def parse_items(self, response):
        locale.setlocale(locale.LC_ALL, 'is_IS.UTF-8')

        hxs = Selector(response)
        entry = hxs.xpath('//div[@class="clear styrmir-entry"]')
        styrmir_entry = entry[0]
        styrmir = StyrmirItem()

        styrmir['link'] = response.url
        styrmir['blog'] = styrmir_entry.xpath('//div[@class="styrmir-entry-body"]').extract()[0]
        styrmir['date_text'] = styrmir_entry.xpath('//div[@class="styrmir-dags"]/text()').extract()[0].strip().encode('utf-8').replace('\xc3\x9e', '\xc3\xbe')
        styrmir['date'] = datetime.strptime(styrmir['date_text'], "%A, %d. %B %Y")
        styrmir['title'] = styrmir_entry.xpath('//h2/a/text()').extract()[0]

        return styrmir