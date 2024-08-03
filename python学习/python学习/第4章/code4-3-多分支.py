score = 73
# if score > 90:
#     print('A')
# elif score > 80:
#     print('B')
# elif score > 70:
#     print('C')
# else:
#     print('D')

# if score > 90:
#     print('A')
# else:
#     if score > 80:
#         print('B')
#     else:
#         if score > 70:
#             print('C')
#         else:
#             print('D')

# bmi计算
# bmi = w/(h*h)
w = float(input(' 请输入你的体重，单位kg：'))
h = float(input(' 请输入你的身高，单位米：'))
bmi = w / (h * h)
print(bmi)

if bmi < 18.5:
    print('过廋')
elif bmi < 23.9:
    print('正常')
else:
    print('过胖')
    