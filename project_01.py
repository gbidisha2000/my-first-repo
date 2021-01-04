import random

def game(computer,you):
    if computer=='s':
        if you=='w':
            print("Snake drinks the water. Computer Wins!")
        else:
            print("Gun kills the snake. You win!")
    elif computer=='w' :
        if you=='s':
            print("Snake drinks the water. You win!")
        else:
            print("No competition between gun and water. No one wins!")
    elif computer=='g':
        if you=='w':
            print("No competition between gun and water. No one wins!")
        else:
            print("Gun kills the snake. Computer wins!")
    else:
        print("Tie!!!")

bids=input("Choose a letter:\nSnake: s\nGun: g\nWater: w\n")

comp=random.randint(1,3)
if comp==1:
    comp='s'
    game(comp,bids)
elif comp==2:
    comp='w'
    game(comp,bids)
else:
    comp='g'
    game(comp,bids)
