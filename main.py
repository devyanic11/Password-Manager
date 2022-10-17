from tkinter import *
from tkinter import messagebox
from password_generator import Password
import json

YELLOW = "#ffe9a0"
GREEN = "#367e18"
FONT_NAME = "Courier"
# ---------------------------- SEARCH ------------------------------- #

def search():
    website = website_entry.get()
    with open("data.json", "r") as data_file:
        try:
            data = json.load(data_file)
            saved_email = data[website]["email"]
            saved_password = data[website]["password"]
        except KeyError:
            messagebox.showerror(title="Error", message="No such website data saved")
        except json.decoder.JSONDecodeError:
            messagebox.showerror(title="Error", message="No such website data saved")
        else:
            messagebox.showinfo(title=website, message=f"Email: {saved_email}\nPassword: {saved_password}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    new_password = Password()
    generated_password = new_password.password_generator()
    password_entry.insert(0, generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: "
                                                      f"{email}\nPassword: {password}")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    #Reading old data
                    data = json.load(data_file)
            except json.decoder.JSONDecodeError:
                with open("data.json","w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                #Update data
                data.upate(new_data)
                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(new_data, data_file, indent=4)

            finally:
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)
                    email_entry.delete(0, END)
                    email_entry.insert(0, "devyanichavan110@gmail.com")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, bg=YELLOW)

canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website: ", bg=YELLOW, font=(FONT_NAME, 10, "bold"))
website_label.grid(row=1, column=0, sticky="e")
email_label = Label(text="Email/Username: ", bg=YELLOW, font=(FONT_NAME, 10, "bold"))
email_label.grid(row=2, column=0, sticky="e")
password_label = Label(text="Password: ", bg=YELLOW, font=(FONT_NAME, 10, "bold"))
password_label.grid(row=3, column=0, sticky="e")

# Entries
website_entry = Entry(width=25)
website_entry.grid(row=1, column=1,sticky="e", padx=5, pady=4)
website_entry.focus()
email_entry = Entry(width=44)
email_entry.grid(row=2, column=1, columnspan=2, sticky="e", padx=2, pady=4)
email_entry.insert(0, "devyanichavan110@gmail.com")
password_entry = Entry(width=25)
password_entry.grid(row=3, column=1, sticky='e', padx=5, pady=4)

#Buttons
generate_password_button = Button(text="Generate Password", bg=GREEN, command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=37, bg=GREEN, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="e", pady=4)
search_button = Button(text="Search", bg=GREEN, width=14, command=search)
search_button.grid(column=2, row=1, sticky="e")





window.mainloop()