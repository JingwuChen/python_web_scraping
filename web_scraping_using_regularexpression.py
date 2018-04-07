#coding=utf-8
import requests
import  json
import re

#定义头文件
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36','Accept-Language':'zh-CN,zh;q=0.8',
'Cookie':'bid="q6fbJVZCZcs"; ll="129059"; viewed="1461903_25798756"; gr_user_id=17f8b890-3226-4b8c-8a33-19481d21c178; ct=y; ap=1; \
ps=y; ue="sohoyouwo0301@hotmail.com"; dbcl2="68474246:tuPrCpg3IbA"; ck=4zDa; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1478433025%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DoHPx3751eMnMMm9iyzClcSDRSmWhzim_3mM1td0Ym2ol4Ghi2O7SlFzwdlDIVagC%26wd%3D%26eqid%3D9367338900030a6e00000006581f18e4%22%5D; __utmt=1; _pk_id.100001.4cf6=2b1ca60bb40ba53d.1451820168.46.1478433720.1477797647.; _pk_ses.100001.4cf6=*; __utmt_douban=1; __utma=30149280.881850140.1451459636.1478091747.1478433025.61; __utmb=30149280.6.10.1478433025;\
 __utmc=30149280; __utmz=30149280.1478433025.61.59.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=30149280.6847; __utma=223695111.1262847605.1451820168.1477797641.1478433025.46; __utmb=223695111.0.10.1478433025; __utmc=223695111; __utmz=223695111.1478433025.46.45.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; \
 push_noty_num=0; push_doumail_num=0; _vwo_uuid_v2=7403936E788E89D96F646C0546AE8D24|198cc1af87ffdd895bb27b479442a250'}
# url='https://movie.douban.com/j/search_subjects?type=movie&tag=%E5%8D%8E%E8%AF%AD&sort=recommend&page_limit=20&page_start=0'
#获取豆瓣每个页面的链接
def get_link(start,end):
    urls=[]
    for i in range(start,end,20):
        url='https://movie.douban.com/j/search_subjects?type=movie&tag=%E5%8D%8E%E8%AF%AD&sort=recommend&page_limit=20&page_start={}'.format(str(i))
        urls.append(url)
    return urls
#获取每部电影的详情页面链接
def get_page(url):
    web_data = requests.get(url, headers=headers)#对网页进行解析
    s1 = json.loads(web_data.content)
    titles = []
    rates = []
    urls = []
    # images = []
    for i in s1['subjects']:
        titles.append(i['title'].encode('utf-8'))
        rates.append(i['rate'].encode('utf-8'))
        urls.append(i['url'])
        # images.append(i['cover'])
    content={'titles':titles,'rates':rates,'urls':urls}
    return  content


# url1='https://movie.douban.com/subject/25827935/'
#获取单部电影中导演，编剧，演员，发行日期，类型，评分
def get_content(url):
    web_data=requests.get(url,headers=headers)#对网页进行解析
    people = re.findall(r"<span class='attrs'><a .*?>(.*?)</a></span>", web_data.content, re.S | re.M)
    split_people = r'</a> / <a.*?>'
    find_type = r'<span property="v:genre">(.*?)</span>'
    find_date = r'<span property="v:initialReleaseDate".*?>(.*?)</span>'
    find_vote = r'<span property="v:votes">(\w+)</span>'
    # find_rate = r'<strong class="ll rating_num" property="v:average">(.*?)</strong>'
    find_award = r'<ul class="award">\s+<li>.*?</li>\s+<li>(.*?)</li>'
    # find_title = r'<span property="v:itemreviewed">(.*?)</span>'
    if len(people) == 3:
        directors = re.split(split_people, people[0]) if re.findall(split_people, people[0]) else people[0]
        scripters = re.split(split_people, people[1]) if re.findall(split_people, people[1]) else people[1]
        actors = re.split(split_people, people[2])
    else:
        directors = re.split(split_people, people[0]) if re.findall(split_people, people[0]) else people[0]
        scripters = None
        actors = re.split(split_people, people[1])
    types = re.findall(find_type, web_data.content, re.S | re.M)
    dates = re.findall(find_date, web_data.content, re.S | re.M)
    if dates:
        m = re.match('\d{4}(-\d{1,2}-\d{1,2})?', dates[0])
        date = m.group()
    else:
        date = None
    vote = re.findall(find_vote, web_data.content, re.S | re.M)[0]
    # rate = re.findall(find_rate, web_data.content, re.S | re.M)[0]
    awards = re.findall(find_award, web_data.content, re.S | re.M)

    # 把名称全部连接起来，方面导入mysql

    # title = re.findall(find_title, web_data.content, re.S | re.M)[0]
    if isinstance(awards, list):
        award = ",".join(awards)
    else:
        award = awards
    if isinstance(scripters, list):
        scripter = ",".join(scripters[0:3])
    else:
        scripter = scripters
    if isinstance(directors, list):
        director = ",".join(directors[0:2])
    else:
        director = directors
    if isinstance(types,list):
        type = ",".join(types[0:3])
    else:
        type = types
    if isinstance(actors,list):
        actor = ",".join(actors[0:4])
    else:
        actor = actors
    content = { 'director': director, 'scripter': scripter, 'actor': actor, 'type': type,
               'date': date, 'vote': vote, "award":award}
    return content

