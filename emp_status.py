from tkinter import*
from tkinter import ttk
import pymysql
from tkinter import messagebox
class employee:
    def __init__(self,root):
        self.root = root
        self.root.title("OILC-Management system")
        self.root.geometry("1370x700")
        
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
#obj.add_employees()

root.mainloop()
