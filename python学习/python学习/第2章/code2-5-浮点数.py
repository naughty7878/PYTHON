# 浮点数的计算
# n1 = 0.1234
# n2 = 0.2
# print(n1 + n2)

n1 = 0.1
n2 = 0.2
print(n1 + n2)

# 四舍五入round
n3 = round(n1 + n2, 2)
print(n3)

import math

# 向上取整
n4 = math.ceil(n1 + n2)
print("向上取整的结果是：", n4)
# 向下取整
n5 = math.floor(n1 + n2)
print("向下取整的结果是：", n5)
