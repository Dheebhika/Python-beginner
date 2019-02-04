def remove(duplicate):
    list_ = []
    for num in duplicate:
        if num not in list_:
            list_.append(num)
    return list_


duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(remove(duplicate))
