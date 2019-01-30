def immutable_test(my_string):
    print(hex(id(my_string)))
    my_string=my_string.replace("st","ST")
    print(hex(id(my_string)))
    print()


def mutable_test1(number):
    print(hex(id(number)))
    number+=1
    print(hex(id(number)))
    print()


def mutable_test2(my_list):
    print(hex(id(my_list)))
    my_list=my_list.sort()
    print(hex(id(my_list)))
    print()


immutable_test("string")
mutable_test1(4)
mutable_test2((1,2,3,4))