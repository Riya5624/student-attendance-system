from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import os
import cv2
import mysql.connector
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self,root):
         self.root=root
         self.root.geometry("1530x790+0+0")
         self.root.title("face Recognition System")


         title=Label(self.root,text="FACE DETECT",font=("Helvetica",34,"bold"),bg="white",fg="#74b3ce")
         title.place(x=0,y=0,width=1530,height=45)


         img_top=Image.open("C:\\Users\\riyan\\OneDrive\\Desktop\\Attendance System\\images\\t3.jpeg")
         img_top=img_top.resize((650,700),Image.ANTIALIAS)
         self.photoimg_top=ImageTk.PhotoImage(img_top)
         
         f_lbl=Label(self.root,image=self.photoimg_top)
         f_lbl.place(x=0,y=55,width=600,height=700)

         
         img_top1=Image.open("C:\\Users\\riyan\\OneDrive\\Desktop\\Attendance System\\images\\t2.jpg")
         img_top1=img_top1.resize((950,700),Image.ANTIALIAS)
         self.photoimg_top1=ImageTk.PhotoImage(img_top1)
         
         f_lbl=Label(self.root,image=self.photoimg_top1)
         f_lbl.place(x=650,y=55,width=950,height=700)
        
         b1_1=Button(f_lbl,text="Face Detect",cursor="hand2",command=self.face_detect,font=("Patua One",18,"bold"),bg="#1034A6",fg="white")
         b1_1.place(x=365,y=620,width=200,height=40)

         #==================attendance=========================
    def mark_attendance(self,n,i,r,d):
          with open("attenddance.csv","r+",newline="\n") as f:
               myDatalist=f.readlines()
               name_list=[]
               for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])

               if((i not in name_list)) and ((r not in name_list)) and ((n not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {r}, {n},{d}, {dtString}, {d1}, Present")
                

               




         #=====================face detect===================

    def face_detect(self):
              def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
                  gray_image= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                  features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

                  coord=[]
                  
                  for (x,y,w,h) in features:
                       cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0,),3)
                       id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                       
                       confidence=int((100*(1-predict/300)))
                       
                       conn = mysql.connector.connect(username="root", password="Riraj2809@",host="localhost",database="facial_recognizer")
                       my_cursor = conn.cursor() 

                       my_cursor.execute("select StudentId from student where StudentId="+str(id))
                       i=my_cursor.fetchone()
                       i="+".join(i)

                       
                       my_cursor.execute("select Name from student where StudentId="+str(id))
                       n=my_cursor.fetchone()
                       n="+".join(n)

                       my_cursor.execute("select Roll from student where StudentId="+str(id))
                       r=my_cursor.fetchone()
                       r="+".join(r)

                       my_cursor.execute("select Department from student where StudentId="+str(id))
                       d=my_cursor.fetchone()
                       d="+".join(d)

                      

                       
                       if confidence > 77:
                               cv2.putText(img,f"StudentId:{i}",(x,y-120),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                              
                               cv2.putText(img,f"Name:{n}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                               
                               cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                               cv2.putText(img,f"Department:{d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                               self.mark_attendance(i,r,n,d)
                       else:
                               cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255,),3)
                               cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                       coord=[x,y,w,h]
                  return coord
              def recognize(img,clf,faceCascade):
                     coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
                     return img
              faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
              clf=cv2.face.LBPHFaceRecognizer_create()
              clf.read("classifier.xml")

              videoCap=cv2.VideoCapture(0)

              while True:
                        ret,img=videoCap.read()
                        img=recognize(img,clf,faceCascade)
                        cv2.imshow("Welcome to Face Detection",img)

                        if cv2.waitKey(1)==13:
                             break
              videoCap.release()
              cv2.destroyAllWindows()
                        



                             
                             
if __name__=="__main__":
     root=Tk()
     obj=Face_Recognition(root)
     root.mainloop()