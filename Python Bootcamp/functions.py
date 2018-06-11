def name():
    '''
    DOCSTRING: Info about function
    INPUT: name
    OUTPUT: hello
    '''
    print('Hello')

def say_hello(name='MISERABLE'):
    return('hello ' +name)

result = say_hello('Sally')
result

def add(n1, n2):
    return n1 + n2

result = add(20, 30)
result

def dog_check(mystring):
    return 'dog' in mystring.lower()

dog_check('doggo ran away')

def pig_latin(word):
    first_letter = word[0]

    #check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'

    return(pig_word)

pig_latin('apple')
