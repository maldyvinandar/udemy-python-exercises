# Sample for Conditionals


hungry = False

if hungry:
    print('Feed Me')
elif not hungry:
    print('Go to sleep')
else:
    print('Do nothing')

# For Loops Samples

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in mylist:
    print(num)
    print('hello')

for num in mylist:
    # Check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')

list_sum = 0

for num in mylist:
    list_sum = list_sum + num

    print(list_sum)

mystring = 'Hello World'

for letter in mystring:
    print(letter)

tup = (1, 2, 3)

for item in tup:
    print(item)


mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]

len(mylist)

for item in mylist:
    print(item)

# Tuple unpacking example
for a, b in mylist:
    print(b)

# Useful Operators in Python

index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1
