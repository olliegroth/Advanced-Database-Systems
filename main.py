from tkinter import *
from tkinter import messagebox
from functools import partial
import sqlite3

window = Tk()
window.title("Assessment")
window.geometry("400x250")

def validateLogin(usernameToValidate, passwordToValidate):
    connection_obj = sqlite3.connect("Online Shop (Example Database).db")
    cursor_obj = connection_obj.cursor()
    value_username = usernameToValidate.get()
    value_password = str(passwordToValidate.get())
    cursor_obj.execute(
        "SELECT * FROM login_details WHERE User_Login='" + value_username + "'" + " AND User_password='" + value_password + "'")
    output1 = cursor_obj.fetchall()
    if len(output1) > 0:
        print("hi")
        messagebox.showinfo("showinfo", "correct login and password")
    else:
        print("no")
        messagebox.showwarning("Warning", "Incorrect login or password")
    for row in output1:
        print(row)
    connection_obj.commit()

def register_customer(usernameToRegister, passwordToRegister):
    connection_obj = sqlite3.connect("Online Shop (Example Database).db")
    cursor_obj = connection_obj.cursor()
    value_username = usernameToRegister.get()
    value_password = str(passwordToRegister.get())
    if len(value_password) > 5:
        cursor_obj.execute("insert into login_details values('"+value_username+"', '"+value_password+"')")
        messagebox.showinfo("showinfo", "user registered")
    else:
        messagebox.showwarning("Warning", "Incorrect login or password")
    connection_obj.commit()

Label(window, text="User Name").grid(row=0, column=0)
username = StringVar()
Entry(window, textvariable=username).grid(row=0, column=1)

Label(window,text="Password").grid(row=1, column=0)
password = StringVar()
Entry(window, textvariable=password, show='*').grid(row=1, column=1)

validateLogin = partial(validateLogin, username, password)
Button(window, text="Login", command=validateLogin).place(x=65, y=45)

register_customer = partial(register_customer, username, password)
Button(window, text="Register", command=register_customer).place(x=120, y=45)

mainloop()