# 10阶楼梯，每次上1个台阶或者上2个台阶，一共有多少种走法


# 计算出n阶楼梯，一共有多少种走法
def f(n):
    if n == 1:  # 1阶楼梯，1种走法
        return 1
    elif n == 2:  # 2阶楼梯，2钟走法
        return 2
    return f(n - 1) + f(n - 2)


for i in range(1, 11):
    print('楼梯有%d阶的时候，f(%d) = %d' % (i, i, f(i)))

a = [0, 1, 2]
for i in range(3, 11):
    a.append(a[i - 1] + a[i - 2])
    print('楼梯有%d阶的时候，有%d种走法' % (i, a[-1]))
