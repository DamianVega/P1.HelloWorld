'''

'''

import random

secret = random.randint(1, 99)

guess = 0
tries = 0
print("Can you guess my number?")
print("My number is an integer between 1 and 99.")

while guess != secret and tries < 6 :
    print("Take a guess")
    guess = int(input())
    if guess < secret :
        print("Too low, Guess again :)")
    elif guess > secret :
        print("Too high, Guess again :)")

tries = tries + 1

if guess == secret:
    print("Congrats you guessed it! :)")
else :
    print("You're out of guesses, Better luck next time :)")
    print("The secret number was : ", secret)