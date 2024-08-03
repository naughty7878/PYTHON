print(range(10))
print(list(range(10)))  # end
print(list(range(2, 10)))  # start, end
print(list(range(2, 10, 3)))  # start, end, step

for i in range(3):
    print(i)


# 高斯求和
total = 0
for i in range(1000, 10001):
    total += 1
print('total =', total)

# 水仙花数：三位数，每一位数字的立方和 = 三位数本身
for i in range(100, 1000):
    # a = i % 10
    # b = i // 10 % 10
    # c = i // 100
    t = str(i)
    a = int(t[2])
    b = int(t[1])
    c = int(t[0])
    if a ** 3 + b ** 3 + c ** 3 == i:
        print(i)