import random


options = ['rock', 'paper', 'scissors']
user_wins = 0
computer_wins = 0
tie = 0
while True:
    user = input("Type rock/paper/scissors or Q to quit: ").lower()
    if user == 'q':
        break
    if user not in options:
        continue
    random_number = random.randint(0, 2)
    computer = options[random_number]
    if user == computer:
        print("It's a Tie!")
        tie += 1
    elif user == 'rock' and computer == 'scissors' or user == 'paper' and computer == 'paper' or user == 'scissors' and computer == 'paper':
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1

        
print("Goodbye")
print("You won", user_wins,'times'+'.')
print("The computer won", computer_wins, 'times'+'. And')
print(tie, 'ties.')