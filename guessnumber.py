import random

#generate a number between 1 and 100
number = random.randint(1,100)
#set the initial guess to zero
guess = 0
#set the number of counts at zero
count = 0

#create an if statement to check if the user guess matches
#the computer generated number and provide feedback 
while guess != number:
    guess = int(input('Enter Guess: '))

    if (guess < number):
        print('Guess higher!')
        count += 1
    elif (guess > number):
        print('Guess lower!')
        count += 1
    else:
        print('You won!')

print("I took you " + str(count) + " times to guess the number")

    
    
