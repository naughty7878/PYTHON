names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)

multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

listdemo = ['Google', 'Runoob', 'Taobao']
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
newdict = {key: len(key) for key in listdemo}
print(newdict)

setnew = {i ** 2 for i in (1, 2, 3)}
print(setnew)

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

a = (x for x in range(1, 10))
print(tuple(a))


new_names2 = [name.upper() for name in names if len(name) > 3]
print(new_names2)
