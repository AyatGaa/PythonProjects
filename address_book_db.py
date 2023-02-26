import PySimpleGUI as gui
import csv

#the theme
gui.theme('Dark blue 2')

gui.set_options(font='Arial 18')

#layout of prog ,,,
layout =[
        [gui.Text('Application Info', font='Fixedsys 20 bold')],
        [gui.Text("E-mail/username :"), gui.Push(), gui.InputText(key='-email-')],# push function to make space between text in input field
        [gui.Text("Password :"), gui.Push(), gui.InputText(key='-pswd-')],
        [gui.Text("Related To :"), gui.Push(), gui.InputText(key='-type-')],
        [gui.Button('Save'), gui.Button('Cancel')],
        [gui.InputText(key='-searchText-'), gui.Button('Search')],
        [gui.Text(font='Courier 18', text_color='white', key='-searchoutput-')], [gui.Button('Last Info')]
]
'''
key for input text  then 
event for button search to action upon it
key for text area to show output of search! "searchoutput'
'''

#init window
window = gui.Window(('Emails Books'), layout, icon='email.ico')

#to show window while run using while loop
while True:
    event, values = window.read()
    #close prog if user click on 'Cancel' or X
    if event == gui.WIN_CLOSED or event == 'Cancel':
        break
    #save each field user add in valuse list
    email = values['-email-']
    password = values['-pswd-']
    related_to = values['-type-']
    data = [email, password, related_to]

    #save data
    if event == 'Save':
        #check if all fields are fill with data
        if email == '' or password == '' or related_to == '':
            gui.popup_ok('Please fill all fields', title='Message', icon='email.ico', line_width=200)
        else:
            with open('data.csv', 'a', newline="") as w:
                save_data = csv.writer(w)  # csv comma saver writer
                save_data.writerow(data)  # save data in row
            window['-email-'].update('')
            window['-pswd-'].update('')
            window['-type-'].update('')

    search_txt = values['-searchText-']

    #list to add searched element in it and show it easily
    data = []
    if event == 'Search':
        with open('data.csv', 'r') as r:
            read_data = csv.reader(r)
            for row in read_data:
                for ele in row:
                  if ele == search_txt:
                    #window['-searchoutput-'].update(f"Application : {i[2]}\nE-mail address : {i[0]}\nPassword : {i[1]}")
                    data.append(row)
                    window['-searchoutput-'].update(f"Application : {row[2]}\nE-mail address : {row[0]}\nPassword : {row[1]}")
                  else:
                    window['-searchoutput-'].update(f"Data Not Found!")


#to show last info added to file
    if event == 'Last Info':
        all_info = []
        with open('data.csv', 'r') as rall:
            reader = csv.reader(rall)
            for row in reader:
                all_info.append(row)

            for i in all_info:
               window['-searchoutput-'].update(f"Application : {i[2]}\nE-mail address : {i[0]}\nPassword : {i[1]}")


window.Close()




#"f ==>translate which in { } into it's value

