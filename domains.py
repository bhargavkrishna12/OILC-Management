from tkinter import*
from tkinter import ttk
import pymysql
from tkinter import messagebox
import admin
class employee:
    def __init__(self,root):
        self.root = root
        self.root.title("OILC-Management system")
        self.root.geometry("1350x700+0+0")
        
        title = Label(self.root,text="Employee management system",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg='lightblue',fg='white')
        title.pack(side=TOP,fill=X)

        self.emp_id_var = StringVar()
        self.Name_var = StringVar()
        self.sessions_var = StringVar()
        self.exercises_var = StringVar()
        self.status_var = StringVar()
        self.gender_var = StringVar()
        self.Tech_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        
#--------------------------------------Manage Frame---------------------------------------------------------------#
        
        manage_frame = Frame(self.root,bd=4,relief=RIDGE)
        manage_frame.place(x=20,y=100,width=480,height=800)

        m_title = Label(manage_frame,text="Manage employees",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan = 2,pady=20)
        
        lbl_roll = Label(manage_frame,text="emp_id",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column =0,pady=10,padx=20,sticky="w")


        txt_Roll = Entry(manage_frame,textvariable=self.emp_id_var,font=("times new roman",20,"bold"))
        txt_Roll.grid(row=1,column =1,pady=10,padx=20,sticky="w")

        lbl_roll = Label(manage_frame,text="Name",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=2,column =0,pady=10,padx=20,sticky="w")

        txt_Roll = Entry(manage_frame,textvariable=self.Name_var,font=("times new roman",20,"bold"))
        txt_Roll.grid(row=2,column =1,pady=10,padx=20,sticky="w")

        lbl_roll = Label(manage_frame,text="sessions",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=3,column =0,pady=10,padx=20,sticky="w")

        txt_Roll = Entry(manage_frame,textvariable=self.sessions_var,font=("times new roman",20,"bold"))
        txt_Roll.grid(row=3,column =1,pady=10,padx=20,sticky="w")

        lbl_roll = Label(manage_frame,text="exercises",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=4,column =0,pady=10,padx=20,sticky="w")

        txt_Roll = Entry(manage_frame,textvariable=self.exercises_var,font=("times new roman",20,"bold"))
        txt_Roll.grid(row=4,column =1,pady=10,padx=20,sticky="w")

        lbl_roll = Label(manage_frame,text="status",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=5,column =0,pady=10,padx=20,sticky="w")

        txt_Roll = Entry(manage_frame,textvariable=self.status_var,font=("times new roman",20,"bold"))
        txt_Roll.grid(row=5,column =1,pady=10,padx=20,sticky="w")
        
        lbl_roll = Label(manage_frame,text="gender",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=6,column =0,pady=10,padx=20,sticky="w")

        txt_Roll = Entry(manage_frame,textvariable=self.gender_var,font=("times new roman",20,"bold"))
        txt_Roll.grid(row=6,column =1,pady=10,padx=20,sticky="w")

        lbl_roll = Label(manage_frame,text="Tech",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=7,column =0,pady=10,padx=20,sticky="w")

        txt_Roll = Entry(manage_frame,textvariable=self.Tech_var,font=("times new roman",20,"bold"))
        txt_Roll.grid(row=7,column =1,pady=10,padx=20,sticky="w")
        
#----------------------------------------------ButtonFrame-------------------------------------------------------
        btn_frame = Frame(manage_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=20,y=500,width=420)

        Addbtn = Button(btn_frame,text="Add",width=10,command=self.add_employees).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_frame,text="Update",command=self.update,width=10).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(btn_frame,text="Delete",command=self.delete,width=10).grid(row=0,column=2,padx=10,pady=10)
        clearbtn=Button(btn_frame,text="Clear",command = self.clear,width=10).grid(row=0,column=3,padx=10,pady=10)
        #btn2=Button(Frame_login,text="Logout",command=self.loginform,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
            

        
#--------------------------------------DetailFrame---------------------------------------------------------------     

        detail_frame = Frame(self.root,bd=4,relief=RIDGE)
        detail_frame.place(x=600,y=100,width=700,height=560)

        lbl_search=Label(detail_frame,text="Search by",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search = ttk.Combobox(detail_frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state="readonly")
        combo_search['values'] = ("emp_id","Name","Tech")
        combo_search.grid(row=0,column =1,padx=20,pady=10)
        
        txt_search = Entry(detail_frame,textvariable=self.search_txt,width=18,font=("times new roman",10,"bold"))
        txt_search.grid(row=0,column =2,pady=10,padx=20,sticky="w")

        searchbtn=Button(detail_frame,text="Search",command=self.search_data,width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(detail_frame,text="Show All",command=self.fetch_data,width=10,pady=5).grid(row=0,column=4,padx=10,pady=10)

#============================= Table Frame ===========================================================================================

        Table_frame = Frame(detail_frame,bd=4,relief=RIDGE)
        Table_frame.place(x=10,y=70,width=670,height=470)
        scroll_x = Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_frame,orient=VERTICAL)
        self.employee_table = ttk.Treeview(Table_frame,columns=("emp_id","Name","sessions","exercises","status","gender","Tech"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command = self.employee_table.xview)
        scroll_y.config(command = self.employee_table.yview)
        self.employee_table.heading("emp_id",text="emp_id")
        self.employee_table.heading("Name",text="Name")
        self.employee_table.heading("sessions",text="sessions")
        self.employee_table.heading("exercises",text="exercises")
        self.employee_table.heading("status",text="status")
        self.employee_table.heading("gender",text="gender")
        self.employee_table.heading("Tech",text="Tech")
        self.employee_table['show'] = "headings"
        self.employee_table.column("emp_id",width=100)
        self.employee_table.column("Name",width=100)
        self.employee_table.column("sessions",width=100)
        self.employee_table.column("exercises",width=100)
        self.employee_table.column("status",width=100)
        self.employee_table.column("gender",width=100)
        self.employee_table.column("Tech",width=100)
        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        
        self.fetch_data()
        
    def add_employees(self):
        con = pymysql.connect(host="localhost",user="root",password="root",database="OILC")
        cur = con.cursor()
        cur.execute("insert into employees values(%s,%s,%s,%s,%s,%s,%s)",(self.emp_id_var.get(),self.Name_var.get(),self.sessions_var.get(),self.exercises_var.get(),self.status_var.get(),self.gender_var.get(),self.Tech_var.get()))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("success","Record inserted successfully")
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="root",database="oilc")
        cur=con.cursor()
        cur.execute("select * from employees")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                self.employee_table.insert('',END,values=row)
            con.commit()
        con.close()   
    def clear(self):
        self.emp_id_var.set("")
        self.Name_var.set("")
        self.sessions_var.set("")
        self.exercises_var.set("")
        self.status_var.set("")
        self.gender_var.set("")
        self.Tech_var.set("")     
    def get_cursor(self,ev):
        cursor_row = self.employee_table.focus()
        contents = self.employee_table.item(cursor_row)
        row = contents['values']
       
        self.emp_id_var.set(row[0])
        self.Name_var.set(row[1])
        self.sessions_var.set(row[2])
        self.exercises_var.set(row[3])
        self.status_var.set(row[4])
        self.gender_var.set(row[5])
        self.Tech_var.set(row[6])
    def update(self):
        con = pymysql.connect(host="localhost",user="root",password="root",database="OILC")
        cur = con.cursor()
        cur.execute("update employees set Name =%s,sessions=%s,exercises=%s,status=%s,gender=%s,Tech=%s where emp_id =%s",(self.Name_var.get(),self.sessions_var.get(),self.exercises_var.get(),self.status_var.get(),self.gender_var.get(),self.Tech_var.get(),self.emp_id_var.get()))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
    def delete(self):
        con=pymysql.connect(host="localhost",user="root",password="root",database="oilc")
        cur=con.cursor()
        cur.execute("delete from employees where emp_id=%s",self.emp_id_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        con.close()
        
    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="root",database="oilc")
        cur=con.cursor()
        cur.execute("select * from employees where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                self.employee_table.insert('',END,values=row)
            con.commit()
        con.close() 

        

        
        
root = Tk()
obj = employee(root)
obj.add_employees()

root.mainloop()
