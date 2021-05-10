from tkinter import*
from tkinter import ttk
def fun1():
    import domains
def fun2():
    import logincode 

rw =Tk()
btn1=ttk.Button(rw,text="AdminLogin")
btn1.pack()
btn1.config(command=fun1)
btn2=ttk.Button(rw,text="UserLogin")
btn2.pack()
btn2.config(command=fun2)
