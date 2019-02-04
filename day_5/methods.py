class Person:
    def my_details(self, name, age):
        print("hi")
        print("My details:", name, age)

    def __init__ (self,name,age):
        self.name=name
        self.age=age


p = Person()
p.my_details("Dheebhika", 21)
