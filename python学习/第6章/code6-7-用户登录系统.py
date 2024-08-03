# 用户名、密码、黑冥党
# users = ['小红', 'mia', 'jack']
# password = ['123', '456', '789']
# not_allowed = ['jack']
#
# users = [
#     {'name': '小红', 'password': '123', 'status': True},
#     {'name': 'mia', 'password': '456', 'status': True},
#     {'name': 'jack', 'password': '789', 'status': False}
# ]
# print(users)
# flag = False
# for t in range(3):
#     user = input('请输入你的用户名：')
#     pwd = input('请输入你的密码：')
#     for i in users:
#         if user == i['name']:
#             if pwd == i['password']:
#                 if i['status'] == True:
#                     print('登录成功！')
#                 else:
#                     print('账号失效，请联系管理员！')
#                 flag = True
#                 break
#             else:
#                 print('密码输入错误，请重试！')
#     else:
#         print('用户不存在，请先注册！')
#     if flag:
#         break


users = {
    '小红': {'name': '小红', 'password': '123', 'status': True},
    'mia': {'name': 'mia', 'password': '456', 'status': True},
    'jack': {'name': 'jack', 'password': '789', 'status': False}
}
print(users)
flag = False
for t in range(3):
    user = input('请输入你的用户名：')
    pwd = input('请输入你的密码：')
    if user in users and pwd == users[user]['password']:
        print('登录成功！')
        break
    elif user in users and not users[user]['status']:
        print('账号失效，请联系管理员！')
        break
    elif user in users and pwd != users[user]['password']:
        print('密码输入错误，请重试！')
    else:
        print('用户不存在，请先注册！')

