class Animal(object):

    def speak(self):
        print('动物的叫声')
        pass


class Cat(Animal):

    def speak(self):
        print('喵喵')


class Dog(Animal):

    def speak(self):
        print('汪汪')


class Test(object):
    def speak(self):
        print("TEST")


def speak(object):  # animal
    object.speak()


kitty = Cat()
puppy = Dog()
# kitty.speak()
# puppy.speak()

animal = Animal()
animal.speak()

speak(animal)
speak(kitty)
speak(puppy)

test = Test()
speak(test)
