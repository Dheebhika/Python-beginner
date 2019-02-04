# array_1 = [1,2,3,4]
# array_1 = [1,2,3,"a"]
# print(array_1)


no_of_elements = int(input("Enter number of elements"))
elements_1 = []


def create_list():
    for i in range(0, no_of_elements):
        elements = int(input("Enter the elements"))
        elements_1.append(elements)
    print(elements_1)


def find_even():
    add = 0
    for i in range(0, no_of_elements):
        if elements_1[i] % 2 == 0:
            add = add + elements_1[i]
    print(add)


create_list()
find_even()
