dict = {1: 0, 2: [1, 2, 3], 3: "a"}
print(dict.values())

count = 0
for values in dict.values():
    if type(values) == list:
        count += 1
print(count)
