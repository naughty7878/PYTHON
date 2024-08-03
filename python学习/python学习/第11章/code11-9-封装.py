# 封装
class User(object):
    def __init__(self, name, age):
        self._name = name  # 加一个下划线表示受保护的变量
        self.__age = age  # 加二个下划线表示私有的变量

    def show_info(self):
        print('大家好，我是%s，我今年%d' % (self._name, self.__age))

    @property  # 获取变量
    def get_age(self):
        return self.__age

    @get_age.setter  # 变量的修改器
    def set_age(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            raise Exception('年龄只能是整数')

mia = User('mia', 17)
print(mia.__dict__)
print(mia._name)
# print(mia.__age)  # 无法直接访问
# print(mia._User__age)
# mia.name = 'Tom'
# mia.age = 25
# print(mia.name)
# print(mia.age)

# mia.__show_info()
# mia._User__show_info()
print(dir(mia))  # dir()获取所有属性和方法
mia.show_info()
# print(mia.get_age())
# mia.set_age(25)
# print(mia.get_age())

print(mia.get_age)
mia.set_age = 25
print(mia.get_age)