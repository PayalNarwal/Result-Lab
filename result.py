from tkinter import *  
from tkinter import ttk, messagebox
import sqlite3

class resultClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x580+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
#===title===
        title=Label(self.root,text="Add Result Details",font=("goudy old style",20,"bold"),bg="#9D3876",fg="#262626").place(x=10,y=15,width=1180,height=50)
#====variables====
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_sub1 = StringVar()
        self.var_sub2 = StringVar()
        self.var_sub3 = StringVar()
        self.var_sub4 = StringVar()
        self.var_sub5 = StringVar()
        self.var_sub6 = StringVar()
        self.marks1 = IntVar()
        self.marks2 = IntVar()
        self.marks3 = IntVar()
        self.marks4 = IntVar()
        self.marks5 = IntVar()
        self.marks6 = IntVar()
        self.totalmarks1 = IntVar()
        self.totalmarks2 = IntVar()
        self.totalmarks3 = IntVar()
        self.totalmarks4 = IntVar()
        self.totalmarks5 = IntVar()
        self.totalmarks6 = IntVar()
        self.int_per = IntVar()
        self.int_obt_marks= IntVar()
        self.int_total_marks= IntVar()
        self.var_obt_marks=StringVar()
        self.var_total_marks=StringVar()
        self.var_percentage=StringVar()

        self.roll_list=[]
        self.subject_list=[]
        self.fetch_roll()
        
        lbl_select=Label(self.root,text="Select Student",font=("goudy old style",15,"bold"),bg="white").place(x=15,y=70)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white").place(x=15,y=100)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg="white").place(x=15,y=130)
        
        self.txt_student=ttk.Combobox(self.root,textvariable=self.var_roll,values=self.roll_list,font=("goudy old style",15,'bold'),state='readonly',justify=CENTER)
        self.txt_student.place(x=200,y=70,width=120)
        self.txt_student.set("Select")
        btn_search=Button(self.root,text='Search',font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=(self.search)).place(x=320,y=70,width=100,height=28)
             
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg='#FAE6FA',state='readonly').place(x=200,y=100,width=220)
        txt_course=Entry(self.root,textvariable=self.var_course,font=("goudy old style",15),bg='#FAE6FA',state='readonly').place(x=200,y=130,width=220)
        
        subjects=Label(self.root,text="Subject",font=("goudy old style",15),bg="orange",fg="#262626").place(x=120,y=190,width=140)
        obt_marks=Label(self.root,text="Obtained marks",font=("goudy old style",15),bg="orange",fg="#262626").place(x=270,y=190,width=140)
        total_marks=Label(self.root,text="Maximum marks",font=("goudy old style",15),bg="orange",fg="#262626").place(x=420,y=190,width=140)

        lbl_sub1 = Label(self.root, text = "subject 1", font = ("goudy old style", 15, "bold"), bg = "white").place(x = 35, y = 220)
        txt_sub1 = Entry(self.root, textvariable = self.var_sub1, font = ("goudy old style", 15, "bold"), bg = "#FAE6FA",state='readonly').place(x = 120, y = 220, width = 140)
        self.txt_marks1 = Entry(self.root , textvariable=self.marks1,justify=CENTER)
        self.txt_fullmarks1 = Entry(self.root, textvariable=self.totalmarks1,justify=CENTER)
        
        lbl_sub2 = Label(self.root, text = "subject 2", font = ("goudy old style", 15, "bold"), bg = "white").place(x = 35, y = 250)
        txt_sub2 = Entry(self.root, textvariable = self.var_sub2, font = ("goudy old style", 15, "bold"), bg = "#FAE6FA",state='readonly').place(x = 120, y = 250, width = 140)
        self.txt_marks2 = Entry(self.root, textvariable=self.marks2,justify=CENTER)
        self.txt_fullmarks2 = Entry(self.root, textvariable=self.totalmarks2,justify=CENTER)

        lbl_sub3 = Label(self.root, text = "subject 3", font = ("goudy old style", 15, "bold"), bg = "white").place(x = 35, y = 280)
        txt_sub3 = Entry(self.root, textvariable = self.var_sub3, font = ("goudy old style", 15, "bold"), bg = "#FAE6FA",state='readonly').place(x = 120, y = 280, width = 140)
        self.txt_marks3 = Entry(self.root, textvariable=self.marks3,justify=CENTER)
        self.txt_fullmarks3 = Entry(self.root, textvariable=self.totalmarks3,justify=CENTER)
        
        lbl_sub4 = Label(self.root, text = "subject 4", font = ("goudy old style", 15, "bold"), bg = "white").place(x = 35, y = 310)
        txt_sub4 = Entry(self.root, textvariable = self.var_sub4, font = ("goudy old style", 15, "bold"), bg = "#FAE6FA",state='readonly').place(x = 120, y = 310, width = 140)
        self.txt_marks4 = Entry(self.root, textvariable=self.marks4 ,justify=CENTER)
        self.txt_fullmarks4 = Entry(self.root, textvariable=self.totalmarks4 ,justify=CENTER)
        
        lbl_sub5 = Label(self.root, text = "subject 5", font = ("goudy old style", 15, "bold"), bg = "white").place(x = 35, y = 340)
        txt_sub5 = Entry(self.root, textvariable = self.var_sub5, font = ("goudy old style", 15, "bold"), bg = "#FAE6FA",state='readonly').place(x = 120, y = 340, width = 140)
        self.txt_marks5 = Entry(self.root, textvariable=self.marks5 ,justify=CENTER)
        self.txt_fullmarks5 = Entry(self.root, textvariable=self.totalmarks5 ,justify=CENTER)
        
        lbl_sub6 = Label(self.root, text = "subject 6", font = ("goudy old style", 15, "bold"), bg = "white").place(x = 35, y = 370)
        txt_sub6 = Entry(self.root, textvariable = self.var_sub6, font = ("goudy old style", 15, "bold"), bg = "#FAE6FA",state='readonly').place(x = 120, y = 370, width = 140)
        self.txt_marks6 = Entry(self.root, textvariable=self.marks6 ,justify=CENTER)
        self.txt_fullmarks6 = Entry(self.root, textvariable=self.totalmarks6 ,justify=CENTER)
    
        self.txt_marks1.place(x = 270, y = 220, width = 140)
        self.txt_marks2.place(x = 270, y = 250, width = 140)
        self.txt_marks3.place(x = 270, y = 280, width = 140)
        self.txt_marks4.place(x = 270, y = 310, width = 140)
        self.txt_marks5.place(x = 270, y = 340, width = 140)
        self.txt_marks6.place(x = 270, y = 370, width = 140)
        self.txt_fullmarks1.place(x = 420, y = 220, width = 140)
        self.txt_fullmarks2.place(x = 420, y = 250, width = 140)
        self.txt_fullmarks3.place(x = 420, y = 280, width = 140)
        self.txt_fullmarks4.place(x = 420, y = 310, width = 140)
        self.txt_fullmarks5.place(x = 420, y = 340, width = 140)
        self.txt_fullmarks6.place(x = 420, y = 370, width = 140)
    
        total1=Button(self.root,text="Obtained marks",font=("goudy old style",13,"bold"),bg="#9370DB",fg="#262626",command=self.display_obt_marks).place(x=25,y=450,width=120)
        self.obt_marks=Label(self.root,bg="#FAE6FA")
        self.obt_marks.place(x=145,y=450,width=80,height=35)

        total2=Button(self.root,text="Total marks",font=("goudy old style",13,"bold"),bg="#9370DB",fg="#262626",command=self.display_total_marks).place(x=230,y=450,width=120)
        self.t_marks=Label(self.root,bg="#FAE6FA")
        self.t_marks.place(x=350,y=450,width=80,height=35)

        perButton=Button(self.root,text="Percentage",font=("goudy old style",13,"bold"),bg="#9370DB",fg="#262626",command=self.percentage).place(x=435,y=450,width=120)
        self.per=Label(self.root,bg="#FAE6FA")
        self.per.place(x=555,y=450,width=120,height=35)

        self.btn_add = Button(self.root, text = "Save", font = ("goudy old style", 15, "bold"), bg = "#2196f3", fg = "white", cursor = "hand2",command=(self.add))
        self.btn_add.place(x = 60, y = 520, width = 110, height = 40)
        self.btn_add = Button(self.root, text = "Update", font = ("goudy old style", 15, "bold"), bg = "#4caf50", fg = "white", cursor = "hand2",command=(self.update))
        self.btn_add.place(x = 180, y = 520, width = 110, height = 40)
        self.btn_delete = Button(self.root, text = "Delete", font = ("goudy old style", 15, "bold"), bg = "#f44336", fg = "white", cursor = "hand2",command=self.delete)
        self.btn_delete.place(x = 300, y = 520, width = 110, height = 40)
        self.btn_clear = Button(self.root, text = "Clear", font = ("goudy old style", 15, "bold"), bg = "#607d8b", fg = "white", cursor = "hand2",command=self.clear)
        self.btn_clear.place(x = 420, y = 520, width = 110, height = 40)

    
##Content
        self.C_Frame = Frame(self.root, bd = 2, relief = RIDGE)
        self.C_Frame.place(x = 720, y = 100, width = 470, height = 340)    
        scrolly = Scrollbar(self.C_Frame, orient = VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient = HORIZONTAL)

        self.ResultTable = ttk.Treeview(self.C_Frame, columns = ("roll", "name", "course", "sub1", "sub2","sub3","sub4","sub5","sub6","obt_marks","total_marks","percentage"), xscrollcommand = scrollx.set, yscrollcommand = scrolly.set)
        scrollx.pack(side = BOTTOM, fill = X)
        scrolly.pack(side = RIGHT, fill = Y)
        scrollx.config(command = self.ResultTable.xview)
        scrolly.config(command = self.ResultTable.yview)

        self.ResultTable.heading("roll", text = "Roll no")
        self.ResultTable.heading("name", text = "Name")        
        self.ResultTable.heading("course", text = "Course")
        self.ResultTable.heading("sub1", text = "subject 1")
        self.ResultTable.heading("sub2", text = "subject 2")   
        self.ResultTable.heading("sub3", text = "subject 3")
        self.ResultTable.heading("sub4", text = "subject 4")        
        self.ResultTable.heading("sub5", text = "subject 5")
        self.ResultTable.heading("sub6", text = "subject 6")
        self.ResultTable.heading("obt_marks", text = "Obtained marks")   
        self.ResultTable.heading("total_marks", text = "Total marks")
        self.ResultTable.heading("percentage", text = "Percentage")
        
        self.ResultTable["show"] = "headings"   

        self.ResultTable.column("roll", width = 100)
        self.ResultTable.column("name", width = 100)        
        self.ResultTable.column("course", width = 100)
        self.ResultTable.column("sub1", width = 100)
        self.ResultTable.column("sub2", width = 100) 
        self.ResultTable.column("sub3", width = 100)
        self.ResultTable.column("sub4", width = 100)        
        self.ResultTable.column("sub5", width = 100)
        self.ResultTable.column("sub6", width = 100)
        self.ResultTable.column("obt_marks", width = 100)   
        self.ResultTable.column("total_marks", width = 100)
        self.ResultTable.column("percentage", width = 100)
        self.ResultTable.pack(fill = BOTH, expand = 1)
        self.ResultTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
    def get_data(self,ev):
        r=self.ResultTable.focus()
        content=self.ResultTable.item(r)
        row=content["values"]
        self.var_roll.set(row[0])
        self.var_name.set(row[1])
        self.var_course.set(row[2])
        self.search_subject()
        self.marks1.set(row[3])
        self.marks2.set(row[4])
        self.marks3.set(row[5])
        self.marks4.set(row[6])
        self.marks5.set(row[7])
        self.marks6.set(row[8])
        # self.display_obt_marks()
        # self.obt_marks.config(text=row[9])
        # self.t_marks.config(text=row[10])
        # self.per.config(text =row[11])
        # self.display_total_marks()
        # self.percentage()

    def fetch_roll(self):
        con=sqlite3.connect(database="student_result_management.db")
        cur=con.cursor()
        try:
            cur.execute("select roll from student_record")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.roll_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    
    def search(self):
        con=sqlite3.connect(database="student_result_management.db")
        cur=con.cursor()
        try:
            cur.execute("select name,course from student_record where roll=?",(self.var_roll.get(),))
            row=cur.fetchone()
            if row!=None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
                self.search_subject()
            else:
                messagebox.showerror("Error","No record found",parent=self.root)   
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def search_subject(self):
        con=sqlite3.connect(database="student_result_management.db")
        cur=con.cursor()
        try:
            cur.execute("select sub1,sub2,sub3,sub4,sub5,sub6 from examrecord where roll=?",(self.var_roll.get(),))
            row=cur.fetchone()
            if row!=None:
                self.var_sub1.set(row[0])
                self.var_sub2.set(row[1])
                self.var_sub3.set(row[2])
                self.var_sub4.set(row[3])
                self.var_sub5.set(row[4])
                self.var_sub6.set(row[5])
            else:
                messagebox.showerror("Error","No record found",parent=self.root)         
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    
    def display_obt_marks(self):
        sum = self.marks1.get() + self.marks2.get() + self.marks3.get() + self.marks4.get() + self.marks5.get() + self.marks6.get()
        self.var_obt_marks=str(sum)
        self.int_obt_marks=sum
        self.obt_marks.config(text=str(sum))

    def display_total_marks(self):
        sum = self.totalmarks1.get()+self.totalmarks2.get()+self.totalmarks3.get()+self.totalmarks4.get()+self.totalmarks5.get()+self.totalmarks6.get()
        self.var_total_marks=str(sum)
        self.int_total_marks=sum
        self.t_marks.config(text=str(sum))

    def percentage(self):
        per=(self.int_obt_marks/self.int_total_marks)*100
        self.var_percentage=str(per)
        self.per.config(text =str(per))

    def add(self):
        con=sqlite3.connect(database="student_result_management.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error", "Roll no is required",parent=self.root)
            else:
                cur.execute("select * from final_result where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","roll no already present",parent=self.root)
                else:
                    cur.execute("insert into final_result(roll,name,course,sub1,sub2,sub3,sub4,sub5,sub6,obt_marks,total_marks,percentage) values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.txt_marks1.get(),
                        self.txt_marks2.get(),
                        self.txt_marks3.get(),
                        self.txt_marks4.get(),
                        self.txt_marks5.get(),
                        self.txt_marks6.get(),
                        self.var_obt_marks,
                        self.var_total_marks,
                        self.var_percentage
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox. showerror ("Error",f"Error due to {str(ex)}")

    def update(self):
        con=sqlite3.connect(database="student_result_management.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error", "Student is required",parent=self.root)
            else:
                cur.execute("select * from  final_result where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","select student from list",parent=self.root)
                else:
                    cur.execute("update final_result set name=?,course=?,sub1=?,sub2=?,sub3=?,sub4=?, sub5=?,sub6=?,obt_marks=?,total_marks=?,percentage=? where roll=?",(
                        self.var_name.get(),
                        self.var_course.get(),
                        self.txt_marks1.get(),
                        self.txt_marks2.get(),
                        self.txt_marks3.get(),
                        self.txt_marks4.get(),
                        self.txt_marks5.get(),
                        self.txt_marks6.get(),
                        self.var_obt_marks,
                        self.var_total_marks,
                        self.var_percentage,
                        self.var_roll.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success"," Marks updated successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox. showerror ("Error",f"Error due to {str(ex)}")

    def show(self):
        con=sqlite3.connect(database="student_result_management.db")
        cur=con.cursor()
        try:
            cur.execute("select * from final_result")
            rows=cur.fetchall()
            self.ResultTable.delete(*self.ResultTable.get_children())
            for row in rows:
                self.ResultTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def clear(self):
        self.show()
        self.var_roll.set("Select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_sub1.set("")
        self.var_sub2.set("")
        self.var_sub3.set("")
        self.var_sub4.set("")
        self.var_sub5.set("")
        self.var_sub6.set("")
        self.marks1.set("")
        self.marks2.set("")
        self.marks3.set("")
        self.marks4.set("")
        self.marks5.set("")
        self.marks6.set("")
        self.totalmarks1.set("")
        self.totalmarks2.set("")
        self.totalmarks3.set("")
        self.totalmarks4.set("")
        self.totalmarks5.set("")
        self.totalmarks6.set("")
        self.var_obt_marks.set(""),
        self.var_total_marks.set("")
        
    def delete(self):
        con=sqlite3.connect(database="student_result_management.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error", "Roll number is required",parent=self.root)
            else:
                cur.execute("select * from  final_result where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","please select student from the list",parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","Do you really want to delete the student",parent=self.root)
                    if op==True:
                        cur.execute("delete from final_result where roll=?",(self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","student deleted successfully")
                        self.clear()
        except Exception as ex:
            # messagebox.showerror("Error",f"Error due to {str(ex)}")
            pass

if __name__=="__main__":
    root=Tk()
    obj=resultClass(root)
    root.mainloop()         