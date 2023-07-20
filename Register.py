from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # ============ Variables =================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_security_Q=StringVar()
        self.var_security_A=StringVar()
        self.var_pwd=StringVar()
        self.var_cpwd=StringVar()
        self.var_check=IntVar()

        self.bg=ImageTk.PhotoImage(file=r"images\\bg2.jpg")
        
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0, relwidth=1,relheight=1)

        self.bg1=ImageTk.PhotoImage(file=r"images\\face.jpg")
        
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100, width=470,height=550)

        frame= Frame(self.root,bg="#F2F2F2")
        frame.place(x=520,y=100,width=800,height=550)

        
        

        # img1=Image.open(r"C:\Users\Muhammad Waseem\Documents\Python_Test_Projects\Images_GUI\reg1.png")
        # img1=img1.resize((450,100),Image.ANTIALIAS)
        # self.photoimage1=ImageTk.PhotoImage(img1)
        # lb1img1 = Label(image=self.photoimage1,bg="#F2F2F2")
        # lb1img1.place(x=300,y=100, width=500,height=100)
        

        register_lbl = Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="#002B53",bg="#F2F2F2")
        register_lbl.place(x=20,y=20)

        #label1 
        fname = Label(frame,text="First Name:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        fname.place(x=50,y=100)
        fname_entry=ttk.Entry(frame,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        lname = Label(frame,text="Last Name:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        lname.place(x=370,y=100)

        

        #entry2 
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)

        # ==================== section 2 -------- 2nd Columan===================

        #label1 
        contact = Label(frame,text="Contact No:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        contact.place(x=50,y=170)

        #entry1 
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)


        #label2 
        email = Label(frame,text="Email:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        email.place(x=370,y=170)

        #entry2 
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)

        # ========================= Section 3 --- 1 Columan=================

        #label1 
        security_Q = Label(frame,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        security_Q.place(x=50,y=240)

        #Combo Box1
        self.combo_security_Q = ttk.Combobox(frame,textvariable=self.var_security_Q,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
        
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)


        #label2 
        security_A = Label(frame,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        security_A.place(x=370,y=240)

        #entry2 
        self.txt_security=ttk.Entry(frame,textvariable=self.var_security_A,font=("times new roman",15,"bold"))
        self.txt_security.place(x=370,y=270,width=250)

        # ========================= Section 4-----Column 2=============================

        #label1 
        pswd = Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        pswd.place(x=50,y=310)

        #entry1 
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)


        #label2 
        confirm_pswd = Label(frame,text="Confirm Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        confirm_pswd.place(x=370,y=310)

        #entry2 
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_cpwd,font=("times new roman",15,"bold"))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        # Checkbutton
        checkbtn = Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("times new roman",13,"bold"),onvalue=0,fg="#002B53",bg="#F2F2F2")
        checkbtn.place(x=50,y=380)


        # Creating Button Register
        register_btn=Button(frame,command=self.register_data,text="Register",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        register_btn.place(x=50,y=420,width=200,height=35)

        # Creating Button Login
        loginbtn=Button(frame,text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=340,y=420,width=200,height=35)

        




    def register_data(self):
        if (self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_contact.get()=="" or self.var_email.get()=="" or self.var_security_Q.get()=="Select" or self.var_security_A.get()=="" or self.var_pwd.get()=="" or self.var_cpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.var_pwd.get() != self.var_cpwd.get()):
            messagebox.showerror("Error","Please Enter Password & Confirm Password are security_Ame!")
        elif(self.var_check.get()==0):
            messagebox.showerror("Error","Please Check the Agree Terms and Conditons!")
        else:
             
            try:
                conn = mysql.connector.connect(username="root", password="Riraj2809@",host="localhost",database="facial_recognizer")
                mycursor = conn.cursor()
                query=("select * from regteach where email=%s")
                value=(self.var_email.get(),)
                mycursor.execute(query,value)
                row=mycursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist,please try another email")
                else:
                    mycursor.execute("insert into regteach values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_security_Q.get(),
                    self.var_security_A.get(),
                    self.var_pwd.get()
                    ))

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Successfully Registerd!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)




if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()