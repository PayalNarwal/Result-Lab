from tkinter import *
from course_details import courseClass
from student import studentClass
from exam_record import examClass
from result import resultClass
from final_report import reportClass
from course_report import creportClass
from PIL import Image,ImageTk

class SRM:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1280x700+0+0")
        self.root.config(bg = "black")
##(Upload Images)
        self.bg_image = PhotoImage(file="a.png")
        self.label1 = Label(self.root,image=self.bg_image).place(x = 0, y = 80, width = 1280, height = 700)
        self.logo_img = Image.open("logo.png")
        self.logo_img = self.logo_img.resize((50, 50), Image.ANTIALIAS)
        self.logo_img = ImageTk.PhotoImage(self.logo_img)
        self.chatbot_img = Image.open("chatbot.png")
        self.chatbot_img = self.chatbot_img.resize((80, 80), Image.ANTIALIAS)
        self.chatbot_img = ImageTk.PhotoImage(self.chatbot_img)
##TITLE
        title = Label(self.root, text = "RESULT LAB", padx = 10, compound = LEFT,image = self.logo_img, font = ("courier new", 24, "bold","underline"), bg = "#652A0E", fg = "white").place(x = 0, y = 0, relwidth = 1, height = 50)
        chatbot = Label(self.root, text = "CHAT\nBOT", compound = RIGHT,image = self.chatbot_img, font = ("courier new", 24, "bold","underline"), bg = "#652A0E", fg = "white").place(x = 1115, y = 560, height = 100)
##Menu
        M_Frame = LabelFrame(self.root, text = "Menu", font = ("vivaldi", 25,"bold"), bg = "#9E4244",fg="white",border=10)
        M_Frame.place(x = 0, y = 70, width = 1270, height = 110)
##Buttons
        btn_Course = Button(M_Frame, text = "Courses", font = ("corbel", 20, "bold"), bd = 3, bg = "#FDAB9F", fg = "black", cursor = "hand2", command = self.add_course).place(x = 30, y = 5, width = 180, height = 40)
        btn_Student = Button(M_Frame, text = "Student Details", font = ("corbel", 20, "bold"), bd = 3, bg = "#FDAB9F", fg = "black", cursor = "hand2",command=self.add_student).place(x = 215, y = 5, width = 200, height = 40)
        btn_ExamDetails = Button(M_Frame, text = "Exam Details", font = ("corbel", 20, "bold"), bd = 3, bg = "#FDAB9F", fg = "black", cursor = "hand2", command = self.add_examrecord).place(x = 420, y = 5, width = 200, height = 40)
        btn_marks = Button(M_Frame, text = "Add marks", font = ("corbel", 20, "bold"), bd = 3, bg = "#FDAB9F", fg = "black", cursor = "hand2", command = self.add_result).place(x = 625, y = 5, width = 200, height = 40)
        btn_report = Button(M_Frame, text = "Student Report", font = ("corbel", 20, "bold"), bd = 3, bg = "#FDAB9F", fg = "black", cursor = "hand2", command = self.show_report).place(x = 830, y = 5, width = 200, height = 40)
        btn_course_report = Button(M_Frame, text = "Course Report", font = ("corbel",20, "bold"), bd = 3, bg = "#FDAB9F", fg = "black", cursor = "hand2", command = self.course_report).place(x = 1035, y = 5, width = 200, height = 40)
##Footer
        footer = Label(self.root, text = "RESULT LAB - Student Result Managemnet System - Oopsie Here :)\n ...", font = ("times new romen", 12,), bg = "#262626", fg = "white").pack(side = BOTTOM, fill = X)

    def add_course(self):
        self.new_win = Toplevel(self.root)  
        self.new_obj = courseClass(self.new_win)
    def add_student(self):
        self.new_win = Toplevel(self.root)  
        self.new_obj = studentClass(self.new_win)
    def add_examrecord(self):
        self.new_win = Toplevel(self.root)  
        self.new_obj = examClass(self.new_win)
    def show_report(self):
        self.new_win = Toplevel(self.root)  
        self.new_obj = reportClass(self.new_win) 
    def add_result(self):
        self.new_win = Toplevel(self.root)  
        self.new_obj = resultClass(self.new_win) 
    def course_report(self) :
        self.new_win = Toplevel(self.root)  
        self.new_obj = creportClass(self.new_win) 
        
if __name__ == "__main__":
    root = Tk()
    obj = SRM(root)
    root.mainloop()