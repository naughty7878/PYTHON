def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1


# 使用生成器
for num in count_up_to(5):
    print(num)


# 输出: 1 2 3 4 5

############################################################
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


gen = infinite_sequence()
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2

############################################################
# 生成器表达式
squares_gen = (x**2 for x in range(1000000))

# 相比之下，列表会占用大量内存
# squares_list = [x**2 for x in range(1000000)]



############################################################
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for f in fibonacci():
    if f > 100:
        break
    print(f, end=' ')
# 输出: 0 1 1 2 3 5 8 13 21 34 55 89
print()


############################################################
def stateful_generator():
    yield "First"
    yield "Second"
    yield "Third"

gen = stateful_generator()
print(next(gen))  # First
print(next(gen))  # Second
print(next(gen))  # Third