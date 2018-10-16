
# Sample of Dictionaries

my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict)

print(my_dict['key1'])

prices_lookup = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.80}

print(prices_lookup['apple'])

d = {'k1': 123, 'k2': [0, 1, 2], 'k3': {'insidekey':  100}}

print(d['k3']['insidekey'])

print(d.keys())

print(d.values())

# Sample of Tuples

t = (1, 2, 3, 1)

mylist = [1, 2, 3]

print(type(t))

print(type(mylist))

print(len(t))

print(t.count(1))

print(t.index(1))

# Sample of Sets

myset = set()

print(myset)

myset.add(1)

myset.add(2)

print(myset)

mylist = [1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 5, 5, 6]

print(set(mylist))
