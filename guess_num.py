import random


top_range = int(input("enter the top num: "))
rdm_num = random.randint(1, top_range)
num_of_guesses = 0
while True:
    num_of_guesses += 1
    usr_input = int(input("Enter a number: "))
    if rdm_num == usr_input:
        print(f"You got it right with {num_of_guesses} guesses.")
        break
    elif rdm_num > usr_input:
        print(f"guess a number greater than {usr_input} ")
    else:
        print(f"guess a number less than {usr_input} ")
