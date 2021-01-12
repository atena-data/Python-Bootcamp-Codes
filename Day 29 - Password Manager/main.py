from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
# import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    new_password = "".join(password_list)
    password_input.insert(0, new_password)
    # # copy password to the clipboard
    # pyperclip.copy(new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_save = website_input.get()
    email_save = user_name_input.get()
    password_save = password_input.get()
    new_data = {
        website_save: {
            "email": email_save,
            "password": password_save,
        }
    }
    if len(website_save) == 0 or len(password_save) == 0:
        messagebox.showwarning(title="OOPS", message="Please don't leave any field empty!")
    else:
        try:
            with open("data.json", "r") as data:
                # read old data
                data_json = json.load(data)
        except FileNotFoundError:
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent=4)
        else:
            # update old data with new data
            data_json.update(new_data)
            with open("data.json", "w") as data:
                # save updated data
                json.dump(data_json, data, indent=4)
        finally:
            # delete all the data entries from the app
            website_input.delete(first=0, last=END)
            password_input.delete(first=0, last=END)

# ---------------------------- SEARCH FILE ------------------------------- #


def search_file():
    web = website_input.get()
    try:
        with open("data.json", "r") as data:
            data_json = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Info", message="You don't have any saved passwords.")
    else:
        if web in data_json:
            mail = data_json[web]["email"]
            psswrd = data_json[web]["password"]
            messagebox.showinfo(title="Info", message=f"Email: {mail}\n\nPassword: {psswrd}")
        else:
            messagebox.showinfo(title="Info", message=f"No details for {web} exists.")
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# set canvas
canvas = Canvas(height=200, width=200, highlightthickness=0, bg="white")
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# set labels
website = Label(text="Website:", bg="white")
website.grid(column=0, row=1)

User_name = Label(text="Email/Username:", bg="white")
User_name.grid(column=0, row=2)

password = Label(text="Password:", bg="white")
password.grid(column=0, row=3)

# set buttons
generate_password = Button(text="Generate Password", bg="white", width=15, command=generate_password)
generate_password.grid(column=2, row=3)

search_button = Button(text="Search", bg="white", width=15, command=search_file)
search_button.grid(column=2, row=1)

add_button = Button(text="Add", width=44, bg="white", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky=W)

# set an input field
website_input = Entry(width=32)
website_input.grid(column=1, row=1, sticky=W)
website_input.focus()

user_name_input = Entry(width=52)
user_name_input.grid(column=1, row=2, columnspan=2, sticky=W)
user_name_input.insert(0, "@gmail.com")

password_input = Entry(width=32)
password_input.grid(column=1, row=3, sticky=W)

window.mainloop()
