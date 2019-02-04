user_input = input("Input: ")
a = len(user_input)
print("Output: ")
for i in range(0, a-1):
    user_input = user_input[1:] + user_input[0]
    print(user_input)


