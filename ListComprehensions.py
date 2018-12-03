# List Comprehensions in Python

mystring = 'hello'

mylist = [letter for letter in mystring]

print(mylist)

mylist = [num**2 for num in range(0, 11)]

print(mylist)

mylist = [x**2 for x in range(0, 11) if x % 2 == 0]

print(mylist)

celcius = [0, 10, 20, 34.5]

fahrenheit = [((9/5)*temp + 32) for temp in celcius]

print(fahrenheit)

mylist = []

for x in [2, 4, 6]:
    for y in [100, 200, 300]:
        mylist.append(x*y)

print(mylist)

mylist = range(0, 100)

mylist = []

for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        mylist.append('FizzBuzz')
    elif x % 3 == 0:
        mylist.append('Buzz')
    elif x % 5 == 0:
        mylist.append('Buzz')
    else:
        mylist.append(x)

print(mylist)
