"""
Author: Elijah Morishita
elmorishita@dmacc.edu
10/19/2020
This program creates a GUI using the tkinter imported module.
"""
import tkinter


def check1():
    label.config(text="Good Choice!")


def check2():
    label.config(text="Better Choice!!")


def check3():
    label.config(text="Great Choice!!!")


def check4():
    label.config(text="FANTASTIC CHOICE!!!!")


m = tkinter.Tk()  # where m is the name of the main window object

m.title("Favorite Meal")  # The title of the box
label = tkinter.Label(m, text="Waiting")
label.grid(row=5)
var1 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Breakfast", variable=var1, command=check1).grid(row=1, sticky="W")
var2 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Second Breakfast", variable=var2, command=check2).grid(row=2, sticky="W")
var3 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Lunch", variable=var3, command=check3).grid(row=3, sticky="W")
var4 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Dinner", variable=var4, command=check4).grid(row=4, sticky="W")
exit_button = tkinter.Button(m, text="Exit", width=35, command=m.destroy).grid(row=6)

m.mainloop()  # infinite loop that waits for events to happen
