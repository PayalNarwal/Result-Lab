from tkinter import *
from tkinter import ttk,messagebox
import sqlite3

class examClass:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Exam Record Management")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg = "white")
        self.root.focus_force()
##TITLE
        title = Label(self.root, text = "Student Exam Details", font = ("goudy old style", 20, "bold"), bg = "#8A360F", fg = "white").place(x = 10, y = 15, width = 1180, height = 35)
        subjects = Label(self.root, text = "Enter subjects", font = ("goudy old style", 20, "bold"), bg = "#CD8C95", fg = "white").place(x = 15, y = 240, width = 200, height = 30)

##Variables
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_sem = StringVar()
        self.var_exam = StringVar()
        self.var_sub1 = StringVar()
        self.var_sub2 = StringVar()
        self.var_sub3 = StringVar()
        self.var_sub4 = StringVar()
        self.var_sub5 = StringVar()
        self.var_sub6 = StringVar()
        self.roll_list=[]
        self.fetch_roll()
             
##Widgets  
#column1
        lbl_rollno = Label(self.root, text = "Roll no", font = ("goudy old style", 15, "bold"), bg = "white").place(x = 15, y = 60)
        lbl_name = Label(self.root, text = "Name", font = ("goudy old style", 15, "bold"), bg = "white").place(x = 15, y = 100)
        lbl_course = Label(self.root, text = "Course", font = ("goudy old style", 15, "bold"), bg = "white").place(x = 15, y = 140)
        lbl_sem = Label(self.root, text = "Semester", font = ("goudy old style", 15, "bold"), bg = "white").place(x = 15, y = 180)
        lbl_exam = Label(self.root, text = "Exam", font = ("goudy old style", 15, "bold"), bg = "white").place(x = 400, y = 180)
        self.course_list=[]
        self.fetch_course()
        self.txt_course = ttk.Combobox(self.root, textvariable = self.var_course, font = ("goudy old style", 15, "bold"),values=self.course_list)
        self.txt_course.place(x = 150, y = 140, width = 200)
        self.txt_course.set("Select")
        # btn_search=Button(self.root,text='Search',font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=(self.search)).place(x=320,y=70,width=100,height=28)

        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg='#FAE6FA',state='readonly').place(x=150,y=100,width=200)
        txt_sem = Entry(self.root, textvariable = self.var_sem, font = ("goudy old style", 15, "bold"), bg = "#FAE6FA").place(x = 150, y = 180, width = 200)
        
        self.txt_student=ttk.Combobox(self.root,textvariable=self.var_roll,values=self.roll_list,font=("goudy old style",15,'bold'),state='readonly',justify=CENTER)
        self.txt_student.place(x=150,y=60,width=120)
        self.txt_student.set("Select")
        btn_search=Button(self.root,text='Search',font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=(self.search_details)).place(x=270,y=60,width=100,height=28)
         
        self.txt_exam = ttk.Combobox(self.root, textvariable = self.var_exam, font = ("goudy old style", 15, "bold"),state='readonly',justify=CENTER,values=("select","Mid term","End term"))
        self.txt_exam.place(x = 460, y = 180, width = 120)
        self.txt_exam.current(0)

        lbl_sub1 = Label(self.root, text = "Subject 1", font = ("goudy old style", 12, "bold"), bg = "white").place(x = 25, y = 280)
        txt_sub1 = Entry(self.root, textvariable = self.var_sub1, font = ("goudy old style", 15, "bold"), bg = "#FAE6FA").place(x = 120, y = 280, width = 100)
        lbl_sub2 = Label(self.root, text = "Subject 2", font = ("goudy old style", 12, "bold"), bg = "white").place(x = 255, y = 280)
        txt_sub2 = Entry(self.root, textvariable = self.var_sub2, font = ("goudy old style", 15, "bold"), bg = "#FAE6FA").place(x = 340, y = 280, width = 100)
        lbl_sub3 = Label(self.root, text = "Subject 3", font = ("goudy old style", 12, "bold"), bg = "white").place(x = 475, y = 280)
        txt_sub3 = Entry(self.root, textvariable = self.var_sub3, font = ("goudy old style", 15, "bold"), bg = "#FAE6FA").place(x = 560, y = 280, width = 100)
        lbl_sub4 = Label(self.root, text = "Subject 4", font = ("goudy old style", 12, "bold"), bg = "white").place(x = 25, y = 320)
        txt_sub4 = Entry(self.root, textvariable = self.var_sub4, font = ("goudy old style", 15, "bold"), bg = "#FAE6FA").place(x = 120, y = 320, width = 100)
        lbl_sub5 = Label(self.root, text = "Subject 5", font = ("goudy old style", 12, "bold"), bg = "white").place(x = 255, y = 320)
        txt_sub5 = Entry(self.root, textvariable = self.var_sub5, font = ("goudy old style", 15, "bold"), bg = "#FAE6FA").place(x = 340, y = 320, width = 100)
        lbl_sub6 = Label(self.root, text = "Subject 6", font = ("goudy old style", 12, "bold"), bg = "white").place(x = 475, y = 320)
        txt_sub6 = Entry(self.root, textvariable = self.var_sub6, font = ("goudy old style", 15, "bold"), bg = "#FAE6FA").place(x = 560, y = 320, width = 100)
        

##Buttons
        self.btn_add = Button(self.root, text = "Save", font = ("goudy old style", 15, "bold"), bg = "#2196f3", fg = "white", cursor = "hand2",command=self.add)
        self.btn_add.place(x = 200, y = 400, width = 110, height = 40)
        self.btn_update = Button(self.root, text = "Update", font = ("goudy old style", 15, "bold"), bg = "#4caf50", fg = "white", cursor = "hand2",command=self.update)
        self.btn_update.place(x = 320, y = 400, width = 110, height = 40)
        self.btn_delete = Button(self.root, text = "Delete", font = ("goudy old style", 15, "bold"), bg = "#f44336", fg = "white", cursor = "hand2",command=self.delete)
        self.btn_delete.place(x = 440, y = 400, width = 110, height = 40)
        self.btn_clear = Button(self.root, text = "Clear", font = ("goudy old style", 15, "bold"), bg = "#607d8b", fg = "white", cursor = "hand2",command=self.clear)
        self.btn_clear.place(x = 560, y = 400, width = 110, height = 40)

##Search Panel
        self.var_search = StringVar()
        lbl_search_roll = Label(self.root, text = "Roll No.", font = ("goudy old style", 15, "bold"), bg = "white").place(x = 720, y = 60)
        txt_search_roll = Entry(self.root, textvariable = self.var_search, font = ("goudy old style", 15, "bold"), bg = "#FAE6FA").place(x = 870, y = 60, width = 180)
        btn_search = Button(self.root, text = "Search", font = ("goudy old style", 15, "bold"), bg = "#2196f3", fg = "white", cursor = "hand2",command=self.search).place(x = 1070, y = 60, width = 120, height = 28)

##Content
        self.C_Frame = Frame(self.root, bd = 2, relief = RIDGE)
        self.C_Frame.place(x = 720, y = 100, width = 470, height = 340)    
        scrolly = Scrollbar(self.C_Frame, orient = VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient = HORIZONTAL)
        
        self.examTable = ttk.Treeview(self.C_Frame, columns = ("roll","name","course","semester","examination","sub1","sub2","sub3","sub4","sub5","sub6"), xscrollcommand = scrollx.set, yscrollcommand = scrolly.set)
        scrollx.pack(side = BOTTOM, fill = X)
        scrolly.pack(side = RIGHT, fill = Y)
        scrollx.config(command = self.examTable.xview)
        scrolly.config(command = self.examTable.yview)

        self.examTable.heading("roll", text = "Roll no")
        self.examTable.heading("name", text = "Name")        
        self.examTable.heading("course", text = "Course")
        self.examTable.heading("semester", text = "Semester")
        self.examTable.heading("examination", text = "Examination")   
        self.examTable.heading("sub1", text = "sub1")
        self.examTable.heading("sub2", text = "sub2")        
        self.examTable.heading("sub3", text = "sub3")
        self.examTable.heading("sub4", text = "sub4")
        self.examTable.heading("sub5", text = "sub5")   
        self.examTable.heading("sub6", text = "sub6")
        
        self.examTable["show"] = "headings"   

        self.examTable.column("roll", width = 100)
        self.examTable.column("name", width = 100)        
        self.examTable.column("course", width = 100)
        self.examTable.column("semester", width = 50)
        self.examTable.column("examination", width = 100) 
        self.examTable.column("sub1", width = 50)
        self.examTable.column("sub2", width = 50)        
        self.examTable.column("sub3", width = 50)
        self.examTable.column("sub4", width = 50)
        self.examTable.column("sub5", width = 50)   
        self.examTable.column("sub6", width = 50)
        self.examTable.pack(fill = BOTH, expand = 1)
        self.examTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
      
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
    
    def search_details(self):
        con=sqlite3.connect(database="student_result_management.db")
        cur=con.cursor()
        try:
            cur.execute("select name from student_record where roll=?",(self.var_roll.get(),))
            row=cur.fetchone()
            if row!=None:
                self.var_name.set(row[0])
            else:
                messagebox.showerror("Error","No record found",parent=self.root)   
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    def search(self):
        con=sqlite3.connect(database="student_result_management.db")
        cur=con.cursor()
        try:
            cur.execute("select * from examrecord where roll=?",(self.var_search.get(),))
            row=cur.fetchone()
            if row!=None:
                self.examTable.delete(*self.examTable.get_children())
                self.examTable.insert('',END,values=row)
            else:
                messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
            messagebox. showerror ("Error",f"Error due to {str(ex)}")

    def clear(self):
        self.show()
        self.var_roll.set("")
        self.var_name.set("")
        self.var_course.set("")
        self.var_sem.set("")
        self.var_exam.set("")
        self.var_sub1.set("")
        self.var_sub2.set("")
        self.var_sub3.set("")
        self.var_sub4.set("")
        self.var_sub5.set("")
        self.var_sub6.set("")
        # self.txt_roll.config(state=NORMAL)
        self.var_search.set("")

    def delete(self):
        con=sqlite3.connect(database="student_result_management.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error", "Roll number is required",parent=self.root)
            else:
                cur.execute("select * from  examrecord where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","please select student from the list",parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","Do you really want to delete the student",parent=self.root)
                    if op==True:
                        cur.execute("delete from examrecord where roll=?",(self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","student deleted successfully")
                        self.clear()
        except Exception as ex:
            messagebox. showerror ("Error",f"Error due to {str(ex)}")

    def get_data(self,ev):
        r=self.examTable.focus()
        content=self.examTable.item(r)
        row=content["values"]
        print(row)
        self.var_roll.set(row[0])
        self.var_name.set(row[1])
        self.var_course.set(row[2])
        self.var_sem.set(row[3])
        self.var_exam.set(row[4])
        self.var_sub1.set(row[5])
        self.var_sub2.set(row[6])
        self.var_sub3.set(row[7])
        self.var_sub4.set(row[8])
        self.var_sub5.set(row[9])
        self.var_sub6.set(row[10])

    def add(self):
        con=sqlite3.connect(database="student_result_management.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error", "Roll no is required",parent=self.root)
            else:
                cur.execute("select * from examrecord where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","roll no already present",parent=self.root)
                else:
                    cur.execute("insert into examrecord(roll,name,course,semester,examination,sub1,sub2,sub3,sub4,sub5,sub6) values(?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_sem.get(),
                        self.var_exam.get(),
                        self.var_sub1.get(),
                        self.var_sub2.get(),
                        self.var_sub3.get(),
                        self.var_sub4.get(),
                        self.var_sub5.get(),
                        self.var_sub6.get()
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
                messagebox.showerror("Error", "Course Name should be required",parent=self.root)
            else:
                cur.execute("select * from  examrecord where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","select student from list",parent=self.root)
                else:
                    cur.execute("update examrecord set name=?,course=?,semester=?,examination=?,sub1=?,sub2=?, sub3=?,sub4=?,sub5=?,sub6=? where roll=?",(
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_sem.get(),
                        self.var_exam.get(),
                        self.var_sub1.get(),
                        self.var_sub2.get(),
                        self.var_sub3.get(),
                        self.var_sub4.get(),
                        self.var_sub5.get(),
                        self.var_sub6.get(),
                        self.var_roll.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success"," Student updated successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox. showerror ("Error",f"Error due to {str(ex)}")

    def show(self):
        con=sqlite3.connect(database="student_result_management.db")
        cur=con.cursor()
        try:
            cur.execute("select * from examrecord")
            rows=cur.fetchall()
            self.examTable.delete(*self.examTable.get_children())
            for row in rows:
                self.examTable.insert('',END,values=row)
        except Exception as ex:
            messagebox. showerror ("Error",f"Error due to {str(ex)}")
    
    def fetch_course(self):
        con=sqlite3.connect(database="student_result_management.db")
        cur=con.cursor()
        try:
            cur.execute("select distinct(name) from course2")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])
        except Exception as ex:
            messagebox. showerror ("Error",f"Error due to {str(ex)}")

if __name__ == "__main__":
    root = Tk()
    obj = examClass(root)
    root.mainloop()