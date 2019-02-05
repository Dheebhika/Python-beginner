# Single Inheritance

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
print()


# Multilevel Inheritance


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
print()


# Multiple Inheritance


class Dog():
    def __init__(self):
        self.str1 = "Dog"
        print("Barks")


class Cat():
    def __init__(self):
        self.str2 = "Cat"
        print("Meow")


class Animal(Dog, Cat):
    def __init__(self):
        Dog.__init__(self)
        Cat.__init__(self)
        print("Animals")

    def print(self):
        print(self.str1, self.str2)


print("Multiple Inheritance")
object = Animal()
object.print()
print()

#Hierarchical Inheritance

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
