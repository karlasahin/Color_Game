# a game in which the user guesses what color is the 'average' of two random colors

import random
from tkinter import *
import sys
import os

def btn_Click1():   
    global y
    if y == 3:
        button1.config(text = "CORRECT")   
    else:
        button1.config(text = "INCORRECT")
    return

def btn_Click2():   
    global y
    if y == 1:
        button2.config(text = "CORRECT")
    else:
        button2.config(text = "INCORRECT")
    return

def btn_Click3():
    global y
    if y == 2:
        button3.config(text = "CORRECT") 
    else:
        button3.config(text = "INCORRECT")
    return
def btn_Restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)

root = Tk () 
root.geometry ("555x315") 
root.title ("The Color Game")


#LABELS
title = Label (root, text = "The Color Game", font = ("Calibri", 25, "bold")) 
title.grid(row = 0, column = 0)
description = Label(root, text = "If combined, what will the two colors above make?", font = ("Calibri", 12, "italic"), fg = "grey52")
description.grid(row = 4, column = 0, columnspan = 5)

#COLORS
color = []
counter = 0
while (counter <=255):
    color.append(counter)
    counter += 1
    
a = random.choice(color)
b = random.choice(color)
c = random.choice(color)

d = random.choice(color)
e = random.choice(color)
f = random.choice(color)

red = int((a+d)/2)
green = int((b+e)/2)
blue = int((c+f)/2)


#BUTTONS
original1 = Button(root, highlightbackground = '#'+'{:02x}{:02x}{:02x}'.format(a,b,c), height = 10, width = 20)
original1.grid(row = 2, column = 0, columnspan = 5)
original2 = Button(root, highlightbackground = '#' + '{:02x}{:02x}{:02x}'.format(d,e,f), height = 10, width = 20)
original2.grid(row = 2, column = 8, columnspan = 5)

#randomizing colors for answer choices 
y = random.randint(1,3)
if y ==1:
    color1 = '#' + '{:02x}{:02x}{:02x}'.format(random.choice(color),random.choice(color),random.choice(color))
    color2 = '#' + '{:02x}{:02x}{:02x}'.format(red,blue,green)
    color3 = '#' + '{:02x}{:02x}{:02x}'.format(random.choice(color),random.choice(color),random.choice(color))
    
elif y == 2:
    color2 = '#' + '{:02x}{:02x}{:02x}'.format(random.choice(color),random.choice(color),random.choice(color))
    color3 = '#' + '{:02x}{:02x}{:02x}'.format(red,blue,green)
    color1 = '#' + '{:02x}{:02x}{:02x}'.format(random.choice(color),random.choice(color),random.choice(color))
    
elif y == 3:
    color3 = '#' + '{:02x}{:02x}{:02x}'.format(random.choice(color),random.choice(color),random.choice(color))
    color1 = '#' + '{:02x}{:02x}{:02x}'.format(red,blue,green)
    color2 = '#' + '{:02x}{:02x}{:02x}'.format(random.choice(color),random.choice(color),random.choice(color))


button1 = Button(root, text="1", font = "calibri", highlightbackground = (color1), height = 4, width = 8, command = btn_Click1)
button1.grid(row = 5, column = 0) 
button2 = Button(root, text="2", font = "calibri", highlightbackground = (color2), height = 4, width = 8, command = btn_Click2)
button2.grid(row = 5, column = 1) 
button3 = Button(root, text="3", font = "calibri", highlightbackground = (color3), height = 4, width = 8, command = btn_Click3)
button3.grid(row = 5, column = 10)

restart = Button(root, text = "restart", font = "calibri", highlightbackground = "grey90", height = 1, width = 5, command = btn_Restart)
restart.grid(row = 6, column = 15)

root.mainloop()