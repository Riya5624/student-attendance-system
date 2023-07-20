from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Pannel")

        #==============variables=================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        

       
    # This part is image labels setting start 
        # first header image  
        img=Image.open("images\\student1.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=500,height=130)
    
        img1=Image.open("images\\student.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
         
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
         
         
        img2=Image.open("images\\student3.jpg")
        img2=img2.resize((550,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
         
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        

         # backgorund image 
        bg1=Image.open(r"images\\bg.png")
        bg1=bg1.resize((1530,710),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1530,height=710)


        #title section
        title_lb1 = Label(bg_img,text="STUDENT MANAGEMENT SYSTEM ",font=("verdana",35,"bold"),bg="NAVYBLUE",fg="WHITE")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=20,y=50,width=1480,height=600)

        # Left Label Frame 
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="navyblue")
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open("images\\student2.jpg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
         
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        # Current Course 
        current_course_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course",font=("verdana",13,"bold"),fg="navyblue")
        current_course_frame.place(x=5,y=135,width=720,height=125)

        #label Department
        dep_label=Label(current_course_frame,text="Department",font=("verdana",13,"bold"),bg="white",fg="navyblue")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        #combo box 
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,width=15,font=("verdana",13,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","BCA","B.Voc","Diploma")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # -----------------------------------------------------

        #label Course
        course_label=Label(current_course_frame,text="Course",font=("verdana",13,"bold"),bg="white",fg="navyblue")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        #combo box 
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,width=15,font=("verdana",13,"bold"),state="readonly")
        course_combo["values"]=("Select Course","CE","ME","IT","DE","MC","SD","BCA")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #-------------------------------------------------------------

        #label Year
        year_label=Label(current_course_frame,text="Year",font=("verdana",13,"bold"),bg="white",fg="navyblue")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        #combo box 
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,width=15,font=("verdana",12,"bold"),state="readonly")
        year_combo["values"]=("Select Year","2017-20","2018-21","2019-22","2020-23","2021-24","2022-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #-----------------------------------------------------------------

        #label Semester 
        semester_label=Label(current_course_frame,text="Semester",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        #combo box 
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,width=15,font=("verdana",13,"bold"),state="readonly")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class Student Information
        class_Student_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("verdana",13,"bold"),fg="navyblue")
        class_Student_frame.place(x=5,y=270,width=720,height=300)

        #Student id
        studentId_label = Label(class_Student_frame,text="StudentID:",font=("verdana",13,"bold"),fg="navyblue",bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=13,font=("verdana",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Student name
        studentName_label = Label(class_Student_frame,text="Student Name:",font=("verdana",13,"bold"),fg="navyblue",bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=13,font=("verdana",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Class Division
        class_div_label = Label(class_Student_frame,text="Class Division:",font=("verdana",13,"bold"),fg="navyblue",bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,width=13,font=("verdana",13,"bold"),state="readonly")
        div_combo["values"]=("Select division","A","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        #Roll No
        roll_no_label = Label(class_Student_frame,text="Roll No:",font=("verdana",13,"bold"),fg="navyblue",bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry = ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=13,font=("verdana",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        gender_label = Label(class_Student_frame,text="Gender:",font=("verdana",13,"bold"),fg="navyblue",bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,width=13,font=("verdana",13,"bold"),state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=5,sticky=W)

        #Date of Birth
        dob_label = Label(class_Student_frame,text="DOB:",font=("verdana",13,"bold"),fg="navyblue",bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=13,font=("verdana",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email
        email_label = Label(class_Student_frame,text="Email:",font=("verdana",13,"bold"),fg="navyblue",bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        student_email_entry = ttk.Entry(class_Student_frame,textvariable=self.var_email,width=15,font=("verdana",13,"bold"))
        student_email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone Number
        phone_label = Label(class_Student_frame,text="Phone No:",font=("verdana",13,"bold"),fg="navyblue",bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry = ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=13,font=("verdana",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Address
        address_label = Label(class_Student_frame,text="Address:",font=("verdana",13,"bold"),fg="navyblue",bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry = ttk.Entry(class_Student_frame,textvariable=self.var_address,width=15,font=("verdana",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Teacher Name
        teacher_label = Label(class_Student_frame,text="Teacher Name:",font=("verdana",13,"bold"),fg="navyblue",bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry = ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=13,font=("verdana",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #Radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0,padx=5,pady=5,sticky=W)

        
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn1.grid(row=6,column=1,padx=5,pady=5,sticky=W)

        #Button Frame
        btn_frame = Frame(class_Student_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=0,y=210,width=715,height=50)

        #save button
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        save_btn.grid(row=0,column=0,padx=5,pady=10,sticky=W)

        #update button
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        update_btn.grid(row=0,column=1,padx=5,pady=8,sticky=W)

        #delete button
        del_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        #take photo button
        take_photo_btn=Button(btn_frame,text="Take Pic",command=self.generate_dataset,width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        take_photo_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)

        #update photo button
        update_photo_btn=Button(btn_frame,text="Update Pic",width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        update_photo_btn.grid(row=0,column=5,padx=5,pady=10,sticky=W)





        #----------------------------------------------------------------------
        # Right Label Frame 
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="navyblue")
        Right_frame.place(x=750,y=10,width=720,height=580)

        img_right=Image.open("images\\search.jpg")
        img_right=img_right.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
         
        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)

        #Searching System in Right Label Frame 
        search_frame = LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("verdana",12,"bold"),fg="navyblue")
        search_frame.place(x=5,y=135,width=710,height=70)

        #Phone Number
        search_label = Label(search_frame,text="Search By:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        self.var_searchTX=StringVar()
        #combo box 
        search_combo=ttk.Combobox(search_frame,width=12,font=("verdana",12,"bold"),state="readonly")
        search_combo["values"]=("Select","Roll-No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        self.var_search=StringVar()
        search_entry = ttk.Entry(search_frame,width=12,font=("verdana",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show All",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        showAll_btn.grid(row=0,column=4,padx=4)

        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=350)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
           #create table 
        self.student_table = ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSample")
        self.student_table["show"]="headings"
        
        

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=90)
        self.student_table.column("dob",width=90)
        self.student_table.column("email",width=150)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()



    #====================functions declartion=======
    def add_data(self):
      if self.var_dep.get()=="Select Department" or self.var_course.get=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_div.get()=="Select division" or self.var_roll.get()=="" or self.var_gender.get()=="Select Gender" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
      
      else:
        
              try: 
                conn = mysql.connector.connect(username="root", password="Riraj2809@",host="localhost",database="facial_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",( 
                                                                                                               self.var_dep.get(),
                                                                                                               self.var_course.get(),
                                                                                                               self.var_year.get(),
                                                                                                               self.var_semester.get(),
                                                                                                               self.var_std_id.get(),
                                                                                                               self.var_std_name.get(),
                                                                                                               self.var_div.get(),
                                                                                                               self.var_roll.get(),
                                                                                                               self.var_gender.get(),
                                                                                                               self.var_dob.get(),
                                                                                                               self.var_email.get(),
                                                                                                               self.var_phone.get(),
                                                                                                               self.var_address.get(),
                                                                                                               self.var_teacher.get(),
                                                                                                               self.var_radio1.get()
                                                                                                          
                                                                                                             ))

                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
 
        
              except Exception as es:
                  messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)

#========================fetch data===========================
    def  fetch_data(self):
        conn = mysql.connector.connect(username="root", password="Riraj2809@",host="localhost",database="facial_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())          
          
            for i in data:
                self.student_table.insert("",END,values=i)

            conn.commit()
            
        conn.close()  


  #==============================get cursor==================================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
    
    #=========update function==========
    def update_data(self):
         if self.var_dep.get()=="Select Department" or self.var_course.get=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_div.get()=="Select division" or self.var_roll.get()=="" or self.var_gender.get()=="Select Gender" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
             messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
         else:
              try:
                  Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                  if Update>0:  
                     conn = mysql.connector.connect(username="root", password="Riraj2809@",host="localhost",database="facial_recognizer")
                     my_cursor = conn.cursor()                                                                                                                
                     my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,`Address`=%s,`Teacher`=%s,PhotoSample=%s where StudentId=%s",(
                                                                                                               self.var_dep.get(),
                                                                                                               self.var_course.get(),
                                                                                                               self.var_year.get(),
                                                                                                               self.var_semester.get(),
                                                                                                               self.var_std_name.get(),
                                                                                                               self.var_div.get(),
                                                                                                               self.var_roll.get(),
                                                                                                               self.var_gender.get(),
                                                                                                               self.var_dob.get(),
                                                                                                               self.var_email.get(),
                                                                                                               self.var_phone.get(),
                                                                                                               self.var_address.get(),
                                                                                                               self.var_teacher.get(),
                                                                                                               self.var_radio1.get(),
                                                                                                               self.var_std_id.get()
                                                                                                               ))
                  else:
                      if not Update:
                         return 
                  messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                  conn.commit()
                  self.fetch_data()
                  conn.close()
              except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

        #=====================delete function===========
    def delete_data(self):
        if self.var_std_id.get()=="":
               messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student details",parent=self.root)
                if delete>0:  
                       conn = mysql.connector.connect(username="root", password="Riraj2809@",host="localhost",database="facial_recognizer")
                       my_cursor = conn.cursor()
                       sql="delete from student where StudentId=%s"    
                       val=(self.var_std_id.get(),)
                       my_cursor.execute(sql,val)

                else:
                        if not delete:
                           return 
                     
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                     messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
#===============reset===================
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select divison"),
        self.var_roll.set(""),
        self.var_gender.set("Select Gender"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")

  #====================Generate data set or Take photo Samples=================

    def generate_dataset(self):
         if self.var_dep.get()=="Select Department" or self.var_course.get=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_div.get()=="Select division" or self.var_roll.get()=="" or self.var_gender.get()=="Select Gender" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
         else:
             try:
                 conn = mysql.connector.connect(username="root", password="Riraj2809@",host="localhost",database="facial_recognizer")
                 my_cursor = conn.cursor() 
                 my_cursor.execute("select * from student")
                 myresult=my_cursor.fetchall()
                 id=0
                 for x in myresult:
                     id+=1
                 my_cursor.execute("Update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where StudentId=%s",(
                                                                                                                                                                                                                                  self.var_dep.get(),
                                                                                                                                                                                                                                  self.var_year.get(),
                                                                                                                                                                                                                                  self.var_semester.get(),
                                                                                                                                                                                                                                  self.var_std_name.get(),
                                                                                                                                                                                                                                  self.var_div.get(),
                                                                                                                                                                                                                                  self.var_roll.get(),
                                                                                                                                                                                                                                  self.var_gender.get(),
                                                                                                                                                                                                                                  self.var_course.get(),
                                                                                                                                                                                                                                  self.var_dob.get(),
                                                                                                                                                                                                                                  self.var_email.get(),
                                                                                                                                                                                                                                  self.var_phone.get(),
                                                                                                                                                                                                                                  self.var_address.get(),
                                                                                                                                                                                                                                  self.var_teacher.get(),
                                                                                                                                                                                                                                  self.var_radio1.get(),
                                                                                                                                                                                                                                  self.var_std_id.get()==id+1
                                                                                                                                                                                                                                 ))
                 conn.commit()
                 self.fetch_data()
                 self.reset_data()
                 conn.close()

 
                 #=================Load predefine data on face frontals from opencv======

                 face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                 
                 def face_croped(img):
                     gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                     faces=face_classifier.detectMultiScale(gray,1.3,5)
                     #scaling factor=1.3
                     #Minimum Neighbir=5

                     for(x,y,w,h) in faces:
                         face_croped=img[y:y+h ,x:x+w]
                         return face_croped
                 cap=cv2.VideoCapture(0)
                 img_id=0
                 while True:
                     ret,my_frame=cap.read()
                     if face_croped(my_frame) is not None:
                         img_id+=1
                         face=cv2.resize(face_croped(my_frame),(450,450))
                         face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                         file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                         cv2.imwrite(file_name_path,face)
                         cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                         cv2.imshow("Capture Images",face)

                     if cv2.waitKey(1)==13 or int(img_id)==100:
                         break
                 cap.release()
                 cv2.destroyAllWindows()
                 messagebox.showwarning("Result","Generating data sets completed!")
             except Exception as es:
                   messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)




                

           



# main class object

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)

    root.mainloop()