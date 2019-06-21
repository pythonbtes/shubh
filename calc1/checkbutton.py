'''
Created on 19-Jun-2019

@author: shubh
'''
import tkinter as tk

window=tk.Tk();
window.title("checkbutton")
window.configure(background="white")

var1= tk.IntVar()
var2= tk.IntVar()
var3= tk.IntVar()
var4= tk.IntVar()
def click1():    
    if var1.get()==1:
        window.configure(background="red") 
    elif var2.get()==1 :
        window.configure(background="pink")
    elif  var3.get()==1:
        window.configure(background="blue")
    elif  var4.get()==1:
        window.configure(background="green")
    else:
        window.configure(background="white")
tk.Checkbutton(window,text="red",bg="white",fg="black",width=50,font="none 10",command=click1,variable=var1).grid(row=0,column=50)
tk.Checkbutton(window,text="pink",bg="white",fg="black",width=50,font="none 10",command=click1,variable=var2).grid(row=50,column=50)
tk.Checkbutton(window,text="blue",bg="white",fg="black",width=50,font="none 10",command=click1,variable=var3).grid(row=25,column=10)
tk.Checkbutton(window,text="green",bg="white",fg="black",width=50,font="none 10",command=click1,variable=var4).grid(row=25,column=90)
window.mainloop()