#This code is a simple number guessing game where the user has to guess a randomly generated number between 1 and 100. 
#The user can quit the game by entering 'Q'. The game provides feedback on whether the guess is too high or too low.
#The game continues until the user guesses the correct number or chooses to quit.
import random

target = random.randint(1,100)

while True:
    userChoice = input("Guess the target or Quit(Q) ")
    if(userChoice == "Q"):
        break
    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess!!")
        break
    elif(userChoice < target):
        print("your number too Small. take a bigger guess...")
    else:
        print("your number too Big. take a smaller guess...")

print("-----GAME OVER----")