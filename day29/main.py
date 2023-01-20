from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
# import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(END, password)
    # pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: "
                                                              f"\nEmail: {email} "
                                                              f"\npassword: {password} \nIs it ok to save?")
        if is_ok:
            new_data = {website: {
                "email": email,
                "password": password
            }}
            try:
                with open(file="data.json", mode="r") as file:
                    data = json.load(file)
                    data.update(new_data)
            except FileNotFoundError:
                data = new_data
            finally:
                with open(file="data.json", mode="w") as file:
                    json.dump(data, file, indent=4)
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)


def search():
    website_to_search = website_entry.get()

    try:
        with open(file="data.json", mode="r") as file:
            data = json.load(file)
            the_final_data = data[website_to_search.strip()]
            messagebox.showinfo(title=website_to_search, message=f"Email:{the_final_data['email']}\n"
                                                                 f" Password: {the_final_data['password']}")
    except KeyError:
        messagebox.showerror(title="Oops", message="You don't have any passwords saved for this website")

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

Label(text="Website:").grid(row=1, column=0)
Label(text="Email/Username:").grid(row=2, column=0)
Label(text="password:").grid(row=3, column=0)

website_entry = Entry()
website_entry.grid(row=1, column=1, sticky="nsew")
website_entry.focus()
email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky="nsew")
email_entry.insert(END, "muhammad@gmail.com")
password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="nsew")

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2, sticky="nsew")
add_button = Button(text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="nsew")
search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2, sticky="nsew")
window.mainloop()
