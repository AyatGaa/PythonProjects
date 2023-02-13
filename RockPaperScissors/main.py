import random
'''
Rock Paper Scissors game with computer
init tools[ Rock, Paper, Scissors]
init computer random choice
get user choise  tools[ Rock, Paper, Scissors] or quit
    if user_choice == rock and computer == scissors ==> you won!
    elif user_choice == paper and computer == rock ==> you won!
    elif user_choice == scissors and computer == paper ==> you won!
    else computer won!
    increase user cnt while win
    increase computer cnt while lose
    
'''

tools = ["rock", "paper", "scissors"]
#          0      1         2

user_score = 0
computer_score =0
while True:
    user_choice = input("Type (Rock-Paper-Scissors) or Q for quit ").lower()
    rand_number = random.randrange(0, 2)
    if user_choice == "q":
        break
    if user_choice not in tools:
        print("Please select one off these tools !")
        continue
    computer_choice = tools[rand_number]

    if user_choice == "rock" and computer_choice == "scissors":
        user_score +=1
        print("Computer choice is "+ computer_choice)
        print("You Won! *_*")
    elif user_choice == "paper" and computer_choice == "rock":
        print("Computer choice is "+ computer_choice)
        user_score += 1
        print("You Won! *_*")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("Computer choice is ", computer_choice)
        user_score += 1
        print("You Won! *_*")
    elif user_choice == computer_choice:
        print("Computer choice is ", computer_choice)
        print("Draw! ")
    else:
        print("Computer choice is ", computer_choice)
        computer_score += 1
        print("You Lost! :( ")

print("You won " , str(user_score)," times.")
print("The computer won ", str(computer_score)," times.")
print("Good bye ^_^")


