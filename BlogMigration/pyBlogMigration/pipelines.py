# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pyBlogMigration.spiders import utils


class ArticlePipeline(object):
    def process_item(self, item, spider):
        utils.to_md_file(item)
        return item
