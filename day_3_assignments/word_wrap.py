def word_wrap():
    user_input = input("Input: ")
    print("Output: ")
    for i in range(0, len(user_input)):
        output = user_input[1:] + user_input[0]
        print(output)


word_wrap()
