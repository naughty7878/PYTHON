# 纸的厚度
n = 0.1
w = n
for i in range(1, 51):
    w *= 2
    print(w)

# 国王麦粒
g = 1 # 当前格子应该放的麦粒数
total = 0  # 总麦粒树
a = 1  # 棋盘格子数量
while a <= 100:
    print('格子数：', a, '麦粒数：', g)
    total += g
    a += 1 # 下一格子
    g *= 2 # 下个格子应该放的麦粒数
print('总麦粒', total)