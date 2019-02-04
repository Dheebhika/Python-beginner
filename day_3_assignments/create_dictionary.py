def dictionary():
    create_dictionary = dict()
    for values in range(1, 16):
        create_dictionary[values] = values ** 2
    print(create_dictionary)


dictionary()

'''
def dictionary():
    num = int(input("Enter the number"))
    for i in range(0, num + 1):
        num = int(input("Enter the number"))
        dictionary = {i: i * i}
        print(dictionary)


dictionary()


'''
