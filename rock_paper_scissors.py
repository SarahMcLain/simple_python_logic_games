import random

#set user and computer initial scores to zero
user_wins = 0
comp_wins = 0

#create array of options for game
options = ["rock", "paper", "scissors"]

#start game
while True:
    #have user pick rock, paper, scissors or quit the game
    user_input = input("Pick Rock, Paper, Scissors or Q to quit.   ").lower()
    #if user picks q quit the game
    if user_input == "q":
        break
    #continue if not q
    if user_input not in options:
        continue
    #have the computer generate random number between 0 and 2
    random_number = random.randint(0,2)
    #0: rock, 1: paper, 2: scissors 
    #have computer pick go from number to rock, paper, or scissors
    comp_pick = options[random_number]
    print("Computer picked: ", comp_pick)
    
    #check the different winning scenarios and +1 to count for each win
    if user_input == "rock" and comp_pick == "scissors":
        print('You won!')
        user_wins += 1
        
    if user_input == "paper" and comp_pick == "rock":
        print('You won!')
        user_wins += 1
        
    if user_input == "scissors" and comp_pick == "paper":
        print('You won!')
        user_wins += 1
    #if none of the winning scenarios are true then you lost the round. Add 1 to computer score each
    #time user loses
    else:
        print("You lost")
        comp_wins += 1
#When user quits the game print out the final scores
print("You won ", user_wins, "times. Computer won", comp_wins, "times.")

