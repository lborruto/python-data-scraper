import sys
import os
from tkinter import *
import graph1
import graph2
import graph3

window=Tk()

window.title("Python Data Scraper")
window.geometry('500x70')

def run():
    graph1.draw()

def run2():
    graph2.draw2()

def run3():
    graph3.draw3()

def Close():
    window.destroy()

btn = Button(window, text="GPU Usage", bg="black", fg="white",command=run)
btn.grid(column=0, row=1)

btn2 = Button(window, text="Cryptocurrency Value", bg="black", fg="white",command=run2)
btn2.grid(column=1, row=1)

btn3 = Button(window, text="Offer & Demand", bg="black", fg="white",command=run3)
btn3.grid(column=2, row=1)

exit_button = Button(window, text="Exit", command=window.destroy)
exit_button.grid(column=15, row=7)

window.mainloop()