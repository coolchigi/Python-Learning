def say_name(name):
    return f'Hello {name}, how are you?'


"""
userName = input('Enter your name? ')
say_name(userName)
"""


def even_check(num_list):
    even_numbers = []
    for i in num_list:
        if i % 2 == 0:
            even_numbers.append(i)
        else:
            pass
    return even_numbers


a = [12, 34, 5, 7, 90, 21, 27, 79]
print(even_check(a))


# **Kwargs
"""
Treat like a dictionary 
"""


def myfunc(**kwargs):
    if 'fruit' in kwargs:  # fruit is the key
        print('My fruit of choice is {}'.format(kwargs['fruit'])
              )
    else:
        print('I didnt find any fruit here!')


myfunc(fruit='banana', veggie='spinach')


def aFunc(*args, **kwargs):
    print('I like {} {}'.format(args[2], kwargs['gender']))


aFunc(12, 3, 4, 12, food='eggs', gender='girls')

aText = 'I am home'
reverse = aText.split()[::-1]

print(reverse)


def repeat(text):

    repeated = text.split()
    for letter in repeated:
        return letter * 3


print(repeat('I am home'))
print(repeat('You are a girl'))


test = 'Enid Blyton was a great writer'
split_init = test.split()
for let in split_init:
    print(let * 3)
# print(test.split())
