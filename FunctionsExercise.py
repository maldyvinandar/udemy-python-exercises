def name_function():
    '''
    DOCSTRING: Information about the name_function
    INPUT: no input...
    OUTPUT: Hello
    '''
    print('Hello')


name_function()

help(name_function)

# Add default to method parameter


def say_hello(name='NAME'):
    print('Hello '+name)


say_hello('John')

say_hello()

# Pig Latin example


def pig_latin(word):
    first_letter = word[0]
    # check if vowel
    if first_letter in 'aiueo':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'

        return pig_word


print(pig_latin('laptop'))
