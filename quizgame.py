#welcome the user
print('Welcome to the quiz')

#Ask user if they would like to play
play = input('Would you like to play? ')

#make answers lower case
if play.lower() != 'yes':
    quit()

#start quiz
print("Okay, let's play!")
#initial score set to zero
score = 0

#first question
answer = input("What does CPU stand for? ")

#first answer
if answer.lower() == "central processing unit":
    print('Correct!')
    #if correct increase score count by 1
    score += 1
else:
    print('Incorrect')
    score += 0

#second question
answer = input("What does GPU stand for? ")
#second answer
if answer.lower() == "graphics processing unit":
    print('Correct!')
        #if correct increase score count by 1

    score += 1 
else:
    print('Incorrect')
    score += 0
#Third question
answer = input("What does RAM stand for? ")
#third answer
if answer.lower() == "random access memory":
    print('Correct!')
        #if correct increase score count by 1

    score += 1
else:
    print('Incorrect')

#Fourth question
answer = input('What does PSU stand for? ')
#fourth answer
if answer.lower() == 'power supply':
    print('Correct!')
        #if correct increase score count by 1

    score += 1
else:
    print('Incorrect')

#Calculate how many they got correct and print the answer with feedback
print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) *100) + " percent correct") #update dividing number depending on number of questions in quiz

if score < 2:
    print("you need to practice!")
else:
    print('Youy know your stuff')