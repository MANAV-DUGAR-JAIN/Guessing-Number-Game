import random
print ("Number Guessing Game")
number = random.randint(1,9)

chances=0
print ("Guess a Number Between 1-9 :-")

while chances < 5:
    guess=int(input("Enter Your Guess :-"))

    if guess == number:
        print("Congratulations 😀👍 You Won") 
        break 
    elif guess < number:
        print ("Your Guess was too Low, Guess a number higher than",guess)
    else: 
        print("Your Guess was too High, Guess a number lower than",guess)

chances +=1

if not chances < 5:
    print("You lost, You need to work better next time . The number was",guess)