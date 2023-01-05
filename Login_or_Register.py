# Login or Sign up using tkinter

from tkinter import *
import csv
from tkinter import messagebox
import pandas
import numpy as np


def Register_User():
  #getting datas from user
  firstname_info = firstname.get()
  lastname_info = lastname.get()
  email_info = email.get()
  age_info = age.get()
  username_info = username.get()
  password_info = password.get()

  #storing datas of users in csv formate
  with open("Personal.csv",mode="a",newline="") as f:
    thewriter = csv.writer(f)
    thewriter.writerow([firstname_info,lastname_info,email_info,age_info,username_info,password_info])
    f.close()

  #clearing entring boxes after storing the data
  first_name_entry.delete(0,END)
  last_name_entry.delete(0,END)
  email_entry.delete(0,END)
  age_entry.delete(0,END)
  username_entry.delete(0,END)
  password_entry.delete(0,END)

  lb=Label(reg_page,text="Registration Successful",fg="green").place(x=70,y=210)
  lb.delete(0,END)
  
def Register():
  global reg_page
  reg_page = Toplevel(homepage)
  reg_page.title("Register")
  reg_page.geometry("400x400")
  reg_page.config(bg="#F4A460")
# Label column
  global username
  global password
  global firstname
  global lastname
  global email
  global age
  
# Entry column making as global 
  global first_name_entry
  global last_name_entry
  global email_entry
  global age_entry
  global username_entry
  global password_entry
  
  username = StringVar()
  password = StringVar()
  firstname = StringVar()
  lastname = StringVar()
  email = StringVar()
  age = StringVar()

  
  Label(reg_page,text="Fill your personal Details",fg="red",bg="#F4A460",font=12).grid(row=0,column=0)
  #personal details alone
  Label(reg_page,text="First Name",bg="#F4A460").grid(row=1,column=0)
  first_name_entry = Entry(reg_page,textvariable=firstname)
  first_name_entry.grid(row=1,column=1)
  Label(reg_page,text="Last Name",bg="#F4A460").grid(row=2,column=0)
  last_name_entry = Entry(reg_page,textvariable=lastname)
  last_name_entry.grid(row=2,column=1)
  Label(reg_page,text="Email ID",bg="#F4A460").grid(row=3,column=0)
  email_entry = Entry(reg_page,textvariable=email)
  email_entry.grid(row=3,column=1)
  Label(reg_page,text="Age",bg="#F4A460").grid(row=4,column=0)
  age_entry = Entry(reg_page,textvariable=age)
  age_entry.grid(row=4,column=1)
  #used for login purpose
  Label(reg_page,text="UserName",bg="#F4A460").grid(row=5,column=0)
  username_entry = Entry(reg_page,textvariable=username)
  username_entry.grid(row=5,column=1)
  Label(reg_page,text="Password",bg="#F4A460").grid(row=6,column=0)
  password_entry = Entry(reg_page,textvariable=password)
  password_entry.grid(row=6,column=1)
  reg_button=Button(reg_page,text="Register",width="20",height="2",command=Register_User,activebackground="#FF7F50")
  reg_button.place(x=80,y=160)

def Login_user(username_verify,password_verify):
  #clearing the fields once entered
  username_entry1.delete(0,END)
  password_entry1.delete(0,END)
  
  #reading the csv file using pandas
  df = pandas.read_csv('Personal.csv')
  # converting pandas to numpy array for accessing the elements
  arr=df.to_numpy()
  #print(arr)
  #verify only the username and password are correct
  if (np.where(arr==username_verify)):
    if(np.where(arr==password_verify)):
      messagebox.showinfo("Login", "Login successful")
    else:
      messagebox.showinfo("Incorrect","Enter the Correct password")
  else:
    messagebox.showinfo("Incorrect","Enter the Correct Username")
    
def Login():
  global login_page
  login_page = Toplevel(homepage)
  login_page.title("Login")
  login_page.geometry("400x400")
  login_page.config(bg="#F4A460")
  
  Label(login_page,text="Enter username and password to login",fg="red",bg="#F4A460",font=12).place(x=10,y=10)

  global username_verify
  global password_verify
  global username_entry1
  global password_entry1

  username_verify = StringVar()
  password_verify = StringVar()

  Label(login_page,text="UserName",bg="#F4A460").place(x=20,y=50)
  username_entry1 = Entry(login_page,textvariable=username_verify)
  username_entry1.place(x=100,y=50)
  
  Label(login_page,text="Password",bg="#F4A460").place(x=20,y=80)
  password_entry1 = Entry(login_page,textvariable=password_verify)
  password_entry1.place(x=100,y=80)

  logbt = Button(login_page,text="Log in",command=lambda:Login_user(username_entry1.get(),password_entry1.get()))
  logbt.place(x=150,y=110)
  
  
#Creating the main window
def main_screen():
  global homepage
  homepage = Tk()
  homepage.title("Homepage")
  homepage.geometry("400x400")
  homepage.config(bg="grey")
  Label(text="Login or Register",bg="#F4A460",width="200",height="2",font=("Bold",13)).pack()
  #Login button
  Button(text="Login",height="2",width="20",command=Login,font=10,bg="white",activebackground="red",relief=FLAT).place(x=70,y=90)
  #Register Button
  Button(text="Register",height="2",width="20",command=Register,font=10,bg="white",activebackground="red").place(x=70,y=190)
  homepage.mainloop()

main_screen()
