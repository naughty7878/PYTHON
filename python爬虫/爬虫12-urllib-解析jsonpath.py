import jsonpath
import json

# 案例教程：https://blog.csdn.net/luxideyao/article/details/77802389

obj = json.load(open('爬虫12-urllib-解析jsonpath.json', 'r', encoding='utf-8'))

# 书的作者
author_list = jsonpath.jsonpath(obj, '$.store.book[*].author')
print(author_list)
# 第二本书作者
author_list = jsonpath.jsonpath(obj, '$.store.book[1].author')
print(author_list)
# 所有作者
author_list = jsonpath.jsonpath(obj, '$..author')
print(author_list)

# store下面所有的元素
tag_list = jsonpath.jsonpath(obj, '$.store.*')
print(tag_list)

# store下面所有东西的price
price_list = jsonpath.jsonpath(obj, '$.store..price')
print(price_list)

# 最后一本书
book = jsonpath.jsonpath(obj, '$..book[(@.length-1)]')
print('book', book)

# 前面的两本书
book_list = jsonpath.jsonpath(obj, '$..book[0:2]')
print('book_list', book_list)

# list = [1, 2, 3, 4, 5]
# print(list[0:2])

# 过滤所有包含isbn的书
book_list = jsonpath.jsonpath(obj, '$..book[?(@.isbn)]')
print('book_list', book_list)

# 过滤超过10元的书
book_list = jsonpath.jsonpath(obj, '$..book[?(@.price>10)]')
print('book_list', book_list)
