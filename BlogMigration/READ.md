# BlogMigration
A python project based on [Scrapy][1] helps me crawl my former articles in http://www.cnblogs/neillee.

一个基于[Scrapy][1]的 Python 项目。主要用于爬取早期我在博客站点 http://www.cnblogs/neillee 发布的文章。


It crawls the content and meta-data, such as posts-view-count and finally transforms these html content into local markdown files,in order to post them on my new blog site —— http://cnneillee.github.io. These markdown files are formated in line with the [hexo][2] posts rules.

它将爬取到的 html 内容转化为 markdown 形式的本地文件，以便我能够在我的新博客站点 http://cnneillee.github.io 进行发布。这些 Markdown 文件都是被格式化了的，符合 [hexo][2] 博客文章的格式要求。

# Libs
Following libs are used in this project:

以下关键库被使用在本项目中：

- [Scrapy][1]
- [html2text][3]


[1]: https://github.com/scrapy/scrapy
[2]: https://hexo.io
[3]: https://github.com/aaronsw/html2text
