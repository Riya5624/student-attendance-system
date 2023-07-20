from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import os
import cv2
import mysql.connector
from time import strftime
from datetime import datetime

class Developer:
    def __init__(self,root):
         self.root=root
         self.root.geometry("1530x790+0+0")
         self.root.title("face Recognition System")


         title=Label(self.root,text="Developer",font=("Helvetica",34,"bold"),bg="white",fg="#74b3ce")
         title.place(x=0,y=0,width=1530,height=45)


         img_top=Image.open(r"images\\t3.jpeg")
         img_top=img_top.resize((1530,720),Image.ANTIALIAS)
         self.photoimg_top=ImageTk.PhotoImage(img_top)
         
         f_lbl=Label(self.root,image=self.photoimg_top)
         f_lbl.place(x=0,y=55,width=1530,height=720)

         main_frame=Frame(f_lbl,bd=2,bg="white")
         main_frame.place(x=1000,y=0,width=500,height=600)

         img_top1=Image.open(r"images\\t3.jpeg")
         img_top1=img_top1.resize((200,200),Image.ANTIALIAS)
         self.photoimg_top1=ImageTk.PhotoImage(img_top1)
         
         f_lbl=Label(main_frame,image=self.photoimg_top1)
         f_lbl.place(x=300,y=0,width=200,height=200)

         dev_lbl=Label(main_frame,text="Hello! hope you enjoy this app",font=("times new roman",20,"bold"),bg="white")

         dev_lbl.place(x=0,y=5)


         
if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)

    root.mainloop()