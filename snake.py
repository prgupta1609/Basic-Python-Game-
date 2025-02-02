'''
-1 for water
1 for snake
0 for gun
'''
import random

computer = random.choice([1,-1,0])

youstr = input("enter your choice ")

youdict = {"s":1 ,"w":-1, "g": 0}

reversedict = {1:"snake",-1 : "water" ,0: "gun"}

you = youdict[youstr]

print(f"you choose {reversedict[you]}\n computer choose {reversedict[computer]}")

if (computer == you):
    print("Its a draw")

else:

    if (computer == -1 and you == 1):
        print("You win")

    elif (computer == -1 and you == 0):
        print(" you loose")
    
    elif (computer == 1 and you == -1):
        print(" you loose")
       
       
    elif (computer == 1 and you == 0):
        print(" you win")
       
       
    elif (computer == 0 and you == -1):
        print(" you win")
       
       
    elif (computer == 0 and you == 1):
        print(" you loose")
    else:
        print(" something went wrong")