# import my_module  # 全部导入
#
# # 调用模块中的函数
# print(my_module.add(3, 4))
# print(my_module.total(1, 2, 3))
# # 调用模块中的变量
# print(my_module.author)


# from my_module import add, author  # 指定导入
#
# print(add(3, 4))
# print(author)

# from my_module import *  # 所有导入
#
# print(add(3, 4))
# print(total(1, 2, 3))
# print(author)


from my_package.my_math import add as f  # 改名导入
print(f(3, 4))