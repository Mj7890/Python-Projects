import random2 as r # type: ignore

print("Welcome to Number Guessing Game. Let's start a game")
last  = int(input("Enter last range no."))



GuessNo = r.randrange(last)

chances = 7
guess_counter = 0

while(guess_counter < chances):
    guess_counter +=1
    myGuess = int(input("Enter your guess No."))
    if(myGuess == GuessNo):
        print(f"The number is {GuessNo} and you found it in the {guess_counter} attempt")
        break
    elif(guess_counter>= chances and myGuess):
        print(f"Oops!, The number is {GuessNo} better luck next time")
    elif myGuess > GuessNo:
        print('Your guess is higher ')

    elif myGuess < GuessNo:
        print('Your guess is lesser')



