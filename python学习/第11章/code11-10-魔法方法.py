class User(object):
    # 构造函数
    def __init__(self, name):
        print('__init__被调用')
        self.name = name

    def __str__(self):
        return '我的名字是%s' % self.name

    def __add__(self, other):
        return self.name + other.name

    def __eq__(self, other):
        return  self.name == other.name


mia = User('mia')
print(mia.__dict__)

print(str(mia))
print(mia)

jack = User('jack')
print(mia + jack)

print(mia == jack)

