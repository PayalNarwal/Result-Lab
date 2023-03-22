from tkinter import *  
from tkinter import ttk, messagebox
import sqlite3
import matplotlib
import matplotlib.pyplot as plt 
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class reportClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x680+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
#===title===
        title=Label(self.root,text="Final Report Details",font=("goudy old style",20,"bold"),bg="#9D3876",fg="#262626").place(x=10,y=15,width=1180,height=50)
#====variables====
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_branch=StringVar()
        self.var_dob = StringVar()
        self.var_mothers_name = StringVar()       
        self.var_fathers_name = StringVar()
        self.var_obt_marks = StringVar()
        self.var_total_marks = StringVar()
        self.var_percentage = StringVar()
        self.subject_list=[]
        self.marks_list=[]

        lbl_select=Label(self.root,text="Select Student",font=("goudy old style",13,"bold"),bg="teal").place(x=100,y=120,width=150)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",13,"bold"),bg="teal").place(x=100,y=160,width=150)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",13,"bold"),bg="teal").place(x=100,y=200,width=150)
        lbl_branch=Label(self.root,text="Branch",font=("goudy old style",13,"bold"),bg="teal").place(x=100,y=240,width=150)
        lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",13,"bold"),bg="teal").place(x=100,y=280,width=150)
        lbl_mn=Label(self.root,text="Mother's Name",font=("goudy old style",13,"bold"),bg="teal").place(x=100,y=320,width=150)
        lbl_pn=Label(self.root,text="Father's Name",font=("goudy old style",13,"bold"),bg="teal").place(x=100,y=360,width=150)
        lbl_obt_marks=Label(self.root,text="Obtained Marks",font=("goudy old style",13,"bold"),bg="teal").place(x=100,y=400,width=150)
        lbl_total_marks=Label(self.root,text="Total Marks",font=("goudy old style",13,"bold"),bg="teal").place(x=100,y=440,width=150)
        lbl_percentage=Label(self.root,text="Percentage",font=("goudy old style",13,"bold"),bg="teal").place(x=100,y=480,width=150)
        
        txt_roll=Entry(self.root,textvariable=self.var_roll,font=("goudy old style",13),bg='#FAE6FA').place(x=270,y=120,width=120)
        btn_search=Button(self.root,text='Search',font=("goudy old style",13,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=(self.search)).place(x=400,y=120,width=90,height=25)
             
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",13),bg='#FAE6FA',state='readonly').place(x=270,y=160,width=220)
        txt_course=Entry(self.root,textvariable=self.var_course,font=("goudy old style",13),bg='#FAE6FA',state='readonly').place(x=270,y=200,width=220)
        txt_branch=Entry(self.root,textvariable=self.var_branch,font=("goudy old style",13),bg='#FAE6FA',state='readonly').place(x=270,y=240,width=220)
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",13),bg='#FAE6FA',state='readonly').place(x=270,y=280,width=220)
        txt_mn=Entry(self.root,textvariable=self.var_mothers_name,font=("goudy old style",13),bg='#FAE6FA',state='readonly').place(x=270,y=320,width=220)
        txt_pn=Entry(self.root,textvariable=self.var_fathers_name,font=("goudy old style",13),bg='#FAE6FA',state='readonly').place(x=270,y=360,width=220)
        txt_obt_marks=Entry(self.root,textvariable=self.var_obt_marks,font=("goudy old style",13),bg='#FAE6FA',state='readonly').place(x=270,y=400,width=220)
        txt_total_marks=Entry(self.root,textvariable=self.var_total_marks,font=("goudy old style",13),bg='#FAE6FA',state='readonly').place(x=270,y=440,width=220)
        txt_percentage=Entry(self.root,textvariable=self.var_percentage,font=("goudy old style",13),bg='#FAE6FA',state='readonly').place(x=270,y=480,width=220)

        self.btn_clear = Button(self.root, text = "Clear", font = ("goudy old style", 15, "bold"), bg = "#607d8b", fg = "white", cursor = "hand2",command=self.clear)
        self.btn_clear.place(x = 300, y = 550, width = 110, height = 40)

    def clear(self):
        self.var_roll.set("")
        self.var_name.set("")
        self.var_course.set("")
        self.var_branch.set("")
        self.var_dob.set("")
        self.var_mothers_name.set("")
        self.var_fathers_name.set("")
        self.var_obt_marks.set("")
        self.var_total_marks.set("")
        self.var_percentage.set("")
        
    
    def graph(self):
        self.fig = plt.figure(figsize=(6,5),dpi=100)
        c=["red","yellow","green","orange","pink","blue"]
        barplot = self.fig.add_subplot(111).bar(self.subject_list,self.marks_list,color=c)
        plt.bar_label(barplot,labels=self.marks_list,label_type="edge")
        self.canvas=FigureCanvasTkAgg(self.fig,self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x = 620, y = 130)

    def search(self):
        con=sqlite3.connect(database="student_result_management.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                 messagebox.showerror("Error","Roll No. should be required")  
            else:
                cur.execute("select name,course,pin,dob,city,state from student_record where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.var_name.set(row[0])
                    self.var_course.set(row[1])
                    self.var_branch.set(row[2])
                    self.var_dob.set(row[3])
                    self.var_mothers_name.set(row[4])
                    self.var_fathers_name.set(row[5])
                    self.search_marks()
                    self.search_sub_name()
                    self.search_sub_marks()
                    self.graph()
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)  
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def search_marks(self):
        con=sqlite3.connect(database="student_result_management.db")
        cur=con.cursor()
        try:
            cur.execute("select obt_marks,total_marks,percentage from final_result where roll=?",(self.var_roll.get(),))
            row=cur.fetchone()
            if row!=None:
                self.var_obt_marks.set(row[0])
                self.var_total_marks.set(row[1])
                self.var_percentage.set(row[2])
            else:
                messagebox.showerror("Error","No record found",parent=self.root)    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    
    def search_sub_name(self):
        con=sqlite3.connect(database="student_result_management.db")
        cur=con.cursor()
        try:
            cur.execute("select sub1,sub2,sub3,sub4,sub5,sub6 from examrecord where roll=?",(self.var_roll.get(),))
            row=cur.fetchone()
            if row!=None:
                self.subject_list.append(row[0])
                self.subject_list.append(row[1])
                self.subject_list.append(row[2])
                self.subject_list.append(row[3])
                self.subject_list.append(row[4])
                self.subject_list.append(row[5])
            else:
                messagebox.showerror("Error","No record found",parent=self.root)    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    
    def search_sub_marks(self):
        con=sqlite3.connect(database="student_result_management.db")
        cur=con.cursor()
        try:
            cur.execute("select sub1,sub2,sub3,sub4,sub5,sub6 from final_result where roll=?",(self.var_roll.get(),))
            row=cur.fetchone()
            if row!=None:
                self.marks_list.append(float(row[0]))
                self.marks_list.append(float(row[1]))
                self.marks_list.append(float(row[2]))
                self.marks_list.append(float(row[3]))
                self.marks_list.append(float(row[4]))
                self.marks_list.append(float(row[5]))
            else:
                messagebox.showerror("Error","No record found",parent=self.root)    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    

    # def clear(self):
    #     self.var_roll.set("")
    #     self.var_name.set("")
    #     self.var_course.set("")
    #     self.var_branch.set("")
    #     self.var_dob.set("")
    #     self.var_mothers_name.set("")
    #     self.var_fathers_name.set("")
    #     self.var_obt_marks.set("")
    #     self.var_total_marks.set("")
    #     self.var_percentage.set("")
        

if __name__=="__main__":
    root=Tk()
    obj=reportClass(root)
    root.mainloop()         