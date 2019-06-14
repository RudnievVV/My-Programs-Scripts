#! python3
# guess.py - random guess-number program

import random

print('Hello, kiddo! What is you name?')
name = input()+'-kiddo'

secretNumber = random.randint(1,20)
print(name + ', I am thinking of a number between 1 and 20.')
print('DEBUG: ' + str(secretNumber))
for guessesTaken in range(1, 6):
    try:
        print('Take a guess. Attempts left: ' +str(6 - guessesTaken))
        guess = int(input())
        if guess < secretNumber:
            print('Your guess is too low.')
        elif guess > secretNumber:
            print('Your guess is too high.')
        else:
            break # This condition is the correct guess
    except ValueError:
        print('Enter a number please.')
while guess == secretNumber:
    if guessesTaken == 1:
        print('Great job, ' + name +'! You guessed my number in ' + str(guessesTaken) + ' guess!')
        break
    elif guessesTaken >1:
        print('Great job, ' + name +'! You guessed my number in ' + str(guessesTaken) + ' guesses!')
        break
else:
    print('You are out of attempts. The number I was thinking of was ' + str(secretNumber)+'.')
