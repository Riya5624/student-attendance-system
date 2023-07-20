from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title=Label(self.root,text="TRAIN DATA SET",font=("Helvetica",34,"bold"),bg="white",fg="#74b3ce")
        title.place(x=0,y=0,width=1530,height=45)


        img_top=Image.open("C:\\Users\\riyan\\OneDrive\\Desktop\\Attendance System\\images\\t2.jpg")
        img_top=img_top.resize((500,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
         
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=500,height=325)

         
        img_top1=Image.open("C:\\Users\\riyan\\OneDrive\\Desktop\\Attendance System\\images\\t1.jpg")
        img_top1=img_top1.resize((500,325),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)
         
        f_lbl=Label(self.root,image=self.photoimg_top1)
        f_lbl.place(x=500,y=55,width=500,height=325)
         
         
        img_top2=Image.open("C:\\Users\\riyan\\OneDrive\\Desktop\\Attendance System\\images\\t3.jpeg")
        img_top2=img_top2.resize((550,325),Image.ANTIALIAS)
        self.photoimg_top2=ImageTk.PhotoImage(img_top2)
         
        f_lbl=Label(self.root,image=self.photoimg_top2)
        f_lbl.place(x=1000,y=55,width=500,height=325)
 

  
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("Patua One",40,"bold"),bg="#1034A6",fg="white")
        b1_1.place(x=0,y=380,width=1530,height=60)



        img_bottom=Image.open("C:\\Users\\riyan\\OneDrive\\Desktop\\Attendance System\\images\\t2.jpg")
        img_bottom=img_bottom.resize((500,325),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
         
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=500,height=325)

         
        img_bottom1=Image.open("C:\\Users\\riyan\\OneDrive\\Desktop\\Attendance System\\images\\t1.jpg")
        img_bottom1=img_bottom1.resize((500,325),Image.ANTIALIAS)
        self.photoimg_bottom1=ImageTk.PhotoImage(img_bottom1)
         
        f_lbl=Label(self.root,image=self.photoimg_bottom1)
        f_lbl.place(x=500,y=440,width=500,height=325)
  
        img_bottom2=Image.open("C:\\Users\\riyan\\OneDrive\\Desktop\\Attendance System\\images\\t3.jpeg")
        img_bottom2=img_bottom2.resize((550,325),Image.ANTIALIAS)
        self.photoimg_bottom2=ImageTk.PhotoImage(img_bottom2)
         
        f_lbl=Label(self.root,image=self.photoimg_bottom2)
        f_lbl.place(x=1000,y=440,width=500,height=325)
        
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]

        faces=[]
        ids=[]


        for image in path:
            img=Image.open(image).convert('L') #Gray Scale Image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        #============================Train the classifier and save============

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!")





        




        

       
        
         


if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()