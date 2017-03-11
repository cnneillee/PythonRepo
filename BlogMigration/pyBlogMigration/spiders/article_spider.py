# -*- coding: utf-8 -*-

import scrapy

from pyBlogMigration.items import Article


class ArticleSpider(scrapy.Spider):
    name = "article"
    allowed_domains = ["cnblogs.com"]
    start_urls = [
        "http://www.cnblogs.com/neillee/p/"
    ]
    pages = None

    def parse(self, response):
        self.pages = response.xpath('//div[@class="Pager"]/a/@href').extract()
        self.pages.append("/neillee/p/?page=1")
        for page in self.pages:
            yield scrapy.Request("http://www.cnblogs.com" + page, callback=self.parse_page)

    def parse_page(self, response):
        req_url = response.url
        titles = response.xpath('//div[@class="postTitl2"]/a/text()').extract()
        filename = ("H:\\Hexo\\github-io\\blogMigration\\" + req_url.split("=")[1] + "---%d.txt") % len(titles)
        with open(filename, 'wb') as f:
            f.write(str(titles).encode('utf-8'))

        for url in response.xpath('//div[@class="postTitl2"]/a/@href').extract():
            yield scrapy.Request(url, callback=self.parse_article)

    def parse_article(self, response):
        article = Article()
        self.get_title(article, response)
        self.get_date(article, response)
        self.get_read_num(article, response)
        self.get_categories(article, response)
        self.get_tags(article, response)
        self.get_content(article, response)
        yield article

    def get_title(self, article, sel):
        regx = '//h1[@class="postTitle"]/a/text()'
        article['title'] = sel.xpath(regx).extract_first()
        # print "title:" + article['title']

    def get_date(self, article, sel):
        regx = '//div[@class="postDesc"]/span[@id="post-date"]/text()'
        article['date'] = sel.xpath(regx).extract_first()
        # print "date:" + article['date']

    def get_read_num(self, article, sel):
        regx = '//div[@class="postDesc"]/span[@id="post_view_count"]/text()'
        article['readNum'] = sel.xpath(regx).extract_first()
        # print "readNum:" + article['readNum']

    def get_categories(self, article, sel):
        regx = '//div[@id="BlogPostCategory"]/a/text()'
        article['categories'] = sel.xpath(regx).extract_first()

    def get_tags(self, article, sel):
        regx = '//div[@id="EntryTag"]/a/text()'
        article['tags'] = sel.xpath(regx).extract_first()

    def get_content(self, article, sel):
        regx = '//div[@id="cnblogs_post_body"]'
        article['content'] = sel.xpath(regx).extract_first()
