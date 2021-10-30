'''
    Mini project number 1 - Basic GUI Input Form
    Made by @bh.divyansh (version 1.0 on 30th Oct 2021)
'''
# Importing Tkinter for usage and defining the root
from tkinter import *
root = Tk()
# Basic Geometry of window
root.title("@bh.divyansh's Band Name Generator")
root.geometry("600x450") #window default size
root.maxsize(700,550) #max size of window
root.minsize(500,350) #min size of window
# Defining the funcion which will do all the work
def getvals():
    print(f"The entered name is {nameentry.get()}.")
    print(f"The entered phone is {phoneentry.get()}.")
    print(f"The entered email is {emailentry.get()}.")
    print(f"The entered passkey is {passentry.get()}.")
# Defining UI Elements
headinglabel = Label(root,text="Welcome to Simple GUI Form",font="Arial 20 bold").grid(row=0,column=1)
Label(root,text="Name: ").grid(row=1,column=0)
Label(root,text="Phone Number: ").grid(row=2,column=0)
Label(root,text="Email: ").grid(row=3,column=0)
Label(root,text="Passkey: ").grid(row=4,column=0)
# Defining Value-holding variables and their types
nameentry = StringVar()
phoneentry = StringVar()
emailentry = StringVar()
passentry = StringVar()
# Creating entry-boxes in the grid
Entry(root,textvariable=nameentry).grid(row=1,column=1)
Entry(root,textvariable=phoneentry).grid(row=2,column=1)
Entry(root,textvariable=emailentry).grid(row=3,column=1)
Entry(root,textvariable=passentry).grid(row=4,column=1)
#Creating a submit button that calls the function above
Button(root,text="SUBMIT",font="arial 17 bold",fg='red',bg='yellow',command=getvals).grid(column=1)
# finishing tkinter's syntax
root.mainloop()
