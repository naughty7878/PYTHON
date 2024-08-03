
# ids = input('请输入你的身份证号：')
# # 位数18位
# # 前17位数字 最后一个数字 + x
# if len(ids) == 18:
#     if ids[:-1].isdigit() and (ids[-1].isdigit() or ids[-1] == 'x'):
#         print('输入正确')
#     else:
#         print('输入错误')
# else:
#     print('输入错误')

import re
# result = re.match('hello', 'hello world')
# print(result)

# 检查字符串是否为纯数字的字符串
result = re.match(r'\d+', '12345')
print(result)


result = re.match(r'\w+', 'adf123')
print(result)


result = re.match(r'\s+', '  123')
print(result)


result = re.match(r'^[abcd]+$', 'abc')
print(result)

result = re.match(r'^ab|cd|ef$', 'bc')
print(result)

from my_package import my_tools
result = my_tools.is_phone_number('1123512345')
print(result)