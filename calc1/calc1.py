'''
Created on 18-Jun-2019

@author:shubh
 
'''
from tkinter import * 
def click1():
    entered_text=Label(window,text="1",bg="white",fg="black",font="calibiri 10").grid(row=0,column=10)
def click2():
     entered_text=Label(window,text="2",bg="white",fg="black",font="calibiri 10").grid(row=0,column=11)
def click3():
     entered_text=Label(window,text="3",bg="white",fg="black",font="calibiri 10").grid(row=0,column=12)
def click4():
     entered_text=Label(window,text="4",bg="white",fg="black",font="calibiri 10").grid(row=0,column=13)
def click5():
     entered_text=Label(window,text="5",bg="white",fg="black",font="calibiri 10").grid(row=0,column=14)
def click6():
     entered_text=Label(window,text="6",bg="white",fg="black",font="calibiri 10").grid(row=0,column=15)
def click7():
     entered_text=Label(window,text="7",bg="white",fg="black",font="calibiri 10").grid(row=0,column=16)
def click8():
     entered_text=Label(window,text="8",bg="white",fg="black",font="calibiri 10").grid(row=0,column=17)
def click9():
     entered_text=Label(window,text="9",bg="white",fg="black",font="calibiri 10").grid(row=0,column=18)
def click():
     entered_text=Label(window,text="0",bg="white",fg="black",font="calibiri 10").grid(row=0,column=19)
def clickC():
     Label(window,text=" ").grid(row=0,column=10)
     Label(window,text=" ").grid(row=0,column=11)
     Label(window,text=" ").grid(row=0,column=12)
     Label(window,text=" ").grid(row=0,column=13)
     Label(window,text=" ").grid(row=0,column=14)
     Label(window,text=" ").grid(row=0,column=15)
     Label(window,text=" ").grid(row=0,column=16)
     Label(window,text=" ").grid(row=0,column=17)
     Label(window,text=" ").grid(row=0,column=18)
     Label(window,text=" ").grid(row=0,column=19)
def clickS():
     Label(window,text="+",fg="black").grid(row=0,column=150)
def clickE():
    Label(window,text=" ",fg="black").grid(row=0,column=150)
window=Tk();
window.title("calculator");
window.configure(bg="white")
Label(window,text="  ",bg="white",fg="black",font="calibiri 10").grid(row=0,column=150)
Button(window,text="1",width=5,command=click1).grid(row=9,column=1)
Button(window,text="2",width=5,command=click2).grid(row=9,column=2)
Button(window,text="3",width=5,command=click3).grid(row=9,column=3)
Button(window,text="4",width=5,command=click4).grid(row=8,column=1)
Button(window,text="5",width=5,command=click5).grid(row=8,column=2)
Button(window,text="6",width=5,command=click6).grid(row=8,column=3)
Button(window,text="7",width=5,command=click7).grid(row=7,column=1)
Button(window,text="8",width=5,command=click8).grid(row=7,column=2)
Button(window,text="9",width=5,command=click9).grid(row=7,column=3)
Button(window,text="0",width=5,command=click).grid(row=10,column=2)
Button(window,text="C",width=5,command=clickC).grid(row=7,column=4)
Button(window,text="+",width=5,command=clickS).grid(row=8,column=4)
Button(window,text="=",width=5,command=clickE).grid(row=9,column=4)
window.mainloop()