import re
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog

#Global variable for importCsv Function 
mydata=[]
class Attendance:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance Pannel")

        #-----------Variables-------------------
        self.var_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attend=StringVar()

        # This part is image labels setting start 
        # first header image  
        img=Image.open(r"C:\\Users\\riyan\\OneDrive\\Desktop\\Attendance System\\images\\student1.jpg")
        img=img.resize((800,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=800,height=200)

        img1=Image.open(r"C:\\Users\\riyan\\OneDrive\\Desktop\\Attendance System\\images\\student1.jpg")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img1)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=80,y=0,width=800,height=200)

        # backgorund image 
        bg1=Image.open(r"C:\\Users\\riyan\\OneDrive\\Desktop\\Attendance System\\images\\student1.jpg")
        bg1=bg1.resize((1530,710),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1530,height=710)


        #title section
        title_lb1 = Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        #========================Section Creating==================================

        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=20,y=55,width=1480,height=600)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(x=10,y=10,width=730,height=580)
        
        img_left=Image.open("C:\\Users\\riyan\\OneDrive\\Desktop\\Attendance System\\images\\student2.jpg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
         
        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)
        
        left_inside_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,font=("verdana",12,"bold"),fg="navyblue")
        left_inside_frame.place(x=0,y=135,width=720,height=370)

        # ==================================Text boxes and Combo Boxes====================

        #Student id
        attendanceId_label = Label(left_inside_frame,text="Attendance ID:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceId_entry = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_id,font=("verdana",12,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Student Roll
        rollLabel = Label(left_inside_frame,text="Roll_No:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        rollLabel.grid(row=0,column=2,padx=4,pady=8)

        atten_roll = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_roll,font=("verdana",12,"bold"))
        atten_roll.grid(row=0,column=3,pady=8)

        #Student Name
        nameLabel = Label(left_inside_frame,text="Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        nameLabel.grid(row=1,column=0)

        atten_name = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_name,font=("verdana",12,"bold"))
        atten_name.grid(row=1,column=1,pady=8)

        #Studnet department
        debLabel = Label(left_inside_frame,text="Department:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        debLabel.grid(row=1,column=2)

        atten_dep= ttk.Entry(left_inside_frame,width=15,textvariable=self.var_dep,font=("verdana",12,"bold"))
        atten_dep.grid(row=1,column=3,pady=8)

      

        #time
        timeLabel = Label(left_inside_frame,text="Time:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        timeLabel.grid(row=2,column=0)

        atten_time = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_time,font=("verdana",12,"bold"))
        atten_time.grid(row=2,column=1,pady=8)

        #Date 
        date_label = Label(left_inside_frame,text="Date:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        date_label.grid(row=2,column=2)

        date_entry = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_date,font=("verdana",12,"bold"))
        date_entry.grid(row=2,column=3,pady=8)

        #Attendance
        attendanceLabel = Label(left_inside_frame,text="Attend-status:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        attendanceLabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_attend,font=("verdana",12,"bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

  

        # =========================button section========================

        #Button Frame
        btn_frame = Frame(left_inside_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=0,y=300,width=715,height=35)

        #Improt button
        save_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,width=13,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        save_btn.grid(row=0,column=0,padx=8)

        #Exprot button
        update_btn=Button(btn_frame,text="Export CSV",command=self.exportCsv,width=13,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        update_btn.grid(row=0,column=1,padx=8)

        #Update button
        del_btn=Button(btn_frame,text="Update",width=13,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=2,padx=8)

        #reset button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=13,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=0,column=3,padx=8)



        # Right section=======================================================

        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="navyblue")
        right_frame.place(x=750,y=10,width=720,height=580)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=455)

#=====================scroll bar table=====================
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","name","roll","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("roll",text="Roll no")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("name",width=100)
        
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
       





         #==========================fetch data===================

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    def importCsv(self):
        global mydata
        fin=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fin) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data","No Data found to export",parent=self.root)
                return False
            fin=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fin,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fin)+"successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_id.set(rows[0]),
        self.var_name.set(rows[1]),
        self.var_roll.set(rows[2]),
        self.var_time.set(rows[3]),
        self.var_date.set(rows[4]),
        self.var_attend.set(rows[5])  

    def reset_data(self):
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_roll.set(""),
        self.var_time.set(""),
        self.var_date.set(""),
        self.var_attend.set("") 
        



        


       








if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()