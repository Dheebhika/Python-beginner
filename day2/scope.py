def add_numbers_without_parameters():
    number1 = int(input("Enter the number"))
    number2 = int(input("Enter the number"))
    if (number1 == number2):
        print((number1 + number2) * 2)
    else:
        print(number1 + number2)


def add_numbers_with_parameters(number1=4, number2=5):
    if (number1 == number2):
        print((number1 + number2) * 2)
    else:
        print(number1 + number2)


user_input = input("Do you want to enter value")

if (user_input == "yes"):
    add_numbers_without_parameters()
else:
    add_numbers_with_parameters()
