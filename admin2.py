from tkinter import *
from tkinter import messagebox,filedialog
import db
import admin3
# import admin1

class Frame1:
    def __init__(self):
        self.root=Tk()
        self.root.title("ADMIN LOGIN")
        self.root.geometry('1000x600')
        self.root.resizable(False,False)

        self.frm1=Frame(self.root)
        self.frm1.place(x=0,y=0,width=1000,height=100)
        self.frm1.config(bg="black")

        self.lbl=Label(self.frm1,text="ADMIN LOGIN")
        self.lbl.place(x=320,y=25,width=350,height=50)
        self.lbl.config(bg="black",fg="white",font=("Times",22,"bold"))
        
        # self.btn=Button(self.frm1,text="BACK",command=self.bck)
        # self.btn.place(x=25,y=25,width=100,height=40)
        # self.btn.config(font=18)

        self.lbl1=Label(self.root,text="USERNAME")
        self.lbl1.place(x=300,y=150,width=400,height=50)
        self.lbl1.config(font=("Times",16,"bold"))

        self.etn=Entry(self.root)
        self.etn.place(x=300,y=200,width=400,height=30)

        self.lbl2=Label(self.root,text="PASSWORD")
        self.lbl2.place(x=300,y=250,width=400,height=50)
        self.lbl2.config(font=("Times",16,"bold"))

        self.etn1=Entry(self.root)
        self.etn1.place(x=300,y=300,width=400,height=30)

        self.btn=Button(self.root,text="LOGIN",command=self.check)
        self.btn.place(x=450,y=400,width=100,height=50)
        self.btn.config(font=("Times",16,"bold"))

        def on_enter(e):
            self.btn['background'] = 'green'

        def on_leave(e):
            self.btn['background'] = 'SystemButtonFace'


        self.btn.bind("<Enter>", on_enter)
        self.btn.bind("<Leave>", on_leave)



        self.root.mainloop()

    def check(self):
        u=self.etn.get()
        p=self.etn1.get()
        data=(u,p)
        res=db.login(data)
        print(res)
        if res:
            self.root.destroy()
            admin3.Frame1()
        else:
            messagebox.showerror("Invalid","Username and Password incorrect")


    # def bck(self):
    #     self.root.destroy()
    #     # admin1.Frame1()

if __name__=='__main__':
    Frame1()