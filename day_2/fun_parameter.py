def add_number(number1, number2):
    print(number1 + number2)
    return (number1 + number2) * 2


print(add_number(10, 10))
print(print("hi"))
# print(input("Enter the number"))
print('a', 'b')
print(1, "a,b")
print(type(1))
print(type(0.1))
print(type('a'))
print(type("hai"))
print(type("a,b"))
print(type(print()))
print(type(print("hi")))


def with_default_parameters(number1=5, number2=3):
    return number1 + number2


print(with_default_parameters(1, 2))
print(with_default_parameters(1))
print(with_default_parameters())
