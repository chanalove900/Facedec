from tkinter import *
from tkinter import messagebox,filedialog
import admin2 ,adminfce,admin3

class Frame1:
    def __init__(self):
        self.root=Tk()
        self.root.geometry('1000x600')
        self.root.resizable(False,False)

        self.frm1=Frame(self.root)
        self.frm1.place(x=0,y=0,width=1000,height=100)
        self.frm1.config(bg="black")
        
        self.frm2=Frame(self.root)
        self.frm2.place(x=300,y=150,width=400,height=300)
        self.frm2.config(bg="black")

        # self.btn=Button(self.root,text="Face ID",command=self.face)
        # self.btn.place(x=250,y=520,height=50,width=200)
        # self.btn.config(font=("Times",16))

        self.btn2=Button(self.root,text="User ID",command=self.login)
        self.btn2.place(x=550,y=520,height=50,width=200)
        self.btn2.config(font=("Times",16))

        # self.lbl1=Label(self.root,text="OR")
        # self.lbl1.place(x=475,y=520,width=50,height=50)
        # self.lbl1.config(font=18)

        # self.lbl2=Label(self.root,text="LOGIN BY")
        # self.lbl2.place(x=430,y=460,width=150,height=50)
        # self.lbl2.config(font=("Times",22,"bold"))



        self.root.mainloop()
    def login(self):
        self.root.destroy()
        admin2.Frame1()
    def face(self):
        a1=adminfce.capt()
        if a1:
            admin3.Frame1()
        else:
            messagebox.showwarning("ATTENTION","you ain't USER")


if __name__=='__main__':
    Frame1()