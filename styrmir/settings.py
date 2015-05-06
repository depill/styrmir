# -*- coding: utf-8 -*-

# Scrapy settings for styrmir project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'styrmir'

SPIDER_MODULES = ['styrmir.spiders']
NEWSPIDER_MODULE = 'styrmir.spiders'
ITEM_PIPELINES = [
        'styrmir.pipelines.StyrmirPipeline'
    ]
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'styrmir (+http://www.yourdomain.com)'
