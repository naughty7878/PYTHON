try:
    print('有可能出现异常的代码')
    n = int(input('请输入一个数字：'))
    print(5 / n)
except ZeroDivisionError as e:
    # print('如果出现了异常，进入该代码块执行')
    print('除数不能为0')
    print('原始异常信息', type(e), e)
except Exception as e:
    print('请输入一个数字')
    print('原始异常信息', type(e), e)
except:
    print('其他异常')
else:
    print('运行没有被except语句捕获，执行else模块')
finally:
    print('无论如何，都要执行finally模块')