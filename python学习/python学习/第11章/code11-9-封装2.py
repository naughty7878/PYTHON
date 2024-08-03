class Player(object):
    numbers = 0  # 类属性
    levels = ['青铜', '白银', '黄金', '钻石', '王者']

    def __init__(self, name, age, city, level):  # 初始化函数
        print('初始化__init__')
        print(self)
        self.__name = name  # 实例属性
        self.__age = age
        self.__city = city

        # 使用类属性
        Player.numbers += 1

        if level not in Player.levels:
            raise Exception('段位设置错误！')
        else:
            self.level = level

    def show(self):  # 实例的方法
        print("我是荣耀王者的第%d玩家，我的名字是%s，我来自%s，我的段位是%s" % (
            Player.numbers, self.__name, self.__city, self.level))

    def level_up(self):
        index = Player.levels.index(self.level)
        if index < len(Player.levels) - 1:
            self.level = Player.levels[index + 1]

    def get_weapon(self, weapen):
        self.weapon = weapen

    def show_weapon(self):
        self.weapon.show_weapon()

    # 类方法
    @classmethod
    def get_players(cls):
        print('荣耀王者的用户数量达到了%d人' % cls.numbers)

    # 静态方法
    @staticmethod
    def isvalid(**kwargs):
        if kwargs['age'] > 18:
            return True
        else:
            return False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if self.__name == name:
            raise Exception('修改名字不能与原名字相同')
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise Exception('年龄必须为整数')
        elif age < 0 or age > 150:
            raise Exception('年龄必须大于等于0且小于等于150')
        self.__age = age

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        if len(city) > 10 or len(city) < 2:
            raise Exception('城市名称有误')
        self.__city = city


mia = Player('mia', 18, '深圳', '青铜')
mia.show()
mia.name = 'miaa'
print(mia.name)
mia.age = 34
print(mia.age)
mia.city = '杭州'
print(mia.city)
mia.show()
print(mia.__dict__)