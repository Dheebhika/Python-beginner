def sorting():
    items = input("Enter the sequence with hypen: ")
    for i in items:
        m = items.split('-')
        m.sort()
    print('-'.join(m))


sorting()

# items=[n for n in input().split('-')]
# items.sort()
# print('-'.join(items))
