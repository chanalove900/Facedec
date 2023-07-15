from tkinter import *
from tkinter import messagebox,filedialog
import User2
from PIL import Image, ImageTk
import sample

class Frame1:
    def __init__(self):
        self.root=Tk()
        self.root.geometry('1000x600')
        self.root.resizable(False,False)
        self.root.config(bg="white")

        # self.frm1=Frame(self.root)
        # self.frm1.place(x=0,y=0,width=1000,height=100)
        # self.frm1.config(bg="black")

        self.frm2=Frame(self.root)
        self.frm2.place(x=300,y=150,width=400,height=300)
        self.frm2.config(bg="black")

        self.img = Image.open('img3.jpg').resize((1000, 600))
        self.imgTk = ImageTk.PhotoImage(self.img)
        self.imgLbl = Label(self.root, image = self.imgTk)
        self.imgLbl.place(x = 0, y = 0,height=600,width=1000)


        self.btn=Button(self.root,text="launh cam!",command=self.detail)
        self.btn.place(x=150,y=400,height=50,width=200)
        self.btn.config(font=("Times",16))



        # self.etn=Entry(self.root)
        # self.etn.place(x=650,y=500,width=200,height=30)
        def on_enter(e):
            self.btn['background'] = 'green'

        def on_leave(e):
            self.btn['background'] = 'SystemButtonFace'


        self.btn.bind("<Enter>", on_enter)
        self.btn.bind("<Leave>", on_leave)


        self.root.mainloop()
    def detail(self):
        # data=self.etn.get()
        self.root.destroy()
        sample.capt()
        User2.Frame1()

        

if __name__=='__main__':
    Frame1()