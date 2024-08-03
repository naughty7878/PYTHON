while True:
    try:
        op = input('请输入一个四则运算算式（例如1+2）：')
        if '+' in op:
            a = op.split('+')
            result = int(a[0]) + int(a[1])
            print('结果是：%d' % result)
        elif '-' in op:
            a = op.split('-')
            result = int(a[0]) - int(a[1])
            print('结果是：%d' % result)
        elif '*' in op:
            a = op.split('*')
            result = int(a[0]) * int(a[1])
            print('结果是：%d' % result)
        elif '/' in op:
            a = op.split('/')
            result = int(a[0]) / int(a[1])
            print('结果是：%d' % result)
        elif op == 'C':
            print('感谢您使用本计算器！')
            break
        else:
            raise Exception('请输入1+2这个格式输入算式！')
    except ZeroDivisionError as e:
        print('异常原始信息', type(e), e)
        print('注意除法运算，除数不能为0')
    except Exception as e:
        print('异常原始信息', type(e), e)