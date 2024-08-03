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

    def show(self):  # 实  例的方法
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


class weapon(object):
    # 类属性
    numbers = 0
    max_damage = 10000
    levels = ['青铜', '白银', '黄金', '钻石', '王者']
    all_weapon = []

    # 构造方法
    def __init__(self, name, damage, level):
        self.name = name
        self.damage = damage
        self.level = level
        weapon.numbers += 1
        if damage > weapon.max_damage:
            raise Exception('最大的伤害值是10000，请重试')
        if level not in weapon.levels:
            raise Exception('段位设置错误！')
        weapon.all_weapon.append(self)

    def show_weapon(self):
        for k, v in self.__dict__.items():
            print(k, v)

    @classmethod
    def get_max_damage(cls):
        max_damage = 0
        for w in cls.all_weapon:
            if w.damage > max_damage:
                max_damage = w.damage
        return max_damage


infos = {'name': 'mia', 'age': 13, 'city': '北京', 'level': '青铜'}
if Player.isvalid(**infos):
    mia = Player('mia', 22, '深圳', '青铜')
    mia.show()
else:
    print('请检查')
