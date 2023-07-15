from tkinter import *
from tkinter import messagebox,filedialog
from PIL import Image, ImageTk
import exstuser
import admin1
import adduser
import updateuser
import delusr

class Frame1:
    def __init__(self):
        self.root=Tk()
        self.root.geometry('1000x600')
        self.root.resizable(False,False)

        self.frm1=Frame(self.root)
        self.frm1.place(x=0,y=0,width=1000,height=100)
        self.frm1.config(bg="black")

        self.btnlg=Button(self.root,text="SIGN OUT",command=self.signout)
        self.btnlg.place(x=850,y=25,width=130,height=50)
        self.btnlg.config(fg="black",font=("Times",16,"bold"),bg="red")

        self.lbl1=Label(self.frm1,text="ADMIN PANEL")
        self.lbl1.place(x=50,y=25,width=200,height=50)
        self.lbl1.config(bg="black",fg="white",font=("Times",22,"bold"))

        self.frmpic=Frame(self.root)
        self.frmpic.place(x=100,y=150,width=300,height=300)
        self.frmpic.config(bg="black")

        self.img = Image.open('image/love.JPG').resize((250, 250))
        self.imgTk = ImageTk.PhotoImage(self.img)
        self.imgLbl = Label(self.frmpic, image = self.imgTk,bg='black')
        self.imgLbl.place(x = 25, y = 25,height=250,width=250)

        self.lbl1=Label(self.root,text="WELCOME LOVEPREET!")
        self.lbl1.place(x=500,y=150,width=500,height=50)
        self.lbl1.config(fg="black",font=("Times",26,"bold"))

        self.lbl2=Label(self.root,text="TOTAL STUDENTS : 220")
        self.lbl2.place(x=500,y=215,width=500,height=50)
        self.lbl2.config(fg="black",font=("Times",20,"bold"))

        self.lbl3=Label(self.root,text="PRESENT STUDENTS : 210")
        self.lbl3.place(x=500,y=280,width=500,height=50)
        self.lbl3.config(fg="black",font=("Times",20,"bold"))

        self.lbl4=Label(self.root,text="ABSENT STUDENTS : 10")
        self.lbl4.place(x=500,y=345,width=500,height=50)
        self.lbl4.config(fg="black",font=("Times",20,"bold"))

        self.btn=Button(self.root,text="EXISTING STUDENTS",command=self.ext)
        self.btn.place(x=550,y=400,width=400,height=50)
        self.btn.config(fg="black",font=("Times",20,"bold"))

        self.btn=Button(self.root,text="ADD",command=self.add)
        self.btn.place(x=225,y=500,width=150,height=50)
        self.btn.config(fg="black",font=("Times",20,"bold"),bg="green")

        self.btn=Button(self.root,text="UPDATE",command=self.updt)
        self.btn.place(x=425,y=500,width=150,height=50)
        self.btn.config(fg="black",font=("Times",20,"bold"),bg="yellow")
        
        self.btn=Button(self.root,text="DELETE",command=self.delete)
        self.btn.place(x=625,y=500,width=150,height=50)
        self.btn.config(fg="black",font=("Times",20,"bold"),bg="red")
        

        self.root.mainloop()
    def ext(self):
        self.root.destroy()
        exstuser.frame4()

    def signout(self):
        self.root.destroy()
        admin1.Frame1()
    
    def add(self):
        self.root.destroy()
        adduser.Frame1()

    def updt(self):
        self.root.destroy()
        updateuser.Frame1()
    
    def delete(self):
        self.root.destroy()
        delusr.frame4()
        
if __name__=='__main__':
    Frame1()