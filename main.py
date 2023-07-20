from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
import tkinter
from face_recognition import Face_Recognition
from train import Train
from attendance import Attendance
from developer import Developer
from time import strftime
from chatbot import ChatBot


class Face_Recognition_System:
    def __init__(self,root):
         self.root=root
         self.root.geometry("1530x790+0+0")
         self.root.title("face Recognition System")

         img=Image.open("images\\logo.jpg")
         img=img.resize((500,130),Image.ANTIALIAS)
         self.photoimg=ImageTk.PhotoImage(img)
         
         f_lbl=Label(self.root,image=self.photoimg)
         f_lbl.place(x=0,y=0,width=500,height=130)

         
         img1=Image.open("images\\face.jpg")
         img1=img1.resize((500,130),Image.ANTIALIAS)
         self.photoimg1=ImageTk.PhotoImage(img1)
         
         f_lbl=Label(self.root,image=self.photoimg1)
         f_lbl.place(x=500,y=0,width=500,height=130)
         
         
         img2=Image.open("images\\college.jpg")
         img2=img2.resize((550,130),Image.ANTIALIAS)
         self.photoimg2=ImageTk.PhotoImage(img2)
         
         f_lbl=Label(self.root,image=self.photoimg2)
         f_lbl.place(x=1000,y=0,width=550,height=130)

         img3=Image.open("images\\bg.png")
         img3=img3.resize((1530,710),Image.ANTIALIAS)
         self.photoimg3=ImageTk.PhotoImage(img3)
         bg_img=Label(self.root,image=self.photoimg3)
         bg_img.place(x=0,y=130,width=1530,height=710)
         
         title=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("Helvetica",34,"bold"),bg="white",fg="#74b3ce")
         title.place(x=0,y=0,width=1530,height=45)

         #=====================time=====================
         def time():
              string=strftime('%H:%M:%S %p')
              lbl.config(text=string)
              lbl.after(1000,time)
         lbl=Label(title,font=('times new roman',14,'bold'),background='white',foreground='blue')
         lbl.place(x=0,y=(-15),width=110,height=50)
         time()


         #student button
         img4=Image.open("images\\student.png")
         img4=img4.resize((220,220),Image.ANTIALIAS)
         self.photoimg4=ImageTk.PhotoImage(img4)

         b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
         b1.place(x=200,y=100,width=220,height=220)

         b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("Helvetica",15,"bold"),bg="#1034A6",fg="white")
         b1_1.place(x=200,y=300,width=220,height=40)
         
         #detect face button
         img5=Image.open("images\\facial-recognition.png")
         img5=img5.resize((220,220),Image.ANTIALIAS)
         self.photoimg5=ImageTk.PhotoImage(img5)

         b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
         b1.place(x=500,y=100,width=220,height=220)

         b1_1=Button(bg_img,text="Detect Face",cursor="hand2",command=self.face_data,font=("Helvetica",15,"bold"),bg="#1034A6",fg="white")
         b1_1.place(x=500,y=300,width=220,height=40)
         
        #attendance
         img6=Image.open("images\\attendance.png")
         img6=img6.resize((220,220),Image.ANTIALIAS)
         self.photoimg6=ImageTk.PhotoImage(img6)

         b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.Attendance_data)
         b1.place(x=800,y=100,width=220,height=220)

         b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.Attendance_data,font=("Helvetica",15,"bold"),bg="#1034A6",fg="white")
         b1_1.place(x=800,y=300,width=220,height=40)

          #help desk
         img7=Image.open("images\\helpdesk.png")
         img7=img7.resize((220,220),Image.ANTIALIAS)
         self.photoimg7=ImageTk.PhotoImage(img7)

         b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.chatbot_data)
         b1.place(x=1100,y=100,width=220,height=220)

         b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.chatbot_data,font=("Helvetica",15,"bold"),bg="#1034A6",fg="white")
         b1_1.place(x=1100,y=300,width=220,height=40)

           #Train Data
         img8=Image.open("images\\train.png")
         img8=img8.resize((220,220),Image.ANTIALIAS)
         self.photoimg8=ImageTk.PhotoImage(img8)

         b1=Button(bg_img,image=self.photoimg8,command=self.train_data,cursor="hand2")
         b1.place(x=200,y=380,width=220,height=220)

         b1_1=Button(bg_img,text="Train",cursor="hand2",command=self.train_data,font=("Helvetica",15,"bold"),bg="#1034A6",fg="white")
         b1_1.place(x=200,y=580,width=220,height=40)

        #photos
         img9=Image.open("images\\photos.png")
         img9=img9.resize((220,220),Image.ANTIALIAS)
         self.photoimg9=ImageTk.PhotoImage(img9)

         b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
         b1.place(x=500,y=380,width=220,height=220)

         b1_1=Button(bg_img,text="Photo",cursor="hand2",command=self.open_img,font=("Helvetica",15,"bold"),bg="#1034A6",fg="white")
         b1_1.place(x=500,y=580,width=220,height=40)
        #developer
         img10=Image.open("images\\developer.png")
         img10=img10.resize((220,220),Image.ANTIALIAS)
         self.photoimg10=ImageTk.PhotoImage(img10)

         b1=Button(bg_img,image=self.photoimg10,command=self.developer_data,cursor="hand2")
         b1.place(x=800,y=380,width=220,height=220)

         b1_1=Button(bg_img,text="Developer",command=self.developer_data,cursor="hand2",font=("Helvetica",15,"bold"),bg="#1034A6",fg="white")
         b1_1.place(x=800,y=580,width=220,height=40)
         #exit
         img11=Image.open("images\\exit.png")
         img11=img11.resize((220,220),Image.ANTIALIAS)
         self.photoimg11=ImageTk.PhotoImage(img11)

         b1=Button(bg_img,image=self.photoimg11,command=self.iExit,cursor="hand2")
         b1.place(x=1100,y=380,width=220,height=220)

         b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("Helvetica",15,"bold"),bg="#1034A6",fg="white")
         b1_1.place(x=1100,y=580,width=220,height=40)

    def open_img(self):
         os.startfile("data")

    def iExit(self):
         self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure, you want to exit this project",parent=self.root)
         if self.iExit>0:
              self.root.destroy()
         else:
              return

       #=============================functions button==========================

    def student_details(self):
         self.new_window=Toplevel(self.root)
         self.app=Student(self.new_window)

    def train_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Train(self.new_window)

    def face_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Face_Recognition(self.new_window)

    def Attendance_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Attendance(self.new_window)

    def developer_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Developer(self.new_window)

    def chatbot_data(self):
         self.new_window=Toplevel(self.root)
         self.app=ChatBot(self.new_window)
  
    

    

     




if __name__=="__main__":
     root=Tk()
     obj=Face_Recognition_System(root)
     root.mainloop()