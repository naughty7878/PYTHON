class Player(object):
    def __init__(self, name, age, city):  # 初始化函数
        print('初始化__init__')
        print(self)
        self.name = name
        self.age = age
        self.city = city


# mia = Player()
# # 实例的属性
# mia.name = 'mia'
# mia.age = 24
# mia.city = '深圳'
# print(mia.name, mia.age, mia.city)
# print(mia)


tom = Player('tom', 25, '上海')
print(tom.name, tom.age, tom.city)
print(tom.__dict__)  # 获取一个实例(对象)的所有属性

# 武器：名字 攻击值 等级
class weapon(object):
    def __init__(self, name, damage, level):
        self.name = name
        self.damage = damage
        self.level = level

gun = weapon('magic', 1000, 5)
print(gun.__dict__)