number1 = int(input("Enter the number"))
number2 = int(input("Enter the number"))


def add_numbers():
    if number1 == number2:
        print((number1 + number2) * 2)
    else:
        print(number1 + number2)


add_numbers()