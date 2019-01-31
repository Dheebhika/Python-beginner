#count = 0
#count += 1


def fizz_buzz():
    for values in range(0, 51):

        if values % 3 == 0 and values % 5 == 0:
            print("fizzbuzz")

        elif values % 3 == 0:
            print("fizz")

        elif values % 5 == 0:
            print("buzz")

        else:
            print(values)


#count += 1
#print(count)

fizz_buzz()
