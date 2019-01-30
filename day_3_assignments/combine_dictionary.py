from collections import Counter

# def combine_dictionary_():
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
combine_elements = Counter(d1) + Counter(d2)
print(combine_elements)
