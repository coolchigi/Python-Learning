from random import randint

guess = randint(1, 100)
userName = input('What is your name? ')
print(f'Welcome to my guessing game {userName}')


playerGuess = [0]
while True:
    userGuess = int(input('Guess a number between 1 and 100: '))

    if userGuess < 1 or userGuess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue
    # If the user's guess equal, break else append to the player guess list
    if userGuess == guess:
        print(f'Congrats! You got that on your {len(playerGuess)} attempt')
        break
    playerGuess.append(userGuess)
    if userGuess > guess:
        print('Your guess is too high, try a lower number')
    else:
        print('Your guess is too low, try a higher a number')
