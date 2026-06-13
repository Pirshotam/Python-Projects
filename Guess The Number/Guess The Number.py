import random

print("=====Guess The Number=====")

number=random.randint(1,10)
attempts=5
print("I'm thinking of a number between 1 and 10. You have",attempts,"attempts.")
while attempts>0:
    userChoice=input("Enter your guess or Quit(Q): ")
    if userChoice=="Q":
        break
    userChoice=int(userChoice)
    if userChoice>number:
        print("Number too big\nTry a smaller number")
    elif userChoice<number:
        print("Number too small\nTry a bigger number")
    else:
        print("Congrats! You guessed the number right")
        break
    attempts-=1
print("=====END=====")
