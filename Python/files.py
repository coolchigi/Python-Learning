with open('mylife.txt', 'r') as myfile:
    lines = myfile.read()
    words = lines.split()
    

for word in words:
    print(word)
print(lines)


def myfunc(string):
    returned_String = ''
    for index, letter in enumerate(string):
        if index % 2 == 0:
           returned_String += letter.upper()
        else:
            returned_String += letter.lower()
        
    return returned_String

print(myfunc('Anthropomorphism Antho'))
word = 'Anthropomorphism Lntho'
first, second = word.split()
print(first)
print(second[0])









