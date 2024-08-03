# 字典的创建
d = {
    'name': 'mia',  # 键值对
    'gender': False,
    'name': 'jack',  # 键重复的话，会覆盖前面的值
}
print(d)
print(type(d))

d = {}
print(d)
print(type(d))

d = dict()
print(d)
print(type(d))

d = dict(a=1, b=2)
print(d)
print(type(d))

d = dict([('a', 1), ('b', 2)])
print(d)
print(type(d))

d = dict({'a': 1, 'b': 2})
print(d)
print(type(d))

d = {}
# 新增键值对
d['heigh'] = 170
print(d)
# 获取键值对
print(d['heigh'])
# 修改键值对
d['heigh'] = 180
print(d)
# del d
# print(d)
del d['heigh']
print(d)
# in
d['heigh'] = 170
print('name' in d)
print('heigh' in d)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
d = {
    'name': 'mia',  # 键值对
    'gender': False,
}
# 字典的遍历
for i in d:
    print(i, d[i])

print(d.items())
for k, v in d.items():
    print(k, v)

for k in d.keys():
    print(k)
for v in d.values():
    print(v)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# 字典的常用方法
d = {
    'name': 'mia',  # 键值对
    'gender': False,
}
d.pop('name')
print(d)
a = d.copy()
print('a =', a)
print(d.get('gender'))

d.update({'age': 18})
print('d.update({\'age\': 18}) =', d)

d = {
    'name': 'mia',  # 键值对
    'gender': False,
}
d.popitem()
print('d.popitem() =', d)
d.clear()
print(d)
