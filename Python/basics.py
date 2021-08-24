#*Lists are mutable
"""
print(4*(6+5))
print(4 * 6 + 5)
print(4 + 6 * 5)
"""

"""
s = 'hello'
print(s[::-1]) #reversing a string
print(s[-1:])
"""
"""
mylist = [0] * 3
list3 = [1, 2, [3, 4, 'hello']]
list3[2][2] = 'goodbye'
#print(mylist)
#print(list3)
"""
"""
list4 = [5, 3, 4, 6, 1]
list4.sort()
#print(list4)
"""
"""
unsortedList = ['a','f','t','p','w','k']
unsortedList.sort()
#(unsortedList)
#print(myList[1:])
"""

"""
#Dictionaries
d = {'simple_key': 'hello'}
print(d['simple_key'])
d2 = {'k1': {'k2': 'hello'}}
print(d2['k1']['k2'])
d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])
myDict = {'girl':23, 'boy':34 ,'woman':56, 'man':90}
for i, v in sorted(myDict.items()):
    print(i.upper(),v)

#print(myDict['girl'])
"""

myset =  set('Wolverine')
print("Here is my set!")
print(myset)

#For-Loops
aList =  [7,45,12,98,45,23,30]
for i in aList:
    if i % 2 == 0:
        print(i)
    else:
        print(f'Odd Number init: {i}')
"""
#Sum
aString = 'Hello World'
for letter in aString:
    print(letter, end="")
    """

"""
anotherList = [(1,2),(35,42),(75,62),(120,320)]
for (a,g) in anotherList:
    print(a,g)
"""

"""
x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x += 1
else:
    print('X aint less than 5')

for letter in 'Ilikegirls':
    if letter == 'i':
        continue
    #print(letter, end='')
"""

#RANGE

myList1 = [12,34,56,78]
for n in range(1,11,2):
    print(n)

word = 'saliva'
for i,l in enumerate(word):
    print(i,l)
"""
"""
mylist1 = [1,2,3,4,5,6,7,8,9]
mylist2 = ['M','n','a','m','e','is','C','h','i','g','o','z'
]
for item in zip(mylist1,mylist2):
    print(item)
"""

#LIST COMPREHENSION
#Ordinary Way
mylist = []
for letter in 'Helloworld':
    mylist.append(letter)

print(mylist)

#List Comp
mystring = 'Zedd is Awesome'
mylist2 = [letter for letter in mystring ]
print(mylist2)

mylist3 = [ num**2 for num in range(0,11) if num % 2==0]
print(mylist3)

#LAMBDA/MAP/FILTER
def square(num):
    return num ** 2

'''
If you have a list and want to apply the square function to each element, you use the map keyword
'''


my_nums = [1,2,3,4,5]
for item in map(square,my_nums):
    print(item, end=' ')





