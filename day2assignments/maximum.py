number = int(input("Enter a number:"))
array=[]
def maximum():
    for i in range(0,number):
        enter_numbers = int(input("Enter the numbers:"))

        array.append(enter_numbers)
        array.sort()
    return array[number-1]
print("The largest number is",maximum())

