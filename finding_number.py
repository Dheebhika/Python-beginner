b = 45
while True:
    a = int(input("enter the number less than 60"))
    if a == b:
        print("matched")
        break
    elif a > b:
        print("enter smaller value")
    else:
        print("enter larger value")
