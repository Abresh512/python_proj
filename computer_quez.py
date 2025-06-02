#now let's tell the user their score
score = 0

#first we ask the user if he want to play or not
print("Welcome to computer quez. Do you want to proceed to the questions? (yes/no)")
#after this we accept the users answer via input method built in python

play = input().lower() #.lower means change the word user inputs to lowercase

# and after this we check if the user wants to play or not
if play != 'yes':
    print("Alright, Maybe next time.")
# if user enters "Yes" that means user wants to play so we give question to the user.
else:
    print("1. What does CPU stands for? ")
    #here we're gonna store the correct answer in a varaible so we can use it later
    answer = "Central Processing unit".lower()

    #and we recieve user input here and store it in a varaible
    user_answer = input().lower()

    #after this we check if the user's answer is correct or not
    if user_answer == answer:
        print("Correct!\n")
        score+=1 # this means if the user is correct add to the top variable 'score' 1 we can also write it as score = score + 1
    else:
        print(f"Incorrect. The correct answer is {answer}\n")

        #let's add some questions, actually let's copy and paste

    
    print("2. What does GPU stands for? ")
    #here we're gonna store the correct answer in a varaible so we can use it later
    answer = "Graphical Processing unit".lower()

    #and we recieve user input here and store it in a varaible
    user_answer = input().lower()

    #after this we check if the user's answer is correct or not
    if user_answer == answer:
        print("Correct!\n")
        score+=1
    else:
        print(f"Incorrect. The correct answer is {answer}\n")


    print("3. What does RAM stands for? ")
    #here we're gonna store the correct answer in a varaible so we can use it later
    answer = "Random Access Memory".lower()

    #and we recieve user input here and store it in a varaible
    user_answer = input().lower()

    #after this we check if the user's answer is correct or not
    if user_answer == answer:
        print("Correct!\n")
        score+=1
    else:
        print(f"Incorrect. The correct answer is {answer}\n")


    print("4. What does ROM stands for? ")
    #here we're gonna store the correct answer in a varaible so we can use it later
    answer = "Read Only Memory".lower()

    #and we recieve user input here and store it in a varaible
    user_answer = input().lower()

    #after this we check if the user's answer is correct or not
    if user_answer == answer:
        print("Correct!\n")
        score+=1
    else:
        print(f"Incorrect. The correct answer is {answer}")
    
    print(f"you've got {score} out of 4")
    print(f"your percentage is {score / 4 * 100}")