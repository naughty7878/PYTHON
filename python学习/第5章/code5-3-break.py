# while True:
#     print(111)
#     break
#     print(222)
#
#


# while True:
#     print(111)
#     name = input('请输入你的名字：')
#     if name == 'mia':
#         print('mia欢迎回家')
#         break
#     else:
#         print('mia不在家，一会再来吧')
#

# for i in range(10):
#     if i > 0 and i % 3 == 0:
#         print(i)
#         break

# 判断一个数字n是否是质数
# n = 7
# a = 2
# while a < n:
#     if n % a == 0:
#         print(n, '不是质数')
#         break
#     a += 1
# else:
#     print(n, '是质数')
#
# if a == n:
#     print(n, '是质数')

n = 8
for i in range(2, n):
    if n % i == 0:
        print(n, '不是质数')
        break
else:
    print(n, '是质数')
