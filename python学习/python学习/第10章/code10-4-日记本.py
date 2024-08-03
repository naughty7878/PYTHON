def write_txt():
    date = input('请输入今天的日期：')
    text = input('请输入日记内容：')
    filename = '日记本.txt'
    f = open(filename, mode='a', encoding='utf-8')
    f.write(date + '\n')
    f.write(text + '\n')
    f.close()
    return True


def read_txt(day=-1):
    filename = '日记本.txt'
    f = open(filename, mode='r', encoding='utf-8')
    context = f.readlines()
    f.close()
    if day != '-1':
        arr = []
        c = False
        for i in context:
            if c:
                if i.startswith('20'):
                    break
                arr.append(i)
                continue
            if i.strip() == day:
                arr.append(i)
                c = True
        if len(arr) == 0:
            return False
        else:
            for i in arr:
                print(i, end='')
    else:
        for i in context:
            print(i, end='')
    return True


def quit():
    print('欢迎下次使用！再见！')


def menu():
    print('*' * 30)
    print('''欢迎使用python笔记本系统
    1：记日记
    2：阅读日记
    3：退出系统''')
    print('*' * 30)


menu()
while True:
    op = input('请输入你的选择：')
    if op == '1':
        if write_txt():
            print('日记保存成功！')
    elif op == '2':
        day = input('请输入你查询的日期（查询全部请输入-1）：')
        if read_txt(day):
            print('日记已加载完毕！')
        else:
            print('日记未找到')
    elif op == '3':
        quit()
        break
    else:
        print('请重新选择')
