import tkinter as tk
from tkinter import ttk,messagebox
import mysql.connector
from tkinter import *


def Delete(event):
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select['emp_id'])
    e2.insert(0,select['emp_name'])
    e3.insert(0,select['emp_session'])
    e4.insert(0,select['emp_attendence'])
    e5.insert(0,select['emp_status'])

    
def add():
    emp_id = e1.get()
    emp_name = e2.get()
    emp_session = e3.get()
    emp_attendence = e4.get()
    emp_status = e5.get()

    mysqldb = mysql.connector.connect(host = "localhost",user = "root",password = "root",database="employee_status")
    mycursor =  mysqldb.cursor()
    
    try:
        sql = "INSERT INTO record(emp_id,emp_name,emp_session,emp_attendence,emp_status) VALUES(%s,%s,%s,%s,%s)"
        val = (emp_id,emp_name,emp_session,emp_attendence,emp_status)
        mycursor.execute(sql,val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information","Record inserted successfully")
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()
def update():
    emp_id       = e1.get()
    emp_name     = e2.get()
    emp_session  = e3.get()
    emp_attendence = e4.get()
    emp_status = e5.get()

    
    mysqldb = mysql.connector.connect(host = "localhost",user = "root",password = "root",database="Employee_status")
    mycursor =  mysqldb.cursor()

    
    try:
        sql = "update record set emp_name = %s,emp_session=%s,emp_attendence=%s,emp_status=%s where emp_id=%s "
        val = (emp_name,emp_session ,emp_attendence,emp_status,emp_id)
        mycursor.execute(sql,val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information","Record inserted successfully")
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def delete():
    emp_id = e1.get()
    mysqldb = mysql.connector.connect(host = "localhost",user = "root",password ="root",database="Employee_status")
    mycursor =  mysqldb.cursor()
    
    try:
        #sql = "delete from emp where emp_id='%s'
        val =(emp_id)
        print(emp_id)
        print(e1.get())
        print(val)
        print(type(val))
        mycursor.execute(f"delete from record where emp_id='{val}'")
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information","Record Deleted  successfully")
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

def show():
    mysqldb = mysql.connector.connect(host = "localhost",user = "root",password="root",database="Employee_status")
    mycursor =  mysqldb.cursor()
   
    mycursor.execute("SELECT emp_id,emp_name,emp_session ,emp_attendence,emp_status FROM record")                        
    records = mycursor.fetchall()
    print(records)
    for i,(emp_id,emp_name,emp_session ,emp_attendence,emp_status) in enumerate (records,start=1):
        listBox.insert("","end",values = (emp_id,emp_name,emp_session ,emp_attendence,emp_status))
        mysqldb.close()
                            
root = Tk()

root.geometry("800x500")
global e1
global e2
global e3
global e4
global e5
                            
tk.Label(root, text = "Employee_Report",fg = "black",font = (None,30)).place(x=400,y=5)
tk.Label(root, text = "emp_Id").place(x=10,y=10)
Label(root, text = "emp_Name").place(x=10,y=40)
Label(root, text = "emp_session").place(x=10,y=70)
Label(root, text = "emp_attendence").place(x=10,y=100)
Label(root, text = "emp_status").place(x=10,y=140)

e1 = Entry(root)
e1.place(x=140,y=10)

e2 = Entry(root)
e2.place(x=140,y=40)

e3 = Entry(root)
e3.place(x=140,y=70)

e4 = Entry(root)
e4.place(x=140,y=100)

e5 = Entry(root)
e5.place(x=140,y=140)




     
Button(root, text = "add",command = add,height=2,width=13).place(x=30,y=180)

Button(root, text = "update",command = update,height=2,width=13).place(x=140,y=180)

Button(root, text = "Delete",command = delete,height=2,width=13).place(x=250,y=180)


cols = ('emp_id','emp_name','emp_session' ,'emp_attendence','emp_status')
listBox = ttk.Treeview(root,columns = cols,show = 'headings')


for col in cols:
    listBox.heading(col,text=col)
    listBox.grid(row=1,column=0,columnspan=2)
    listBox.place(x=20,y=250)

show()
listBox.bind('<Double-Button-1>',Delete)

root.mainloop()

