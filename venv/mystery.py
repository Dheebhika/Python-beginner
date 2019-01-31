def mystery(number):
    sum = 1
    for i in range(1, number):
        if i < 6:                                   # number=1 to 5:sum=2^(num^2)
            for k in range(1, number):
                sum *= 2
        else:
            if i < 10:                              # number=6:sum=2^(5*num)*5
                sum *= 5                            # number=7:sum=2^(5*num^)*(5^2)
            else:                                   # number=8:sum=2^(5*num)*(5^3)
                sum *= 3                            # number=9:sum=2^(5*num)*(5^4)
    print(sum)                                      # number=10:sum=2^(5*num)*(5^4)*(3^1)
    return sum                                      # number=11:sum=2^(5*num)*(5^4)*(3^2)
                                                    # number=12:sum=2^(5*num)*(5^4)*(3^3)


mystery(4)
