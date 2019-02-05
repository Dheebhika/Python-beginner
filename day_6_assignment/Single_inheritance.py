class Animal():
    def __init__(self, name):
        self.name = name

    def eat(self):
        return self.name


class Dog(Animal):
    def __init__(self, sound):
        self.sound = sound

    def bark(self):
        return self.sound


print("Single Inheritance")
object = Animal("Animal eats")
print(object.eat())
object = Dog("Dog Barks")
print(object.bark())





