user_input = int(input("Enter the height of the pyramid:"))
print("Pyramid:")
for i in range(0,5):
    for j in range(0,i+1):
        print("# ",end="")
    print()
