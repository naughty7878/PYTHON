# 全局变量
num1 = 10  # 不可变数据类型
list1 = [1, 2, 3, 4, 5]  # 可变的数据类型

def f(): 
    num2 = 20  # 局部变量
    # num1 = 30  # 声明一个num1，未修改全局变量num1

    global num1  # 声明在f中使用num1全局变量
    num1 = 50

    print('在函数中打印num1的值', num1)
    print('在函数中打印num2的值', num2)

    list1[2] = 8
    print('在函数中打印list1的值', list1)


f()
print('在函数外打印num1的值', num1)
# print('在函数外打印num2的值', num2)
print('在函数外打印list1的值', list1)

