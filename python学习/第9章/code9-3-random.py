import random

# 随机数
print(random.random())  # random.random() 方法返回值的范围是[0.0, 1.0)
# 随机整数(包含1与100)
print(random.randint(1, 100))

# for i in range(1000):
#     if random.randint(1, 10) == 1:
#         print(1)
#     elif random.randint(1, 10) == 10:
#         print(10)
print(random.choice('abcdefg'))
print(random.choice([1, 2, 3, 4, 5, 6, 7]))

# 生成一个随机字母组成的列表
# a = []
# n = 5
# for i in range(20):
#     s = ''
#     for j in range(n):
#         t = random.randint(65, 90)
#         s += chr(t)
#     a.append(s)
# print(a)
from my_package import my_tools, my_games

print(my_tools.random_string(5))

list1 = [1, 2, 3, 4, 5, 6, 7]
# 随机打乱列表元素
random.shuffle(list1)
print(list1)

# my_games.game1()
my_games.guess_number(1, 1000)