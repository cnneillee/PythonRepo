# -*- coding: utf-8 -*-
import html2text
import re

migrationDesc = '\n\n\n*本文从我的另一个 blog [http://www.cnblogs/neillee](http://www.cnblogs/neillee) 中同步过来，' \
                '同步过程使用了 python 脚本，文章[cnblogs博客迁移过程](http://cnneillee.github.io/2017/02/26/' \
                'cnblogs%E5%8D%9A%E5%AE%A2%E8%BF%81%E7%A7%BB%E8%BF%87%E7%A8%8B/)' \
                '详细介绍了同步过程，并附有源码！*'

migrationExtra = '\n\n*截至博客迁移时，cnblogs上的访问量为：*'


def to_md_file(article):
    filename = "H:\\Hexo\\github-io\\blogMigration\\" + correct_win_filename(article['title']) + '.md'
    with open(filename, 'wb') as f:
        f.write('---')
        f.write('\ntitle: ')
        if article['title'] is not None:
            f.write(article['title'])
        f.write('\ndate: ')
        if article['date'] is not None:
            f.write(article['date'])
        f.write('\ncategories: ')
        if article['categories'] is not None:
            f.write(article['categories'])
        f.write('\ntags: ')
        if article['tags'] is not None:
            f.write(article['tags'])
        f.write('\n---\n')
        md_content = html2text.html2text(article['content'])
        f.write(md_content)
        f.write(migrationDesc)
        f.write(migrationExtra)
        if article['readNum'] is not None:
            f.write(article['readNum'])
        f.flush()
        # print article['title']


def is_legal_win_filename(filename):
    pattern = re.compile(r'<|>|/|\\|||:|"|\*|\?')
    match = pattern.match(filename)
    if match is None:
        return True
    else:
        return False


def correct_win_filename(filename):
    if is_legal_win_filename(filename):
        return filename
    my_dict = {"<": "-", ">": "-", "\\": "-", "/": "-", "|": "-", ":": "-", "\"": "-", "*": "-", "?": "-"}
    return multiple_replace(filename, my_dict)


def multiple_replace(text, adict):
    rx = re.compile('|'.join(map(re.escape, adict)))

    def one_xlat(match):
        return adict[match.group(0)]

    return rx.sub(one_xlat, text)
