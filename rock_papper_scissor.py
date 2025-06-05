#Hello Family, today we're going to build a rock, papper scissor game aginst to the computer...let's get started


#                                           DON'T FORGET TO SUBSCRIBE

#First we're gonna import the python random module, so...
import random

# and now lets make the computer to choose from the tree choices which are ['r' for rock, 'p' for papper and 's' for scissor]
computer = random.choice(['r', 'p', 's'])

# and now it's users turn, 
user = input("what is your choice 'r' for rock 'p' for papper and 's' for scissor: ")

#at the end we're gonna see who wons the game...
if (user == 'r' and computer == 'p') or (user == 'p' and computer == 's') or (user == 's' and computer == 'r'):
    print("You won! CONGRATS.")
elif (user == computer):
    print(f"IT's a TIE! you both chose {user}") #here we can also say computer b/c thier play is the same
else:
    print(f"You LOST! the computer chose {computer} and you chose {user}.")

#now let's see where we messed up :)