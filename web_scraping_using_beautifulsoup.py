# coding=utf-8
import requests
from bs4 import BeautifulSoup as bs
import re
import time


headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36'}
#获取豆瓣每个页面的链接
def get_every_page(start,end):
    time.sleep(2)
    bigurls=[]
    for i in range(start,end):
        bigurls.append('http://cc.58.com/iphonesj/pn{}/'.format(str(i)))
    return bigurls

#获取每部电影的页面链接
def get_link(url):
    time.sleep(2)
    urls=[]
    web_data=requests.get(url,headers=headers)#对网页进行解析
    soup=bs(web_data.text,'lxml')
    links=soup.select('td.t a.t')
    for link in links:
        urls.append(link.get('href'))
    return urls
#获取单部电影中导演，编剧，演员，发行日期，类型，评分
def get_content(url):
    web_data=requests.get(url,headers=headers)#对网页进行解析
    soup=bs(web_data.text,'lxml')
    desc=soup.select('h1.info_titile')
    price=soup.select('span.price_now i')
    area=soup.select('div.palce_li span i')
    view=soup.select('span.look_time')
    label=soup.select('span.qual_label')
    view_num=''
    for i in re.findall('\d',view[0].text.encode('utf-8')):
        view_num+=i
    content={
        'desc':desc[0].text.encode('utf-8'),
        'price':int(price[0].text),
        'area':area[0].text.encode('utf-8') if soup.find_all('div','palce_li','span') else None,
        'view':int(view_num)
    }
    return content



