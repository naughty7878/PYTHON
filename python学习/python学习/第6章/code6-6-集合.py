# 集合的创建
s = set()
print(s, type(s))
s = {1, 2, 3, 4, 1, 2}
print(s, type(s))
s = set([30, 40, 50])  # list -> set
print(s, type(s))
s = set((1, 2, 3))  # tuple -> set
print(s, type(s))
s = set('123')  # str -> set
print(s, type(s))
s = set({'a': 1, 'b': 2})  # dist -> set
print(s, type(s))

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# 集合运算
s = {1, 2, 3, 4, 1, 2}
print(1 in s)
print(len(s))
print(max(s), min(s))

# 集合的遍历
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
s = {1, 2, 3, 4, 1, 2}
for i in s:
    print(i, end=' ')
print()

# 集合的方法
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
s = {1, 2, 3, 4, 1, 2}
s.remove(4)
print(s)
s.update({5, 6, 7})
print(s)
s.add(0)
print(s)

# 交集 并集
s2 = {6, 7, 8, 9}
print(s & s2)
print(s | s2)
d = {}
a = s | s2
for i in a:
    total = 0
    total += 1 if i in s else 0
    total += 1 if i in s2 else 0
    print('数字%d有%d个' % (i, total))
    d['数字' + str(i)] = total
print()
print(d)
