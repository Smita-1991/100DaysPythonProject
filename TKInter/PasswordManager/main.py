from random import randint, choice, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatePassword():
    letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
             't','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L',
             'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers=['0','1','2','3','4','5','6','7','8','9']
    symbols=['!','#','$','%','&','(',')','*','+']

    password_list=[]

    for _ in range(randint(4,6)):
        password_list.append(choice(letters))
    for _ in range(randint(2,3)):
        password_list.append(choice(numbers))
    for _ in range(randint(2,3)):
        password_list.append(choice(symbols))

    shuffle(password_list)
    finalPassword = ""
    for char in password_list:
        finalPassword += char

    password.insert(0, finalPassword)
    pyperclip.copy(finalPassword)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def saveInformation():
  websiteInfo=website.get()
  usernameEmail=username_email.get()
  userPassword=password.get()
  new_data={
      websiteInfo:{
      'username': usernameEmail,
      'password': userPassword
        }
     }

  if websiteInfo=="" or userPassword=="":
      messagebox.showinfo("Oops","Please dont leave any fields empty!")
  else:
        try:
          with open("Data.json","r") as file:
            data=json.load(file)
            print(data)
        except FileNotFoundError:
            with open("Data.json","w") as file:
                json.dump(new_data,file,indent=4)
        else:
          data.update(new_data)
          with open("Data.json","w") as file:
              json.dump(data,file,indent=4)
        finally:
            website.delete(0, END)
            password.delete(0, END)


# ---------------------------- SEARCH PASSWORD --------------------------- #
def searchPassword():
    websiteInfo=website.get()
    try:
        with open("Data.json","r") as file:
            data=json.load(file)
    except FileNotFoundError:
        messagebox.showinfo("Error","No Data File Found")
    else:
        if websiteInfo in data:
            username=data[websiteInfo]['username']
            password=data[websiteInfo]['password']
            messagebox.showinfo(websiteInfo,f"Username: {username}\nPassword: {password}")
        else:
            messagebox.showinfo("Error",f"No details for {websiteInfo} exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=10, pady=10)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=1)

website_label = Label(text="Website:")
website_label.grid(column=0, row=2)
userName_label = Label(text="Email/Username:")
userName_label.grid(column=0, row=3)
password_label = Label(text="Password:")
password_label.grid(column=0, row=4)

website = Entry(width=40)
website.grid(column=1, row=2, sticky=EW)
username_email = Entry(width=40)
username_email.insert(0,"autismita5@gmail.com")
username_email.grid(column=1, row=3, columnspan=2,sticky=EW)
password = Entry(width=21)
password.grid(column=1, row=4,sticky=EW)


addButton = Button(text="Add", width=40,command=saveInformation)
addButton.grid(column=1, row=5, columnspan=2,sticky=EW)
searchButton=Button(text="Search", width=15,command=searchPassword)
searchButton.grid(column=2, row=2)
generatePasswordButton = Button(text="Generate Password:",command=generatePassword)
generatePasswordButton.grid(column=2, row=4)

window.mainloop()
