from tkinter import *
from tkinter import messagebox
import random
import json
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter_list = [random.choice(letters) for char in range(nr_letters)]
    symbol_list = [random.choice(symbols) for char in range(nr_symbols)]
    number_list = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = letter_list + symbol_list + number_list

    random.shuffle(password_list)
    password = ''.join(password_list)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    pas = password_entry.get()
    em = email_entry.get()
    web = website_entry.get()

    new_data = {
                web: {
                    'email': em,
                    'password': pas

                     }

                }

    if len(web) == 0 or len(pas) == 0:
         messagebox.showwarning(title='Null entry', message='Please do not leave any field empty')

    else:
        try:
            with open('data.json', "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    webr = website_entry.get()
    with open('data.json','r') as data_file:
        sample_file = json.load(data_file)
        try:
            et = sample_file[webr]["password"]
            em=sample_file[webr]['email']
        except KeyError:
            messagebox.showwarning(title='Unsaved Password',message=f'There is no such password saved for website {webr}')
        else:
            messagebox.showinfo(message=f"Email : {em}\n password: {et}", title='Your Password details')

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(pady=20, padx=20)
window.title('My Password Manager')
window.minsize(width=300, height=300)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file=r"C:\Users\jagya\Downloads\password-manager-start\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)
#Label
web = Label(text='Website:')
web.grid(row=1, column=0)

email = Label(text='Email/username:')
email.grid(row=2, column=0)

password = Label(text='Password:')
password.grid(row=3, column=0)

# Entry

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=1)
email_entry.insert(0, 'jayansis@gmail.com')
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=1)

# Buttons

password_button = Button(text='Generate Password',width=15, command=generate_password)
password_button.grid(row=3, column=2)
add_button = Button(text='add', width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text='Search', width=15, command=find_password)
search_button.grid(row=1, column=2)






window.mainloop()