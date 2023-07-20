# <---------------------------the perfect guess game-------------------------------------?

import random
randNumb= random.randint(1, 100)
# print(randNumb)
userGuess=None
guesses=0

while(userGuess != randNumb):
    userGuess=int(input("enter your guess::::"))
    guesses +=1
    if (userGuess==randNumb):
        print("----------------Your guess is right--------------------")
    else:
        if(userGuess>randNumb):
            print("You guessed it wrong, enter LOWER number")
        else:
            print("You guessed it wrong, enter HIGHER number")

print(f"You guessed the number in {guesses} guesses")

with open("project/highscore.txt",'r') as f:
    highscore = int(f.read())

if(guesses<highscore):
    print("<<<<<<<<<<<You have set new record:>>>>>>>>>>>>")
    with open('project/highscore.txt','w') as f:
        f.write(str(guesses))