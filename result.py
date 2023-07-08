from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import tkinter as tk 
from tkinter import filedialog

import time

from tkinter import Tk, Label, Entry, Toplevel, Canvas

from PIL import Image, ImageDraw, ImageTk, ImageFont
image = Image.open('SC.jpg')


import cv2
import numpy as np
import time


########################################################################################    

global i
i = 0
def take_choice():

    color = "#fffff0"

    CHOICE= Tk()
    CHOICE.geometry("1300x600+30+30")
    CHOICE.configure(background = color)
    
    photoimage = ImageTk.PhotoImage(image)
    Label(CHOICE, image=photoimage).place(x=0,y=0)

    label2 = Label(CHOICE, text="Beacon Technology")
    label2.configure(background="#ffffFf")
    label2.config(font=("Courier", 30))
    label2.place(x = 150,y=20,height=40, width=1000)

    label2 = Label(CHOICE, text="Class Room 1")
    label2.configure(background="#ffffFf")
    label2.config(font=("Courier", 15))
    label2.place(x = 750,y=150,height=40, width=300)

    label2 = Label(CHOICE, text="Class Room 2")
    label2.configure(background="#ffffFf")
    label2.config(font=("Courier", 15))
    label2.place(x = 750,y=250,height=40, width=300)

    label2 = Label(CHOICE, text="Class Room 3")
    label2.configure(background="#ffffFf")
    label2.config(font=("Courier", 15))
    label2.place(x = 750,y=350,height=40, width=300)


    label2 = Label(CHOICE, text="user 2")
    label2.configure(background="#ffffFf")
    label2.config(font=("Courier", 15))
    label2.place(x = 1050,y=150,height=40, width=200)


    label2 = Label(CHOICE, text="user 1")
    label2.configure(background="#ffffFf")
    label2.config(font=("Courier", 15))
    label2.place(x = 1050,y=250,height=40, width=200)

    label2 = Label(CHOICE, text="user 3")
    label2.configure(background="#ffffFf")
    label2.config(font=("Courier", 15))
    label2.place(x = 1050,y=350,height=40, width=200)


    CHOICE.mainloop()

