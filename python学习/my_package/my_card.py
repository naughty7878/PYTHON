def menu():
    print('*' * 30)
    print('''欢迎使用【名片管理系统】
    1.新建名片
    2.显示全部
    3.查询名片
    0.退出系统''')
    print('*' * 30)


def new_card(name, phone, qq, email):
    user = {
        'name': name,
        'phone': phone,
        'qq': qq,
        'email': email
    }
    cards.append(user)
    return True


def show_card():
    for card in cards:
        print(card)


def query_card(kw):
    for card in cards:
        for k, v in card.items():
            if kw == v:
                return card
    return False


def quit():
    print('欢迎下次使用【名片管理系统】')


def modify_card(card, name, phone, qq, email):
    card['name'] = name
    card['phone'] = phone
    card['qq'] = qq
    card['email'] = email
    return True


def del_card(card):
    if card in cards:
        cards.remove(card)
        return True
    return False


cards = [{'name': 'jack', 'phone': '1', 'qq': '1', 'email': '1111'},
         {'name': 'mia', 'phone': '2', 'qq': '2', 'email': '2222'},
         {'name': 'tom', 'phone': '3', 'qq': '3', 'email': '3333'}]


def main():
    menu()
    while True:
        op = input('请输入你要操作的序号：')
        if op == '1':
            name = input('请输入你的姓名：')
            phone = input('请输入你的电话：')
            qq = input('请输入你的QQ号：')
            email = input('请输入你的电子邮箱：')
            result = new_card(name, phone, qq, email)
            if result:
                print('成功新建名片')
            else:
                print('请重试')
        elif op == '2':
            show_card()
        elif op == '3':
            kw = input('请输入查询的关键字：')
            result = query_card(kw)
            if result:
                print(result)
                op2 = input('输入4修改名片，输入5删除名片：')
                if op2 == '4':
                    name = input('请输入你的姓名：')
                    phone = input('请输入你的电话：')
                    qq = input('请输入你的QQ号：')
                    email = input('请输入你的电子邮箱：')
                    result2 = modify_card(result, name, phone, qq, email)
                    if result2:
                        print('成功修改名片')
                    else:
                        print('请重试')
                elif op2 == '5':
                    result2 = del_card(result)
                    if result2:
                        print('成功删除名片')
                    else:
                        print('请重试')
            else:
                print('没有查到相关信息')
        elif op == '0':
            quit()
            break
        else:
            print('请重试')
