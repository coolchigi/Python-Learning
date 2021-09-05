from functions import repeat


st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 's':
        print(word)

# 2
evenNum = [x for x in range(0, 11) if x % 2 == 0]
print(evenNum)

# 3
divisibleByThree = [num for num in range(1, 51) if num % 3 == 0]
print(divisibleByThree)

# 4
sts = 'Print every word in this sentence that has an even number of letters'
for word in sts.split():
    if len(word) % 2 == 0:
        print(f'Length of {word} is even!')

# 5
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print(f'{number} => FizzBuzz')
    if(number % 3 == 0):
        print(f'{number} => Fizz')
    else:
        print(f'{number} => Buzz')

# 6
std = 'Create a list of the first letters of every word in this string'
firstLetter = [first[0] for first in std.split()]
print(firstLetter)

# 7


def myfunc(string):
    returned_String = ""  # the returned string
    for letter in string:
        if string.index(letter) % 2 == 0:
            returned_String += letter.upper()
        else:
            returned_String += letter.lower()

    return returned_String


result = myfunc('Anthropomorphism')

print(result)

# 8


def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


print(lesser_of_two_evens(2, 4))

# 9


def animal_crackers(text):
    firstLet, secondLet = text.split(" ")
    if firstLet[0] == secondLet[0]:
        return True
    else:
        return False


print(animal_crackers('Levelheaded Llama'))

# 10


def makes_twenty(n1, n2):
    if (n1+n2) == 20 or n1 == 20 or n2 == 20:
        return True
    else:
        return False


print(makes_twenty(20, 10))

# 11


def old_macdonald(name):

    return name[0:3].capitalize() + name[3:].capitalize()


print(old_macdonald('macdonald'))

# 12


def master_yoda(text):
    reverse = text.split()[::-1]
    return ' '.join(reverse)


print(master_yoda('I am home'))
print(master_yoda('We are ready'))


# 13
def almost_there(n):
    if abs(n - 100) <= 10 or abs(n-200) <= 10:
        return True
    else:
        return False


print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

# 14


def has_33(nums):
    for i in range(len(nums)-1):  # The len(list) is > than the index positions
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False


print('The has_33 function results')
print(has_33([1, 3, 3]))
print(has_33([44, 33, 1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

# 15


def paper_doll(text):
    full_string = ''
    for letter in text:
        full_string += letter * 3
    return full_string


print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

# 16

print('BlackJack function results: ')


def blackJack(a, b, c):
    numberSum = a + b + c
    if numberSum <= 21:
        return numberSum
    elif numberSum >= 21 and a == 11 or b == 11 or c == 11:
        return numberSum - 10
    else:
        if numberSum >= 21:
            return 'BUST'


print(blackJack(5, 6, 7))
print(blackJack(9, 9, 9))
print(blackJack(9, 9, 11))

# 17


def summer_69(arr):
    sum = 0
    for num in arr:
        if num == 6 or num == 9:
            continue

        elif num != 6 and num != 9:
            sum += num
    return sum


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))

# 18

print('Result of the spy_game function')


def spy_game(nums):
    placeHolder = [0,0,7,'x']
    for i in nums:
        if i == placeHolder[0]:
            placeHolder.pop(0)
    return len(placeHolder) == 1


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 7, 5]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))


#19

def count_primes(nums):
    if nums < 2:
        return 0
