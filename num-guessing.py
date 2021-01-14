import random

#welcome messages
print("Welcome to the number guessing game!\n")
print("This is a game where you guess a number and I tell you if you are right or not!\n")

#Max
max = int(input("What is the max you would like to guess? :"))

#Create random number
magic_num = random.randint(1,max)

#Get user's input
guess = int(input(f"\nEnter your guess here (under {max})! :"))

if guess == magic_num:
    print("You got it right!")

while guess != magic_num:

    if guess == magic_num:
        print("You got it right!")
    elif guess < magic_num:
        print("You guessed too low!")
    elif guess > magic_num:
        print("You guessed too high!")
    else:
        print("You found an error")

    guess = int(input("\nEnter your guess here:  "))

    if guess == magic_num:
        print("You got it right!")