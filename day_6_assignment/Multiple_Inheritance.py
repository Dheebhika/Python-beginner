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
