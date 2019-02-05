class Animal():
    def __init__(self, name):
        self.name = name

    def eat(self):
        return self.name

class Dog (Animal):

    def __init__(self, sound):
        self.sound = sound

    def bark(self):
        return self.sound
class Cat (Animal):
    def __init__(self, sound):
        self.sound = sound

    def meow(self):
        return self.sound
object=Animal()

print("Hierarchial inheritance")
print(object.meow())
print(object.eat())