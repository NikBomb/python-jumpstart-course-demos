import random

print("--------------------")
print("GUESS THAT NUMBER")
print("--------------------")

theNumber = random.randint(0, 100)
guess = int(input("Guess a number between 0 and 100: "))

while True:
    if guess < theNumber:
        guess = int(input("Your guess is too low, try again: "))
    elif guess > theNumber:
        guess = int(input("Your guess is too high, try again: "))
    else:
        print("Yes the number was: " + str(guess))
        break
