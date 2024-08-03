import time

t = time.time()  # 时间戳：1721918790.4672627,  从1970年开始的秒数
print(t)

t = time.localtime()  # 结构化的时间
print(t)
print(t.tm_year, type(t.tm_year))  # 获取
s = time.strftime('%Y-%m-%d %H:%M:%S', t)  #格式化时间
print(s)


from my_package import my_tools
print(my_tools.get_time())