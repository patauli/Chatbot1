from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk     # Pip install pillow


class Chatbot:
  def __init__(self,root):
    self.root=root
    self.root.title("ChatBot")
    self.root.geometry("730x620+0+0")
    self.root.bind('<Return>',self.enter_func)
    
    
    main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
    main_frame.pack()
    
    img_chat=Image.open('chat.jpg')
    img_chat=img_chat.resize((200,70),Image.ANTIALIAS)
    self.photoimg=ImageTk.PhotoImage(img_chat)
    
    Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,image=self.photoimg,text='CHAT ME',font=('arial',30,'bold'),fg='green',bg='white')
    Title_label.pack(side=TOP)


    self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
    self.text=Text(main_frame,width=65,height=20,bd=20,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
    self.scroll_y.pack(side=RIGHT,fill=Y) 
    self.text.pack()


    btn_frame=Frame(self.root,bd=4,bg='white',width=730)
    btn_frame.pack

    label=Label(btn_frame,text="type Something",font=('arial',14,'bold'),fg='green',bg='white')
    label_1.grid(row=0,column=0,padx=5,sticky=W)

    self.entry=StringVar()
    self.entry=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('times new roman',16,'bold'))
    self.entry.grid(row=0,column=1,padx=5,sticky=W)

    self.send=Button(btn_frame,text="Send>>",font=('arial',15,'bold'),width=8,bg='green')
    self.send.grid(row=0,column=2,padx=5,sticky=W)

    self.clare=Button(btn_frame,text="Clear Data",command=self.clear,font=('arial',15,'bold'),width=8,bg='red',fg='white')
    self.clare.grid(row=1,column=0,padx=5,sticky=W)

    self.msg=''
    self.label_11=Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='red',bg='white')
    self.label_11.grid(row=1,column=1,padx=5,sticky=W)



    #. <<<<<<<<<<<<<<<<<<<<<<<<<<<Function Declaration>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def enter_func(self,event):
       self.send.invoke()
       self.entry.set('')

    def clear(self):
       self.text.delete('1.0',END)
       self.entry.set()



    def send(self):
        send='\t\t\t'+'You:  '+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if (self.entry.get()==''):
           self.msg='Please enter some input'
           self.label_11.config(text=self.msg,fg='red')


        else:
           self.msg=''
           self.label_11.config(text=self.msg,fg='red')

        if (self.entry.get()=='hello'):
           self.text.insert(END,'\n\n'+'Bot:Hi')

        if (self.entry.get()=='hello'):
            self.text.insert(END,'\n\n'+'Bot:Hi')

        elif (self.entry.get()=='hi'):
           self.text.insert(END,"\n\n"+"Bot: Hello")

        elif (self.entry.get()=="How are you"):
           self.text.insert(END,"\n\n"+"Bot: fine and you")

        elif (self.entry.get()=="Fantastic"): 
           self.text.insert(END,"\n\n"+"Bot: Nice to hear")

        elif (self.entry.get()=="who created you"):
           self.text.insert(END,"\n\n"+"Bot: Sandeep did using python")

        elif (self.entry.get()=="what is your name"):
           self.text.insert(END,"\n\n"+"Bot: My name is Sus bot")

        elif (self.entry.get()=="Can you speak Marathi"):
           self.text.insert(END,"\n\n"+"Bot: I'm still learning it..")

        elif (self.entry.get()=="What is machine learning"):
           self.text.insert(END,"\n\n"+"Bot: Machine learning is a brancho\nof artificial intelligence")

        elif (self.entry.get()=="How does facial recognition works"):
           self.text.insert(END,"\n\n"+"Bot: Facial recognition is a way of\nrecognizing a human face\nthrough technology.")

        elif (self.entry.get()=="How facial recognition work step by step"):
           self.text.insert(END,"\n\n"+"Bot: Step1: Face Detection. The Camera\n detects and locates the image of\n the human face. Step 2: It reads \n through the parameters and collects\n the data sets. Step3: \n then it verifies using data pointers from the storage and \n gives the inputs")
    
        elif (self.entry.get()=="How many countries are use facial recognition?"):
           self.text.insert(END,"\n\n"+"Bot: In use 98\nApproved, but not implemented 12\nconsidering facial recognition in tech")

        elif (self.entry.get()=="what is python programming"):
           self.text.insert(END,"\n\n"+"Bot: Python is a general purpose\nand high level programming language. \nYou can use python to program using simple syntax")
           
        elif (self.entry.get()=="What is a chatbot?"):
           self.text.insert(END,"\n\n"+"Bot: A Chatbot is a computer \nprogram that's designed to\nsimulate human conversation  ")
    
        elif (self.entry.get()=="bye"):
           self.text.insert(END,"\n\n"+"Bot: Thank You for chatting")
           
           
           



    
    
    if __name__ == '__main__':
      root=Tk()
      obj=ChatBot(root)
      
