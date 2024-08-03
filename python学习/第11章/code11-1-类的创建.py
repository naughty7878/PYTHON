class Player(object):  # object 基类
    pass


tom = Player()  # 类的实例化（创建对象）
print(type(tom))
print(isinstance(tom, Player)) 
print(isinstance(tom, object))
