from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
class ChatBot:
    def __init__(self,root): 
       self.root=root
       self.root.title("ChatBot")
       self.root.geometry("730x620+0+0")
       self.root.bind("<Return>",self.enter_func)
      
       main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
       main_frame.pack()

       img_chat=Image.open("images\\chatbot.jpg")
       img_chat=img_chat.resize((200,70),Image.ANTIALIAS)
       self.photoimg=ImageTk.PhotoImage(img_chat)

       Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text="Chat With Me ",font=('arial',30,'bold'),fg='powder blue',bg='white')
       Title_label.pack(side=TOP)
       self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
       self.text=Text(main_frame,width=65,height=20,bd=20,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
       self.scroll_y.pack(side=RIGHT,fill=Y)
       self.text.pack()

       btn_frame=Frame(self.root,bd=4,bg='white',width=730)
       btn_frame.pack()

       label_l=Label(btn_frame,text="Type something",font=('arial',14,'bold'),fg='powder blue',bg='black')
       label_l.grid(row=0,column=0,padx=5,sticky=W)

       self.entry=StringVar()

       self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('arial',16,'bold'))
       self.entry1.grid(row=0,column=0,padx=5,sticky=W)

       self.send=Button(btn_frame,text="Send>>",command=self.send,font=('arial',15,'bold'),width=8,bg='powder blue',)
       self.send.grid(row=0,column=2,padx=5,sticky=W)

       self.clear=Button(btn_frame,text="Clear Data",command=self.clear,font=('arial',15,'bold'),width=8,bg='powder blue')
       self.clear.grid(row=0,column=10,padx=5,sticky=W)   

       self.msg=''

       self.label_ll=Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='powder blue',bg='black')
       self.label_ll.grid(row=1,column=1,padx=5,sticky=W)



    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')
        
    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')
        



    def send(self):
        send="\t\t\t"+"You:"+self.entry.get()
        self.text.insert(END,'\n'+send)  
        self.text.yview(END)
        if(self.entry.get()==''):
            self.msg="Please enter some input"
            self.label_ll.config(text=self.msg,fg='powder blue')
        else:
            self.msg=''
            self.label_ll.config(text=self.msg,fg='powder blue')

        if (self.entry.get()=="hello"):
            self.text.insert(END,"\n\n"+"Bot: Hello!\nHow may I help you?")

        elif (self.entry.get()=='how does facial recognition work?'):
            self.text.insert(END,'\n\n'+'Bot: step 1:face detection.The Camera\ndetecs and located the image of a face,\neither alone or in a crowd....\nStep 2:Face analysis.Next,an image of\n the face is captured and analyzed')

        else:
            self.text.insert(END,"\n\n"+"Bot: sorry I don't have answer of\nthis question,\nyou can mail your query to\nriyanegi658@gmail.com")


















if __name__ == "__main__":
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()