# 任务1： 打印数字2024
print(2024)

# 任务2：打印字符串 我是mia
print("我是mia")

# 任务3： 创建变量year，值为2024，打印变量year
year = 2024
print(year)
print(year, "年，我要加油")
print(year, "年，我要加油", sep="")
print(year, "年，我要加油", sep="--")
print(year, "年，我要加油", end="xx")
print("END")
str = """ 
    sfsdfddsfdsfs
    sfsdfdsfs
    ssss
    deeeeeee
"""
print(str)

month = 2
day = 20
week = "一"
weather = "晴"
temp = 19.5
# 格式化输出
print("今天是%d年%02d月%d日, 星期%s, 天气%s, 温度%.2f" % (year, month, day, week, weather, temp))
