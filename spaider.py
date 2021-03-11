import requests # 作用： 模拟浏览器去发起请求
from lxml import etree
# 1. 获取网页源码
res = requests.get('https://www.qiushibaike.com/video/').text

html = etree.HTML(res)

srcs = html.xpath('//*[@id="content"]/div/div[2]/div/video/source/@src')

# print(srcs)





