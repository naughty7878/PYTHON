# 转int
s = "2024"
print(s)
n = int(s)
print(n)
print(type(s), type(n))

# s1 = "aa123"
# print(int(s1))
# s1 = "123.4"
# print(int(s1))
f1 = 123.4
print(int(f1))

b1, b2 = True, False
print(int(b1))
print(int(b2))
# 进制的转换
print("int(\"10\")", int("10"))
print("int(\"10\", 2)", int("10", 2))
print("int(\"a\", 16)", int("a", 16))



# 转float
print(float("2024.1"))
print(float(123))
print(float(True))
print(float(False))

# 转bool
print(bool("abc"))
print(bool(""))
print(bool("0"))
print(bool(1.0))
print(bool(0.0))
print(bool(1))
print(bool(0))

# 转str
print(type(str(5)))
print(type(str(5.5)))
print(str(True))
print(type(str(True)))
