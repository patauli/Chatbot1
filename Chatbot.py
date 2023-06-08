From tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk     # Pip install pillow


class Chatbot:
  def __init__(self,root):
    self.root=root
    self.root.title("ChatBot")
    self.root.geometry("730x620+0+0")
    
    
    main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
    main_frame.pack()
    
    img_chat=Image.open('chat.jpg')
    img_chat=img_chat.resize((200,70),Image.ANTIALIAS)
    self.photoimg=ImageTk.PhotoImage(img_chat)
    
    Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,image=self.photoimg,text='CHAT ME',font=(arial',30,'bold'),fg='green',bg='white')
    Title_label.pack(side=TOP)
    
    
    if __name__ == '__main__':
      root=Tk()
      obj=ChatBot(root)
      
