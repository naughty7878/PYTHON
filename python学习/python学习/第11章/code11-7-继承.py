class Player(object):
    numbers = 0  # 类属性
    levels = ['青铜', '白银', '黄金', '钻石', '王者']

    def __init__(self, name, age, city, level):  # 初始化函数
        print('初始化__init__')
        print(self)
        self.name = name  # 实例属性
        self.age = age
        self.city = city

        # 使用类属性
        Player.numbers += 1

        if level not in Player.levels:
            raise Exception('段位设置错误！')
        else:
            self.level = level

    def show(self):  # 实例的方法
        print("我是荣耀王者的第%d玩家，我的名字是%s，我来自%s，我的段位是%s" % (
            Player.numbers, self.name, self.city, self.level))

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


class VIP(Player):  # 子类

    # 构造函数重写
    def __init__(self, name, age, city, level, coin):
        print('VIP初始化__init__')
        print(self)
        super().__init__(name, age, city, level)

        self.coin = coin
        # self.name = name  # 实例属性
        # self.age = age
        # self.city = city
        #
        # # 使用类属性
        # Player.numbers += 1
        #
        # if level not in Player.levels:
        #     raise Exception('段位设置错误！')
        # else:
        #     self.level = level

    def show(self):  # 实例的方法
        print("我是荣耀王者的第%d玩家，我的名字是%s，我来自%s，我的段位是%s， 我的余额%s" % (
        Player.numbers, self.name, self.city, self.level, self.coin))


mia = VIP('mia', 18, '深圳', '青铜', 1000)
print(type(mia))
print(isinstance(mia, Player))
print(isinstance(mia, VIP))

print(mia.coin)
mia.show()
mia.level_up()
mia.show()
