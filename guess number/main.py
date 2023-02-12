import random
'''
1- enter top of random number 
2- check if isdigit
3- check if negative 
4- take user guess 
5- check if it true if not loop until get it 
6- count num of guesses !
'''


max_num = input("Please Enter Number: ")
if max_num.isdigit():
    max_num = int(max_num)
    if max_num <= 0:
        #print("Please enter a number greater than zero!")
        quit("Enter Number greater than 0 ")
else:
    #print("Please enter a number next time. ")
    quit("Please enter a number next time. ")

rand = random.randrange(0,max_num)
guesses_number = 0

while True:
    guesses_number += 1
    user_guess = input("Enter your guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number next time!")
        continue
    if user_guess == rand:
        print("You got it ! ")
        break
    elif user_guess > rand:
        print("You are above the number ")
    elif user_guess < rand:
        print("You are below the number  ")

print("You got it in ", guesses_number , "guesses")