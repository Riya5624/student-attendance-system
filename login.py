from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

import mysql.connector
# --------------------------
from train import Train
from main import Face_Recognition_System

import os
from Register import Register

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # variables 
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_password=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"images\\bg1.jpg")
        
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame= Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"images\\login.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        
        lb1img1 = Label(image=self.photoimage1,bg="black",borderwidth=0)
        lb1img1.place(x=730,y=175, width=100,height=100)

        get_str = Label(frame,text="Login",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #label1 
        username =lb1= Label(frame,text="Username:",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        #entry1 
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)


        #label2 
        password =lb1= Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        #entry2 
        self.txtpassword=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpassword.place(x=40,y=250,width=270)

        #============================Icon Image==========================

        img2=Image.open(r"images\\login.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        
        lb1img2 = Label(image=self.photoimage2,bg="black",borderwidth=0)
        lb1img2.place(x=650,y=323, width=25,height=25)

        img3=Image.open(r"images\\password.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        
        lb1img3 = Label(image=self.photoimage3,bg="black",borderwidth=0)
        lb1img3.place(x=650,y=395, width=25,height=25)


        # Creating Button Login
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="white",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=110,y=300,width=120,height=35)


        # Creating Button Registration
        registerbtn=Button(frame,command=self.register_window,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="orange",activebackground="blue")
        registerbtn.place(x=15,y=350,width=160)


        # Creating Button Forget
        forgetbtn=Button(frame,command=self.forget_password,text="Forget password",font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="orange",activebackground="blue")
        forgetbtn.place(x=9,y=370,width=160)


    #  THis function is for open register window
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if (self.txtuser.get()=="" or self.txtpassword.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.txtuser.get()=="admin" and self.txtpassword.get()=="admin"):
            messagebox.showinfo("Sussessfully","Welcome to Attendance Managment System Using Facial Recognition")
        else:
            # messagebox.showerror("Error","Please Check Username or Password !")
            conn = mysql.connector.connect(username="root", password="Riraj2809@",host="localhost",database="facial_recognizer")
            mycursor = conn.cursor()
            mycursor.execute("select * from regteach where email=%s and password=%s",(
                self.txtuser.get(),
                self.txtpassword.get()
            ))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!")
            else:
                open_main=messagebox.askyesno("YesNo","Access only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                    
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()






#=======================Reset Passowrd Function=============================
    def reset_pass(self):
        if self.var_ssq.get()=="Select":
            messagebox.showerror("Error","Select the Security Question!",parent=self.root2)
        elif(self.var_sa.get()==""):
            messagebox.showerror("Error","Please Enter the Answer!",parent=self.root2)
        elif(self.var_password.get()==""):
            messagebox.showerror("Error","Please Enter the New Password!",parent=self.root2)
        else:
            conn = mysql.connector.connect(username="root", password="Riraj2809@",host="localhost",database="facial_recognizer")
            mycursor = conn.cursor()
            query=("select * from regteach where email=%s and ss_que=%s and s_ans=%s")
            value=(self.txtuser.get(),self.var_ssq.get(),self.var_sa.get())
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Answer!",parent=self.root2)
            else:
                query=("update regteach set password=%s where email=%s")
                value=(self.var_password.get(),self.txtuser.get())
                mycursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Successfully Your password has been rest, Please login with new Password!",parent=self.root2)
                



# =====================Forget window=========================================
    def forget_password(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email ID to reset Password!")
        else:
            conn = mysql.connector.connect(username="root", password="Riraj2809@",host="localhost",database="facial_recognizer")
            mycursor = conn.cursor()
            query=("select * from regteach where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please Enter the Valid Email ID!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("400x400+610+170")
                l=Label(self.root2,text="Forget Password",font=("times new roman",30,"bold"),fg="black",bg="#fff")
                l.place(x=0,y=10,relwidth=1)
                # -------------------fields-------------------
                #label1 
                ssq =lb1= Label(self.root2,text="Select Security Question:",font=("times new roman",15,"bold"),fg="black",bg="#F2F2F2")
                ssq.place(x=70,y=80)

                #Combo Box1
                self.combo_security = ttk.Combobox(self.root2,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
                self.combo_security.current(0)
                self.combo_security.place(x=70,y=110,width=270)


                #label2 
                sa =lb1= Label(self.root2,text="Security Answer:",font=("times new roman",15,"bold"),fg="black",bg="#F2F2F2")
                sa.place(x=70,y=150)

                #entry2 
                self.txtpassword=ttk.Entry(self.root2,textvariable=self.var_sa,font=("times new roman",15,"bold"))
                self.txtpassword.place(x=70,y=180,width=270)

                #label2 
                new_password =lb1= Label(self.root2,text="New Password:",font=("times new roman",15,"bold"),fg="black",bg="#F2F2F2")
                new_password.place(x=70,y=220)

                #entry2 
                self.new_password=ttk.Entry(self.root2,textvariable=self.var_password,font=("times new roman",15,"bold"))
                self.new_password.place(x=70,y=250,width=270)

                # Creating Button New Password
                loginbtn=Button(self.root2,command=self.reset_pass,text="Reset Password",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="black",activeforeground="white",activebackground="#007ACC")
                loginbtn.place(x=70,y=300,width=270,height=35)


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
   main()