import random
from tkinter import *
from tkinter import messagebox
import os
import json

os.system('cls')

FONT = ('times new roman', 12, 'normal')
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_num = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letter+password_num+password_symbol

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():

    website = website_entry.get()
    user_id = user_id_entry.get()
    password = password_entry.get()

    new_data = {website: {
        "email": user_id,
        "password": password,
    }}
    if len(website) == 0 or len(user_id) == 0 or len(password) == 0:
        messagebox.showwarning(
            title="Waring", message="Please dont leave any field empty.")
    else:
        is_ok = messagebox.askokcancel(
            title="Save Password", message=f"Details to be save: \n Website:{website} \n Email/User ID:{user_id} \n Passwords:{password} \nPress 'Ok' to save.")

        if is_ok:
            try:
                with open("password manager\data.json", "r") as data_file:
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("password manager\data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("password manager\data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                user_id_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def find_password():
    website = website_entry.get()
    try:
        with open("password manager\data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR", message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website, message=f"User ID:{email}\nPassword:{password}  ")
        else:
            messagebox.showinfo(
                title="ERROR", message=f"No data of {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
#window.minsize(width=300, height=300)
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="password manager/logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=FONT)
website_label.grid(row=1, column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

user_id_label = Label(text="Email/User ID:", font=FONT)
user_id_label.grid(row=2, column=0)

user_id_entry = Entry(width=35)
user_id_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Passwords:", font=FONT)
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

pass_generator_button = Button(
    text="Generate", command=password_generator, width=10)
pass_generator_button.grid(row=3, column=2)

add_button = Button(text="Add", command=save_password, width=36)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", command=find_password, width=10)
search_button.grid(column=2, row=1)

window.mainloop()
