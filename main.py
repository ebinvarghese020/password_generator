from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


def generate():
    # Password Generator
    password_entry.delete(0, END)
    if len(password_entry.get()) == 0:
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                   'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password_list1 = [random.choice(letters) for n in range(random.randint(8, 10))]

        password_list2 = [random.choice(symbols) for n in range(random.randint(2, 4))]

        password_list3 = [random.choice(numbers) for n in range(random.randint(2, 4))]

        password_list = password_list1 + password_list2 + password_list3

        random.shuffle(password_list)

        new_password = "".join(password_list)

        password_entry.insert(0, new_password)
        pyperclip.copy(new_password)


def save_values():
    sites = site_entry.get()
    emails = email_entry.get()
    passwords = password_entry.get()

    new_data = {
        sites: {
            "email": emails,
            "password": passwords
        }
    }

    if len(sites) == 0 or len(emails) == 0 or len(passwords) == 0:
        messagebox.showerror(title="Blank Entries", message="Please make sure to fill all the entries")
    else:
        message = messagebox.askokcancel(title=sites,
                                         message=f"The details saved are Website : {sites} \n email : {emails}\n Password : {passwords}\n READY TO SAVE ?")

        file_data = {}
        if message:
            try:
                with open("data.json", "r") as file:
                    file_data = json.load(file)
                    file_data.update(new_data)

                with open("data.json", "w") as file:
                    json.dump(file_data, file, indent=4)

            except  FileNotFoundError:
                with open("data.json", "w") as file:
                    print(new_data)
                    json.dump(new_data, file, indent=4)

            except  JSONDecodeError:
                with open("data.json", "w") as file:
                    print(new_data)
                    json.dump(new_data, file, indent=4)
            finally:
                site_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


def search():
    email_entry.delete(0, END)
    password_entry.delete(0, END)
    try:
        with open("data.json") as file:
            data = json.load(file)
            if site_entry.get() in data:
                email1 = data[site_entry.get()]["email"]
                password1 = data[site_entry.get()]["password"]
                messagebox.showinfo("Password", f"email : {email1} \n password : {password1}")
            else:
                messagebox.showerror("Oops", "No such data is stored!")

    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="No such file/ value exist!")


window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30, bg="white")

canvas = Canvas(height=240, width=200, bg="white", highlightthickness=0)
photo = PhotoImage(file="image.png")
canvas.create_image(100, 110, image=photo)
canvas.grid(row=0, column=0, rowspan=3)

site = Label(text="Website : ", bg="white", font=("Ariel", 12))
site.grid(row=0, column=2)

site_entry = Entry(width=40, borderwidth=2, fg="black")
site_entry.focus()
site_entry.grid(row=0, column=3)

email = Label(text="Email/ID : ", bg="white", font=("Ariel", 12))
email.grid(row=1, column=2)

email_entry = Entry(width=40, borderwidth=2, fg="black")
email_entry.grid(row=1, column=3)

password = Label(text="Password : ", bg="white", font=("Ariel", 12))
password.grid(row=2, column=2)

password_entry = Entry(width=40, borderwidth=2, fg="black")
password_entry.grid(row=2, column=3)

generate_button = Button(text="Generate Password", bg="white", highlightthickness=0, command=generate)
generate_button.grid(row=3, column=2)

search_button = Button(text="Search", bg="white", highlightthickness=0, command=search)
search_button.grid(row=3, column=0)

save_button = Button(text="Save", bg="white", highlightthickness=0, command=save_values)
save_button.grid(row=3, column=3)

window.mainloop()
