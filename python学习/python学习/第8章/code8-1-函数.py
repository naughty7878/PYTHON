# 先定义后使用
# f()

# 函数定义
def f():
    print('python')


# 函数调用
f()


def sum_2(a, b):  # 形参
    return a + b


result = sum_2(2, 3)  # 实参
print(result)


def power(x, n=2):  # n:默认参数，缺省参数
    return x ** n


a = power(4, 3)
print(a)
b = power(5, 3)
print(b)
c = power(6)
print(c)


def infos(name, age=24, gender='女'):
    return '大家好，我是%s，我今年%d岁，我是一名%s生' % (name, age, gender)


print(infos('mia', 24, '女'))
print(infos('lily', 25))
print(infos('jack', gender='男'))


# 可变参数
def total(*args):
    # args = (1,3,4,5,6,7,2)
    print(args)  # a是一个元组
    result = 0
    for i in args:
        result += i
    return result


print(total(1, 3, 4, 5, 6, 7, 2))
a = [1, 3, 4]
print(total(*a))


def f(**kwargs):  # 可变参数，接收字典
    for k, v in kwargs.items():
        print(k, v)


d = {'x1': 1, 'x2': 2}
f(**d)


