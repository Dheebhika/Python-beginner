def add(*args):
    sum = 0
    for num in args:
        sum = sum + num
    print (sum)
    print(type(args))

add(1,2,3,4,5,6,7,8,9)


#a = [1,2]
#def x(*num):
    #num[0]=10
    #num[1]=20
    #print (num)
#x(1,2)
