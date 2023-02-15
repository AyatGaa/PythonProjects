'''
address book
-help user to store email addresses & passwords, and other operation can do on its data
-deal with data from text file "next version I'll do it with Database"
-operation that user can do:
    1- add address and password
    2- view the address
    3- delete from address
    4- edit address

Note:to make any action on file MUST OPEN IT IN READ 'r' Mode FIRST!
'''


def add():
    email = input("Email :  ")
    psw = input("Password :  ")
    with open("data.txt", "a") as file:
        file.write(email + " |" + psw + "\n")

def view():
    cnt_lines = 0
    with open("data.txt", "r") as file:
        for line in file.readlines():
            data = line.rstrip()
           #global emails, passwords
            emails, passwords = data.split(" |")
            cnt_lines +=1
            print(str(cnt_lines) + "- Email:", emails, " | Password:", passwords )

def delete():
    #open file in read mode first to read lines in var.
    with open('data.txt', 'r') as file:
        input_file_lines = file.readlines()
    #ask user for which email need to delete and view the list
    print("Which email you need to delete? PLEASE TYPE LINE NUMBER")
    view()
    #init of line number to search all over the file
    line_num =1
    #take the number from user and convert it to int to loop
    num_del_data = int(input(" PLEASE TYPE LINE NUMBER TO DELETE IT"))

    # open file again in write mode
    with open('data.txt', 'w') as file:
        #loop line by line
        for line in input_file_lines:
            #check if desired line number equal to current line ?
            if line_num != num_del_data:
                #if not write agian the same line!
                file.write(line)
            #increase counter for next line
            line_num += 1

# to show data of delete row we use index of [num_del_data -1 ] to acces it from the list of input_file_lines is zero index
        print("Email data, ", num_del_data, input_file_lines[num_del_data-1], "is deleted successfully")
    print("The Email List :")
    view()

def edit():
    #open file to read lines
    with open('data.txt', 'r') as file:
        input_file_lines = file.readlines()
        print("Which email you need to modify? Please Enter Email Number")
        view()
        line_num = 1

        num_edit_data = int(input(" PLEASE Enter Email Number To Modify it"))
        #open data to modify it
        with open('data.txt ', 'w') as file:
            #loop on file
            for line in input_file_lines:
                # check if desired line number equal to current line
                if line_num != num_edit_data:
                    file.write(line)
                else:
                    email = input("Enter new email : ")
                    psw = input("Enter new password : ")
                    file.write(email + " |" + psw + "\n")
                #increase line counter
                line_num += 1
        print("Email data modified successfully!")
        print("The Email List After Modifying :")
        view()

def address_book():
    while True:
        action = input("What do you want? \n     [add - view - edit - delete - Q for quit ]").lower()
        if action == "q":
            print("==================End of program ======================================")
            break
        if action == "add":
            add()
            print("==================End of", action, " operation==========================")
        elif action == "view":
            view()
            print("==================End of", action, " operation==========================")
        elif action == "delete":
            delete()
            print("==================End of", action, " operation==========================")
        elif action == "edit":
            edit()
            print("==================End of", action, " operation==========================")
        else:
            print("Invalid Action!")
            print("Please type one of those actions")

#check login with fixed'pre-defined' email and password in external file
def login_check():
    usernm_entry = input("Username: ")
    pass_entry = input("Password: ")

    with open('login_info.txt', 'r') as login_file:

        for line in login_file.readlines():
             data = line.rstrip()
             master_nm ,pswd_master = data.split(" ")

        if master_nm == usernm_entry and pass_entry == pswd_master:
            address_book()
        else:
            quit("Wrong Password or Username, please try again after restart the program!")


print("      Welcome to Your Addresses Book ")
print("*********************************************** ")
login_check()
