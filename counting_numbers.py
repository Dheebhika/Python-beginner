zero_count, positive_count, negative_count = 0, 0, 0
list1 = [-1, 0, 0, 1, 100]
print("Input: ", list)
print("Output:")
for num in list1:
    if num == 0:
        zero_count += 1
    elif num >= 0:
        positive_count += 1
    else:
        negative_count += 1
print("zero_count:", zero_count)
print("positive_count:", positive_count)
print("negative_count:", negative_count)
