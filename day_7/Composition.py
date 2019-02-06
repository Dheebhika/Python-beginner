class House():
    def __init__(self, door_no, address):
        self.door_no = door_no
        self.place = address

    def address(self):
        print("Address: ", self.door_no, ",", self.place)


class Room():
    def __init__(self, books, House):
        self.books = books
        self.house = House

    def address1(self):
        print(self.house.address())


obj1 = House(7, "Kumbakonam")
obj2 = Room("yy", obj1)
obj2.address1()
