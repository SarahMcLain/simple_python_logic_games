import random


def river_scenario():
    answer = input("You come to a river, you can walk around it or swim across. Which do you choose? 'walk' or 'swim':  ").lower()
    if answer == "swim":
        print("You swam across but the current was too strong, you drowned!")
    elif answer == "walk":
        answer = input("You chose to walk, you come to a bridge.  You start to cross the bridge... a troll pops out! What do you do? Pull out your sword and fight or ask the troll what it wants? Choose 'fight' or 'ask': ").lower()
        if answer == "fight":
            print("The troll used it's powerful magic to destroy your sword.  You lose the battle and the troll gets dinner. You lose!")
        elif answer == "ask":
            
            user_joke = input("The troll want's you to tell it a joke to cross the bridge.  Type your joke: ")
            
            troll_response = random.randint(0,1)

            if troll_response == 0:
                print("The troll did not like your joke and ate you. You lose!")
            elif troll_response == 1:
                print("The troll liked your joke and let you across the bridge. \
                      You made it safely across the river and escaped your enemies.  You won!")

                
def spooky_forest_scenario():
    answer = input("You come to a dark spooky forest.  Do you continue through the forest or turn around? Choose 'continue' or 'back'  ").lower()
    if answer == "back":
        river_scenario()
    elif answer == "continue":
        answer = input("You decide to brave the spooky forest. You have been walking for a long time and are now tired. Do you lay down and sleep or continue on? Chose 'sleep' or 'continue'  ").lower()
        if answer == "sleep":
            print("While you were sleeping a hungry witch tracked you down and captured you.  You made her a nice dinner.  You lose!")
        elif answer == "continue":
            print("Although you were tired you persevered on and your perseveranve paid off.  You made it out of the forest and safely away from your enemies. You win!")


username = input("username: ")
print("Welcome", username, "to this adventure")

while True:
    answer = input("You are on a dirt road, it has come to an end.  Do you go left or right?  ").lower()

    if answer == "left":
        river_scenario()
    elif answer == "right":
        spooky_forest_scenario()
    else:
        print("Not valid destination")
    
    backtrack = input("Would you like to backtrack and explore other options? Type yes or no:  ").lower()
    if backtrack != 'yes':
        break

