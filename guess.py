import random
n = random.randint(1,34)
guess = int(input("Enter an integer from 1 to 34: "))
while n != "guess":
    print
    if guess < n:
        print ("guess is low")
        guess = int(input("Enter an integer from 1 to 34: "))
    elif guess > n:
        print ("guess is high")
        guess = int(input("Enter an integer from 1 to 34: "))
    else:
        print ("you guessed it!")
        break
    print




sample output 1 to 34:23
sample output you guessed it
