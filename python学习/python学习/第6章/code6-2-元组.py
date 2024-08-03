# 元组的创建
tuple1 = (1, 2, 3, True, 'hello')
print(tuple1)
print(type(tuple1))

# 单元素的元组创建
tuple2 = (1,)  # 元组里只有一个元素时，加一个逗号
print(tuple2)
print(type(tuple2))

tuple3 = tuple()  # tuple(): 类型转换
print(tuple3)
print(type(tuple3))

tuple4 = ()
print(tuple4)
print(type(tuple4))

tuple5 = tuple('hello')
print(tuple5)
print(type(tuple5))

tuple6 = tuple([1, 2, 3, 4, 5])
print(tuple6)
print(type(tuple6))

list1 = list(tuple6)
print(list1)
str1 = str(tuple6)
print(str1)
print(type(str1))

print('-' * 30)
print(tuple1)
# 序列的通用操作
print(tuple1[1])
# 切片
print(tuple1[2:4:1])
# len
print(len(tuple1))
print(max(tuple6), min(tuple6))
# del tuple5
# print(tuple5)
# +
print(tuple1 + tuple6)
# *
print(tuple1 * 3)
# in
print(1 in tuple1)

# 元组的常用方法
a = tuple1.count('hello')
print(a)
a = tuple1.index('hello')
print(a)

print('-' * 30)
# 元组的遍历
for i in tuple1:
    print(i)

for index, value in enumerate(tuple1):
    print(index, value)

for i in range(len(tuple1)):
    print(i, tuple1[i])
