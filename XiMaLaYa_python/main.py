# -*- coding: utf-8 -*-
"""
    author：李林茂
    date：2016/12/21
"""
import json
from operator import itemgetter

import requests

"""预先对喜马拉雅的android app做了抓包分析操作，分析得到对[url+params]执行get请求，即可获得一些数据。
因此，本程序针对该接口进行数据请求，获得“卓老板”的按播放量从大到小排列专辑搜索的json数据。
最后，对json数据进行一系列的操作，即可达到目的。
url：http://search.ximalaya.com/front/v1
params：?condition=play&core=album&device=android&kw=%E5%8D%93%E8%80%81%E6%9D%BF&live=true&page=1&paidFilter=false&rows=20&spellchecker=true&version=5.4.69

condition：搜索条件，相关度(relation)、最新上传(recent)、最多播放(play)
core：搜索方式，全部(all)、专辑(album)、声音(track)、用户(user)、广播(live)
device：设备，目前仅测试了android
kw：关键字，即key word
live：
page：页码，第x页
rows：行数
paidFilter：支付筛选，true、false
spellchecker：拼写检查，true、false
version：软件版本号
"""


def makeRequest():
    """
    构建针对接口的请求
    :return:返回请求得到的内容
    """
    payload = {'condition': 'play', 'core': 'album',
               'device': 'android', 'kw': '卓老板',
               'live': 'true', 'page': '1', 'paidFilter': 'false',
               'version': '5.4.69', 'rows': '20', 'spellchecker': 'true'}
    url = 'http://search.ximalaya.com/front/v1'
    return requests.get(url, payload).content


# 解析json数据
def decodingJson(data):
    """
    将content（字符串对象）解析成json对象
    :param data: 字符串内容
    :return: 解析出的json对象
    """
    return json.loads(data)


if __name__ == '__main__':
    # 网络请求获得内容
    content = makeRequest()

    # 解析str内容成json对象
    pyObj = decodingJson(content)

    # 从json对象中抽取出一个一个的专辑，去除其他数据
    docs = pyObj[u'response'][u'docs']

    # 抽取出需要的内容并合并成元组列表
    result = [{u'totalPlayCount': doc[u'play'], u'title': doc[u'title'], u'anchorman': doc[u'nickname'],
               u'info': doc[u'intro']} for doc in docs]

    # 由于从接口获得的数据是不一定按照顺序的，此处更改数据，从大到小
    sortedResult = sorted(result, key=itemgetter(u'totalPlayCount'), reverse=True)

    for res in sortedResult:
        print (json.dumps(res)).decode('unicode_escape')

