from multiprocessing.sharedctypes import Value
from random import randint

t = ["Paper", "Rock", "Scissor : "]
options = input("Paper,Rock,Scissor : ")

computer = t [randint(0,2)]

n=0
a=0
value=0


def score(n , a):
    if(value=="Player Wins"):
        n+=1
        
    else:
        a+=1


if (options=="Rock" and computer=="Paper"):
    print("Computer Wins")
    value="Computer Wins"
    score(n,a)

elif (options=="Rock" and computer=="Scissor"):
    print("Player Wins")
    value="Player Wins"
    score(n,a)

elif (options=="Rock" and computer=="Rock"):
    print("It's a tie")
    
elif (options=="Paper" and computer=="Scissor"):
    print("Computer Wins")
    value="Computer Wins"
    score(n,a)

elif (options=="Paper" and computer=="Rock"):
    print("Player Wins")
    value="Player Wins"
    score(n,a)

elif (options=="Paper" and computer=="Paper"):
    print("It's a tie")
   

elif (options=="Scissor" and computer=="Scissor"):
    print("It's a tie")

elif (options=="Scissor" and computer=="Rock"):
    print("Computer Wins")
    value="Computer Wins"
    score(n,a)
elif (options=="Scissor" and computer=="Paper"):
    print("Player Wins")
    value="Player Wins"
    score(n,a)




