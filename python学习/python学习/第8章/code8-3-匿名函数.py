def f(a, b):
    return a + b


result = f(1, 2)
print(result)
fun = lambda a, b: a + b
result = fun(2, 3)
print(result)

print('~' * 10)

a = [1, 2, 3]


# for i in range(len(a)):
#     a[i] = a[i] ** 2
# print(a)

# map() 函数 映射函数
def f1(x):
    return x ** 2


result = map(f1, a)
print(result, type(result))
print(list(result))

print(list(map(lambda x: x ** 3, a)))

# reduce 累积
from functools import reduce

f2 = lambda x, y: x * y

print('reduce', reduce(f2, a))

# filter 过滤
print(list(filter(lambda x: x % 2 == 0, a)))

a = [1, 2, 3, 4, 5, 0, 32, 42, 43]
# 过滤非0
print(list(filter(lambda x: x != 0, a)))
# 累积大整数
print(reduce(lambda x, y: int(str(x) + str(y)), a))
