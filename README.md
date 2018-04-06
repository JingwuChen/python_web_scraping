# python_web_scraping
本文采用beautifulsoup和正则表达式进行网页爬虫
##beautifulsoup是个非常厉害的python爬虫库，可以大幅度降低爬虫的难度，获取标签内容的方法主要有两种：find方法和select方法
###find方法，注意find返回的是一个DOM对象
[find()](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#find)
`find( name , attrs , recursive , text , **kwargs )`

find_all() 方法将返回文档中符合条件的所有tag,尽管有时候我们只想得到一个结果.比如文档中只有一个<body>标签,那么使用 find_all() 方法来查找<body>标签就不太合适, 使用 find_all 方法并设置 limit=1 参数不如直接使用 find() 方法.下面两行代码是等价的:

`soup.find_all('title', limit=1)`
`# [<title>The Dormouse's story</title>]`

`soup.find('title')`
`# <title>The Dormouse's story</title>`
唯一的区别是 find_all() 方法的返回结果是值包含一个元素的列表,而 find() 方法直接返回结果.

find_all() 方法没有找到目标是返回空列表, find() 方法找不到目标时,返回 None .

`print(soup.find("nosuchtag"))`
`# None`
soup.head.title 是 tag的名字 方法的简写.这个简写的原理就是多次调用当前tag的 find() 方法:

`soup.head.title`
`# <title>The Dormouse's story</title>`

`soup.find("head").find("title")`
`# <title>The Dormouse's story</title>`
###select方法，注意select方法返回的是一个列表
Beautiful Soup支持大部分的CSS选择器[1](http://www.w3school.com.cn/css/css_selector_type.asp),在 Tag 或 BeautifulSoup 对象的 .select() 方法中传入字符串参数,即可使用CSS选择器的语法找到tag:
通过tag标签逐层查找:
```python
soup.select("body a")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie"  id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.select("html head title")
# [<title>The Dormouse's story</title>]
找到某个tag标签下的直接子标签 [6] :

soup.select("head > title")
# [<title>The Dormouse's story</title>]

soup.select("p > a")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie"  id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.select("p > a:nth-of-type(2)")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

soup.select("p > #link1")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

soup.select("body > a")
# []
```
##正则表达式直接查找解析过的网页内容

虽然掌握起来较难，但是胜在更灵活。当然作为编程者，不管是学什么语言，都需掌握正则表达式，python正则式可以参考[这篇文章](https://www.cnblogs.com/wxshi/p/6827056.html)，在线测试正则表达式见[这个网址](https://regexr.com/)
