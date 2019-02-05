class Animal():
    def __init__(self, name):
        self.name = name

    def eat(self):
        return self.eat


class Dog(Animal):
    def __init__(self, sound):
        self.sound = sound

    def bark(self):
        return self.bark


class BabyDog(Dog):
    def __init__(self, cry):
        self.cry = cry

    def weep(self):
        return self.weep


print("Multilevel Inheritance")
object1 = BabyDog("BabyDog weeps")
object2 = Dog("Dog barks")
object3 = Animal("Animal eats")
print(object1.weep())
print(object2.bark())
print(object3.eat())

