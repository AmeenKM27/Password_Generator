import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

def chargen(list,num,a,b):
    for i in range(0,num):
        list.append(chr(random.randint(a,b)))

def passgen(list,numu,numl,numn,nums):
    chargen(list,numu,65,90)
    chargen(list,numl,97,122)
    chargen(list,numn,48,57)
    chargen(list,nums,33,47)

def shuffle(list):
    random.shuffle(list)

def clicked():
    global el,eu,es,en,numl,numn,nums,numu
    numu=int(eu.get())
    numl=int(el.get())
    numn=int(en.get())
    nums=int(es.get())
    password=[]
    passgen(password,numu,numl,numn,nums)
    shuffle(password)
    d=''
    for i in range(len(password)):
       d+=password[i]
    messagebox.showinfo("New Password",d)

window=Tk()
window.title("Password Generator")
tframe=Frame(window).pack()
bframe=Frame(window).pack()
label=Label(tframe,text="Password Generator",font=("Century Gothic",30),fg='Sky Blue')
label.pack()

l2=Label(tframe,text="Enter the number of upper case characters you want in your password").pack()
eu=Entry(tframe,bg='white')
eu.pack()

l3=Label(tframe,text="Enter the number of lower case characters you want in your password").pack()
el=Entry(tframe,bg='white')
el.pack()

l4=Label(tframe,text="Enter the number of numerical characters you want in your password").pack()
en=Entry(tframe,bg='white')
en.pack()

l5=Label(tframe,text="Enter the number of special characters you want in your password").pack()
es=Entry(tframe,bg='white')
es.pack()

bt=Button(bframe,text="Click Here to Generate the new password",font=("Arial",15),bg='black',fg='white',command=clicked).pack()

window.mainloop()


