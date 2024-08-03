import  os

# 获取当前目录路径
path = os.getcwd()
print(path)
# 打开文件
# 相对路径
# f = open('test.txt', encoding='utf-8')
# 绝对路径
# f = open('E:\\workspace-pycharm\\python学习\\python学习\\第10章\\test.txt', encoding='utf-8')
f = open(path + '\\test.txt', mode='r', encoding='utf-8')

# 读取文件
# context = f.read()
# print(context)

# while True:
#     context = f.readline()
#     if context:
#         print(context, end='')
#     else:
#         print('\n' + '~' * 10)
#         print(context)  # 最后返回的是一个 ‘’ 空字符串
#         print('~' * 10)
#         break

context = f.readlines()   # 返回一个数组，成员是每一行的内容
print(context)

# 关闭文件
f.close()

