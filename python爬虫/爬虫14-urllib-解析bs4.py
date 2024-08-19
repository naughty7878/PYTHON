from bs4 import BeautifulSoup

soup = BeautifulSoup(open('爬虫14-urllib-解析bs4.html', 'r', encoding='utf-8'), 'lxml')

# print(soup)
# 找到的是第一个符合条件的数据
print(soup.a)
# 获取标签的属性和属性值
print(soup.a.attrs)

# bs4的一些函数
# （1）find
# 找到的是第一个符合条件的数据
print(soup.find('a'))
# 根据title的值找到对应的标签对象
print(soup.find('a', title='a2'))
# 根据class的值找到对应的标签对象,注意class_ 要加下划线
print(soup.find('a', class_='a1'))

# （2）find_all
# 返回的是一个列表，并且返回的是所有标签
print(soup.find_all('a'))
# 查询多个标签
print(soup.find_all(['a', 'span']))
# limit 查询前几个
print(soup.find_all('li', limit=2))

# （3）select
# 返回的是一个列表，并且返回的是多个数据
# 相当于标签选择器
print(soup.select('a'))
# 可以通过标签选择器查找
print(soup.select('#l1'))
print(soup.select('.a1'))
# 属性选择器
print(soup.select('li[id]'))
# 层级选择器
# 后代选择器
print(soup.select('div li'))
# 子代选择器
print(soup.select('div > ul > li'))

print(soup.select('a,li'))


# 节点信息
# 获取节点内容
obj = soup.select('#d1')[0]
# 获取标签内容，内容中有标签时无法获取
print(obj.string)
# 获取标签内容，
print(obj.get_text())

# 节点的属性
obj = soup.select('#p1')[0]
print(obj)
# name是标签的名字
print(obj.name)
# attrs将属性值作为一个字典返回
print(obj.attrs)
# 获取节点的属性
print(obj.attrs.get('class'))
print(obj.get('class'))
print(obj['class'])