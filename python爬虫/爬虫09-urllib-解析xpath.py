import urllib.request
from lxml import etree


# xpath的解析
# 解析本地文件
tree = etree.parse('爬虫09-urllib-解析xpath.html')
print(tree)

# 查找-子孙节点查询
# li_list = tree.xpath('//body/ul/li')
# print(li_list)
# print(len(li_list))


# 查找-查询对应属性标签
# /text() 获取节点中的内容
# li_list = tree.xpath('//ul/li[@id]/text()')
# print(li_list)
# print(len(li_list))

# 查找id为l1的标签
# li_list = tree.xpath('//ul/li[@id="l1"]/text()')
# print(li_list)
# print(len(li_list))

# 查询id为l1的标签的class的属性值
# li_list = tree.xpath('//ul/li[@id="l1"]/@class')
# print(li_list)
# print(len(li_list))

# 模糊查询
# li_list = tree.xpath('//ul/li[contains(@id,"l")]/text()')
# print(li_list)
# print(len(li_list))

# li_list = tree.xpath('//ul/li[starts-with(@id,"l")]/text()')
# print(li_list)
# print(len(li_list))

# 逻辑运算
# li_list = tree.xpath('//ul/li[@id="l1" and @class="c1"]/text()')
# print(li_list)
# print(len(li_list))
#
# li_list = tree.xpath('//ul/li[@id="l1" or @id="q1"]/text()')
# print(li_list)
# print(len(li_list))


# 或运算
li_list = tree.xpath('//ul/li[@id="l1"]/text() | //ul/li[@id="q1"]/text()')
print(li_list)
print(len(li_list))