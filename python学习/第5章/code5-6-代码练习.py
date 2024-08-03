# 打印 m 行 n 列 的图形

# m = 4
# n = 5
# for i in range(m):
#     for j in range(n):
#         print('*', end='')
#     print()


# # 打印n行等腰三角形
# n = 4
# a = 1
# b = n - 1
# for i in range(n):
#     print(' ' * b + '*' * a)
#     a += 2
#     b -= 1

# 穷举
peach = 1
while True:
    d1 = peach // 2 - 1
    d2 = d1 // 2 - 1
    d3 = d2 // 2 - 1
    if d3 == 1:
        print(peach)
        break
    peach += 1