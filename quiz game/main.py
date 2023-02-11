from Questions import Questions
#list of questions which have questions
quiz_bank = [
    "1)ALU stands for?\na)Arithmetic Logic Unit\nb)Application Logic Unit\nc)Array Logic Unit\nd)None of above",
    "2)Which of the following is valid storage type?\na)CPU\nb)Keyboard\nc)Pen Drive\nd)Track Ball\ne)None of the above",
    "3)What does HTML stand for?\na)High text Made a Language \nb)Hyper total Mixed Language \nc)Hypertext Markup Language\nd)High text Make Language",
    "4)What do you mean by SQL?\na)Superior Questions Lot\nb)Standard Query Lot\nc)Statistical Query Language\nd)Structured Query Language\n"

]
#every question in Question class to prompt it and store the answer
ques = [
            Questions(quiz_bank[0], "a"),
            Questions(quiz_bank[1], "a"),
            Questions(quiz_bank[2], "c"),
            Questions(quiz_bank[3], "d"),
  ]



def run_quiz(ques):
    score = 0
    for i in ques:
        ans = input(i.prompt + "\n")
        if ans == i.answer:
            score +=1
    print("You answerd " + str(score) +"/"+str(len(ques))+ " CORRECT!\n")
    print("You got " + str((score/4) *100) + "%.")

#QUIZ START
print("WELCOME TO QUIZ GAME!")

play = input("Do you want to play? [yes or no ]")
if play != "yes":
    quit("QUIT")

print("Ok, Lets play ^_^ \n")
run_quiz(ques)



