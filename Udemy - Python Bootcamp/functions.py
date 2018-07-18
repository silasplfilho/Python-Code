def name():
    '''
    DOCSTRING: Info about function
    INPUT: name
    OUTPUT: hello
    '''
    print('Hello')
#----------------------
def say_hello(name='MISERABLE'):
    return('hello ' +name)

result = say_hello('Sally')
result
#----------------------
def add(n1, n2):
    return n1 + n2

result = add(20, 30)
result
#----------------------
def dog_check(mystring):
    return 'dog' in mystring.lower()

dog_check('doggo ran away')
#----------------------
def pig_latin(word):
    first_letter = word[0]

    #check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'

    return(pig_word)

pig_latin('apple')
#----------------------
def myfunc(*args):
    for item in args:
        print(item)

myfunc(5, 10, 15, 20)
#----------------------
def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('my fruit choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find fruit here')

myfunc(fruit='apple', veggie = 'lettucce    ')
#----------------------
def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print('i would like {} {}'.format(args[0], kwargs['food']))

myfunc(10, 20, 30, fruit='orange', food='eggs', animal='dog')

#------ Learning Python
def times(*args):
    return(args )

#------
def factorial(n):
    '''returns n'''
    return 1 if n<2 else n * factorial(n-1)

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
sorted(fruits, key=len)

#------
def reverse(word):
    return word[::-1]

reverse('testing')
sorted(fruits, key=reverse)
#------
list(map(factorial, range(6)))
[factorial(n) for n in range(6)]
list(map(factorial, filter(lambda n : n % 2, range(6))))
[factorial(n) for n in range(6) if n % 2]
#------
from functools import reduce
from operator import add
reduce(add, range(100))
sorted(fruits, key=lambda word: word[::-1])

#------
import random

class BingoCage:
