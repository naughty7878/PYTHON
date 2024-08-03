# 列表的创建

list1 = []  # 空列表
print(list1)
print(type(list1))

list2 = [1, 2, 3, True, False]
print(list2)

list3 = list()  # 类型转换：把参数转换位列表
print(list3)

list3 = list('123456')
print(list3)

# 列表的索引
print(list3[3])
print(list3[-1])

# 列表的切片
print(list3[2:4:1])

# 列表的加法和乘法
print(list2 + list3)
print(list2 * 2)

# 列表的成员运算
print('0' in list3)
print('0' not in list3)

# 列表的函数
print(len(list3))
print(max(list3))
print(min(list3))

# del list3 # 删除变量
# print(list3)

# 列表的遍历
for i in list3:
    print(i)

for i,j in enumerate(list2):  # 枚举
    print(i, j)

for i in range(6):
    print('list3[%d]' % i, list3[i])


# 列表的常用方法
# 添加元素
list3.append('666')
print(list3)
# 添加列表
list3.extend([1, 2, 3])
print(list3)
# 插入元素
list3.insert(1, 'hello')
print(list3)
# 根据索引删除元素
list3.pop(3)
print(list3)
# 根据元素删除
list3.remove(2)
print(list3)
list3.append(1)
print(list3)
list3.remove(1)
print(list3)
# 清空列表
list3.clear()
print(list3)

# 计算若干个人的平均年龄
age = [10, 20, 30, 40, 23, 45]
# for i in age:
#     print(i)
print(sum(age) / len(age))
