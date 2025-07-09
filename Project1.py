"""
This code is a simple game of "Snack, Water, Gun" where the user plays against the computer. 
The user inputs their choice, and the computer randomly selects one of the three options. 
The outcome is determined based on the rules of the game.
Snack beats Water, Water beats Gun, and Gun beats Snack.
"""
import random
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice:")
youDict = {"s":1,"w":-1,"g":0}
reverseDict = {1:"Snack",-1:"Water",0:"gun"}

you = youDict[youstr]
print(f"You chose {reverseDict[you]}\nCOmputer chose {reverseDict[computer]}")

if(computer == you):
    print("It's a tie")
else:
    if(computer == -1 and you == 1):
        print("You win")
    elif(computer == -1 and you == 0):
        print("You lose")
    elif(computer == 1 and you == -1):
        print("You lose")
    elif(computer == 1 and you == 0):
        print("You win")
    elif(computer == 0 and you == -1):
        print("You win")
    elif(computer == 0 and you == 1):
        print("You lose")
    else:
        print("Something went wrong")