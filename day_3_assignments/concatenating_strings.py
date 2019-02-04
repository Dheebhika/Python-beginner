def concatenate():
    list1 = ["p", "q"]
    list2 = []
    # for i in list1:
    for n in range(1, 6):
        for i in list1:
            concatenate_ = i + str(n)
            list2.append(concatenate_)

    print(list2)


concatenate()
