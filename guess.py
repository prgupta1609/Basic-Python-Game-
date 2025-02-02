import random
n = random.randint(1,100)
a = -1
guesses = 1

while(a!= n):
    a = int(input ("enter the number"))
    if(a >n):
        print("enter a samller number")
    elif(a<n):
        print("enter a larger number ")
        
        guesses+=1
print(f" you have gussed the {n} in {guesses} attempts")