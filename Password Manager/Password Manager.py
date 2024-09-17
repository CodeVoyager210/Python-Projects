from tkinter import *
from tkinter import messagebox
import string
import random
import json
from pathlib import Path
def password_generator():
    characters = string.ascii_letters + string.digits + string.punctuation
    random_password = ''.join(random.choices(characters, k=16))
    password_box.delete(0,END)
    password_box.insert(0, random_password)
def add_text():
    new_data = {
        website_box.get(): {
            "email": email_username_box.get(),
            "password": password_box.get()
        }

    }
    if len(website_box.get()) == 0 or len(email_username_box.get()) == 0:
        ok = messagebox.showerror(title='Error', message="Please make sure you haven't left any empty fields.")
    else:
        try:
            with open(saved_passwords, 'r') as data:
                dt = json.load(data)
                dt.update(new_data)
            with open(saved_passwords, 'w') as data:
                json.dump(dt, data, indent=4)
        except FileNotFoundError:
            with open(saved_passwords,'w') as new:
                json.dump(new_data,new,indent=4)

            website_box.delete(0, END)
            password_box.delete(0, END)
def search_web():
    try:
        with open(saved_passwords, 'r') as data:
            dt = json.load(data)
        website_details = dt[website_box.get()]
        website_find = messagebox.showinfo(title=website_box.get(),message=f'\nEmail: {website_details['email']} \nPassword: {website_details['password']}')
    except KeyError:
        error = messagebox.showerror(title='Error',message='Website not found or not saved')
    except FileNotFoundError:
        not_found = messagebox.showerror(title='Error',message='Please add a website')
    website_box.delete(0,END)


image = 'logo.png'
saved_passwords = Path(r'Saved Passwords\passwords.json')
window = Tk()
image_set = PhotoImage(file=image)
window.title('Password Manager')
window.minsize(600,400)
image_place = Label(image=image_set)
image_place.place(x=200,y=40)
website = Label(text='Website:',font=('Arial',12))
website.place(x=50,y=230)
website_box = Entry(font=8,width=15)
website_box.place(x=200,y=230)
email_username = Label(text='Email/Username:',font=('Arial',12))
email_username.place(x=20,y=260)
email_username_box = Entry(font=8,width=30)
email_username_box.place(x=200,y=260)
password = Label(text='Password:',font=('Arial',12))
password.place(x=41,y=290)
password_box = Entry(font=8,width=15)
password_box.place(x=200,y=290)
generate_password = Button(text='Generate Password',font=('Arial',8),command=password_generator)
generate_password.place(x=370,y=290)
add = Button(text='Add',font=('Arial',8),width=45,command=add_text)
add.place(x=200,y=320)
search = Button(text='Search',font=('Arial',8),width=15,command=search_web)
search.place(x=370,y=230)
window.mainloop()