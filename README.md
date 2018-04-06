# python_web_scraping
本文采用beautifulsoup和正则表达式进行网页爬虫
##beautifulsoup是个非常厉害的python爬虫库，可以大幅度降低爬虫的难度，获取标签内容的方法主要有两种：
```python
        [find()](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#find)
find( name , attrs , recursive , text , **kwargs )

find_all() 方法将返回文档中符合条件的所有tag,尽管有时候我们只想得到一个结果.比如文档中只有一个<body>标签,那么使用 find_all() 方法来查找<body>标签就不太合适, 使用 find_all 方法并设置 limit=1 参数不如直接使用 find() 方法.下面两行代码是等价的:

soup.find_all('title', limit=1)
# [<title>The Dormouse's story</title>]

soup.find('title')
# <title>The Dormouse's story</title>
唯一的区别是 find_all() 方法的返回结果是值包含一个元素的列表,而 find() 方法直接返回结果.

find_all() 方法没有找到目标是返回空列表, find() 方法找不到目标时,返回 None .

print(soup.find("nosuchtag"))
# None
soup.head.title 是 tag的名字 方法的简写.这个简写的原理就是多次调用当前tag的 find() 方法:

soup.head.title
# <title>The Dormouse's story</title>

soup.find("head").find("title")
# <title>The Dormouse's story</title>
```
##正则表达式直接查找解析过的网页内容
虽然掌握起来较难，但是胜在更灵活。当然作为编程者，不管是学什么语言，都需掌握正则表达式，python正则式可以参考[这篇文章](https://www.cnblogs.com/wxshi/p/6827056.html)，在线测试正则表达式见[这个网址](https://regexr.com/)
