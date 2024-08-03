#  题目要求：输入2024-02-25，输入这一天是这一年的多少天
date = input('请输入日期：').split('-')
print(date)
year = int(date[0])
month = int(date[1])
day = int(date[2])

# 一个月有多少天列表
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if not year % 4 and year % 100 or not year % 400:
    days[2] += 1
    print('是闰年')
else:
    print('不是闰年')
print('%d年有%d天' % (year, sum(days)))

# 遍历计算
result = 0
for i in range(month):
    result += days[i]
result += day
print('输入日期是%d年的第%d天' % (year, result))

