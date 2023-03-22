from tkinter import *  
from tkinter import ttk, messagebox
import sqlite3

class creportClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x580+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
#===title===
        title=Label(self.root,text="Course Report Details",font=("goudy old style",20,"bold"),bg="#9D3876",fg="#262626").place(x=10,y=15,width=1180,height=50)
#====variables====
        self.var_course=StringVar()
        self.var_total_candidates=StringVar()
        self.var_candidates_passed=StringVar()
        self.var_failed=StringVar()   
        self.var_avg_marks = StringVar()
        self.var_highest_marks = StringVar()
        self.var_lowest_marks = StringVar()


##labels
        lbl_select=Label(self.root,text="Select Course",font=("goudy old style",15,"bold"),bg="teal").place(x=400,y=140,width=150)
        lbl_total_candidates=Label(self.root,text="Total Candidates",font=("goudy old style",15,"bold"),bg="teal").place(x=400,y=200,width=150)
        lbl_candidates_passed=Label(self.root,text="Candidates Passed",font=("goudy old style",15,"bold"),bg="teal").place(x=400,y=240,width=150)
        lbl_failed=Label(self.root,text="Candidates Failed",font=("goudy old style",15,"bold"),bg="teal").place(x=400,y=280,width=150)
        lbl_avg_marks=Label(self.root,text="Average Marks",font=("goudy old style",15,"bold"),bg="teal").place(x=400,y=340,width=150)
        lbl_highest_marks=Label(self.root,text="Highest Marks",font=("goudy old style",15,"bold"),bg="teal").place(x=400,y=380,width=150)
        lbl_lowest_marks=Label(self.root,text="Lowest Marks",font=("goudy old style",15,"bold"),bg="teal").place(x=400,y=420,width=150)


        txt_course=Entry(self.root,textvariable=self.var_course,font=("goudy old style",15),bg='#FAE6FA').place(x=570,y=140,width=120)
        btn_search=Button(self.root,text='Search',font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=(self.search)).place(x=690,y=140,width=100,height=28)
        
        txt_total_candidates=Entry(self.root,textvariable=self.var_total_candidates,font=("goudy old style",15),bg='#FAE6FA',state='readonly').place(x=570,y=200,width=220) 
        txt_candidates_passed=Entry(self.root,textvariable=self.var_candidates_passed,font=("goudy old style",15),bg='#FAE6FA',state='readonly').place(x=570,y=240,width=220)
        txt_failed=Entry(self.root,textvariable=self.var_failed,font=("goudy old style",15),bg='#FAE6FA',state='readonly').place(x=570,y=280,width=220)
        txt_avg_marks=Entry(self.root,textvariable=self.var_avg_marks,font=("goudy old style",15),bg='#FAE6FA',state='readonly').place(x=570,y=340,width=220)
        txt_highest_marks=Entry(self.root,textvariable=self.var_highest_marks,font=("goudy old style",15),bg='#FAE6FA',state='readonly').place(x=570,y=380,width=220)
        txt_lowest_marks=Entry(self.root,textvariable=self.var_lowest_marks,font=("goudy old style",15),bg='#FAE6FA',state='readonly').place(x=570,y=420,width=220)

        self.btn_clear = Button(self.root, text = "Clear", font = ("goudy old style", 15, "bold"), bg = "#607d8b", fg = "white", cursor = "hand2",command=self.clear)
        self.btn_clear.place(x = 500, y = 490, width = 110, height = 40)


    def clear(self):
        self.var_course.set("")
        self.var_total_candidates.set("")
        self.var_candidates_passed.set("")
        self.var_failed.set("")
        self.var_avg_marks.set("")
        self.var_highest_marks.set("")
        self.var_lowest_marks.set("")
        
    def search(self):
        con=sqlite3.connect(database="student_result_management.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                 messagebox.showerror("Error","Course Name should be required")
            else:
                cur.execute("select count(name) from student_record where course=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.var_total_candidates.set(row[0])
                    self.search_total_passed()
                    self.search_total_fail()
                    self.highest_marks()
                    self.lowest_marks()
                    self.average_marks()
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)  
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
    def search_total_fail(self):
        con=sqlite3.connect(database="student_result_management.db")
        cur=con.cursor()
        try:
            cur.execute("select * from final_result where CAST(percentage as int)<=45 and course = ? ",(self.var_course.get(),))
            row=len(cur.fetchall())
            print(row)
            if row!=None:
                self.var_failed.set(row)
            else:
                messagebox.showerror("Error","No record found",parent=self.root)    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    
    def search_total_passed(self):
        con=sqlite3.connect(database="student_result_management.db")
        cur=con.cursor()
        try:
            cur.execute("select * from final_result where CAST(percentage as int)>45 and course = ? ",(self.var_course.get(),))           
            row=len(cur.fetchall())
            if row!=None:
                self.var_candidates_passed.set(row)
            else:
                messagebox.showerror("Error","No record found",parent=self.root)    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        
    def highest_marks(self):
        con=sqlite3.connect(database="student_result_management.db")
        cur=con.cursor()
        try:
            cur.execute("select obt_marks from final_result ")
            row=cur.fetchall()
            if row!=None:
                # self.var_obt_marks.set(row[0])
                # self.var_total_marks.set(row[1])
                self.var_highest_marks.set(max(row))
            else:
                messagebox.showerror("Error","No record found",parent=self.root)    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    
    def lowest_marks(self):
        con=sqlite3.connect(database="student_result_management.db")
        cur=con.cursor()
        try:
            cur.execute("select obt_marks from final_result ")
            row=cur.fetchall()
            if row!=None:
                self.var_lowest_marks.set(min(row))
            else:
                messagebox.showerror("Error","No record found",parent=self.root)    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
    def average_marks(self):
        con=sqlite3.connect(database="student_result_management.db")
        cur=con.cursor()
        try:
            cur.execute("select avg(CAST(obt_marks as INT)) from final_result ")
            row=cur.fetchall()
            # cur.execute("select * from final_result ")
            # n = len(cur.fetchall())
            if row!=None:
                self.var_avg_marks.set((row[0]))
            else:
                messagebox.showerror("Error","No record found",parent=self.root)    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    



if __name__=="__main__":
    root=Tk()
    obj=creportClass(root)
    root.mainloop()  
        