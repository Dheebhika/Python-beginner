number = int(input("Enter the number: "))


def upper_triangle():
    for i in range(0, number):
        for j in range(0, i + 1):
            print("*", end=" ")
        print()


def lower_triangle():
    for i in range(number, 1, -1):
        for j in range(0, i - 1):
            print("*", end=" ")
        print()


upper_triangle()
lower_triangle()
