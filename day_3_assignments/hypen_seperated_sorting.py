items = input("Enter the sequence with hypen: ")
for i in items:
    m = items.split('-')
    m.sort()
print('-'.join(m))

# items=[n for n in input().split('-')]
# items.sort()
# print('-'.join(items))
