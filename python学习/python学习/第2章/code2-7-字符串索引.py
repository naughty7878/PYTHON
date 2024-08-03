s = "hello,world"
print(s[0])
print(s[4])
print(s[-1])
print(s[0:2]) # 包头不包尾
# 切片 变量名[起始索引:结束索引+1:步数]
# 步数默认为1
# 起始索引默认为0,可以省略
# 而结束索引默认为-1,可以省略
print(s[1:3])
print(s[1:6:2])
print(s[::2])
print(len(s))

# 字符串反转
s2 = "123456789"
print(s2[-1:-10:-1])
print(s2[::-1])