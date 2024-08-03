import turtle,time
from my_package import my_tools

pen = turtle.Turtle()
# pen.forward(100)
# pen.speed(0)  # 设置速度
# for i in range(100):
#     pen.forward(200)  # 画的长度
#     pen.right(71)  # 旋转角度
pen.backward(200)
while True:
    time.sleep(1)
    times = my_tools.get_time()
    pen.clear()  # 清空画布
    pen.write(times, font=('Arial', 40, 'normal'))

input()
