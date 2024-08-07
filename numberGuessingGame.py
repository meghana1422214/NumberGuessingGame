import random
#random is an already inbuilt library no need for any installations
#random.randnumber generates random numbers from start,end-1
#random.randint generates random numbers from start,end
top_of_range=(input("Type a Number: "))
guesses=0
if(top_of_range.isdigit()):
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print("Please enter a digit greater than 0 next time")
        quit()
else:
    print("Please type a number next time.")
    quit()
  

randomNumber=random.randint(0,top_of_range)
while(True):
    guesses+=1
    userGuess=input("Make a guess: ")
    if(userGuess.isdigit()):
       userGuess=int(userGuess)
    else:
        print("Please type a number next time.")
        continue
    if(userGuess==randomNumber):
        print("You got it!")
        break
    elif(userGuess>randomNumber):
        print("You are above the number.")
    else:
        print("You are below the number.")

print("You got it in,", guesses,"guesses")
