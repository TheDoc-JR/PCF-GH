from ast import Delete
from tkinter import messagebox
from tkinter.font import BOLD
import pandas as pd
from tkinter import *
import mysql.connector as sqlc
from PIL import Image, ImageTk

# Establish connection to the database
cnx = sqlc.connect(
    user="root",
    password="TheDoctor3005",
    host="localhost",
    database="perez"
)

# Create a cursor
mycursor = cnx.cursor()

# Create patients table
mycursor.execute("DROP TABLE IF EXISTS ENZYMES")
mycursor.execute("DROP TABLE IF EXISTS COMPLETE_BLOOD_COUNT")
mycursor.execute("DROP TABLE IF EXISTS BIOCHEMISTRY")
mycursor.execute("DROP TABLE IF EXISTS PATIENT")
mycursor.execute("CREATE TABLE PATIENT(\n"
    "ID INT PRIMARY KEY,\n"
    "Name VARCHAR(20),\n"
    "Last_name VARCHAR(20),\n"
    "Birth_date DATE,\n"
    "Age INT,\n"
    "Sex CHAR(1))")

# Config the GUI
root = Tk()
root.title('CLINIC DATA FINDER')
root.geometry("690x291")

# Set a background image
bg = ImageTk.PhotoImage(Image.open("C:\\Users\\Gwendarling\\DarlinGit\\BG_50.jpg"))

canv = Canvas(root, width=690, height=291)
canv.pack(fill="both", expand=True)
canv.create_image(0, 0, image=bg, anchor="nw")

# Create Login frame
# Add Dr Image
log_img = Image.open("C:\\Users\\Gwendarling\\DarlinGit\\LP.jpg")
resized = log_img.resize((100,100), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized)
label = Label(root, image=new_pic, highlightcolor="red", borderwidth=0)

log_img_window = canv.create_window(75, 20, anchor="nw", window=label)

# Create login function
def logpw():
    pssw = pw.get()
    if pssw == "TheDoctor3005":
        messagebox.showinfo("","ACCESS GRANTED!")
    else: messagebox.showerror("","ACCESS DENIED\nWRONG PASSWORD")
    pw.delete(0, END)

# Add Login button
i = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Login.png")

logbtn = Button(root, image=i, borderwidth=0, command=logpw)
logbtnwindow = canv.create_window(10, 245, anchor="nw", window=logbtn)

# Create quit function
def xit():
    q = messagebox.askyesno("","Hey Doc!\nAre you sure you want to exit?")
    if q == 1:
        root.destroy()
    else: pass

# Add Quit button
q = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Exit_button.png")

qbtn = Button(root, image=q, borderwidth=0, command=xit)
qwindow = canv.create_window(180, 250, anchor="nw", window=qbtn)

# Add Password entry
pw = Entry(root, font=("Helvetica",13), bd=2)
pw.insert(0, "Enter your password")

pw_window = canv.create_window(40, 180, anchor="nw", window=pw)

# Define pw_clear function
def pw_clear(e):
    pw.delete(0, END)
    pw.config(show="*")

# Bind the entry box
pw.bind("<Button-1>", pw_clear )

# Add greeting message
greeting = Label(root, text="WELCOME DR. CAROL!", font=("Helvetica",13))
greeting_txt = canv.create_window(37, 140, anchor="nw", window=greeting)

























root.mainloop()