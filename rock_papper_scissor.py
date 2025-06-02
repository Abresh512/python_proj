import random
computer = random.choice(['r', 's', 'p'])
person = input("What is your choice 'r' for rock 's' for scissor and 'p' for papper: ")

if (computer == 'r' and person == 's') or (computer == 's' and person == 'p') or( computer == 'p' and person == 'r'):
    print(f"You Lose!\ncomputer chose {computer}")
else:
    print("You Won!")