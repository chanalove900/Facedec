from tkinter import *
from tkinter import messagebox,filedialog
from PIL import Image, ImageTk
from tkinter import  ttk
import db
import admin3

class Frame1:
    vals=''
    id=''
    def __init__(self):
        self.root=Tk()
        self.root.geometry('1000x600')
        self.root.resizable(False,False)

        self.frm1=Frame(self.root)
        self.frm1.place(x=0,y=0,width=1000,height=100)
        self.frm1.config(bg="black")

        self.lbl1=Label(self.frm1,text="UPDATE")
        self.lbl1.place(x=350,y=25,width=250,height=50)
        self.lbl1.config(font=("Times",22,"bold"),bg="black",fg="white")

        self.btnb=Button(self.frm1,text="BACK",command=self.bck)
        self.btnb.place(x=25,y=25,width=100,height=40)
        self.btnb.config(font=18)

        self.frmpic=Frame(self.root)
        self.frmpic.place(x=100,y=150,width=250,height=250)
        self.frmpic.config(bg="black")

        self.img = Image.open('image/default.png').resize((250, 250))
        self.imgTk = ImageTk.PhotoImage(self.img)
        self.imgLbl = Label(self.frmpic, image = self.imgTk,bg='black')
        self.imgLbl.place(x = 0, y = 0,height=250,width=250)

        self.piclbl=Label(self.root,text="UPLOAD PIC")
        self.piclbl.place(x=150,y=400,width=150,height=50)
        self.piclbl.config(font=("Gill Sans MT", 16))


        self.btn=Button(self.root,text="BROWSE")
        self.btn.place(x=100,y=450,width=100,height=50)
        self.btn.config(font=("Gill Sans MT", 16))

        self.btn2=Button(self.root,text="TAKE")
        self.btn2.place(x=250,y=450,width=100,height=50)
        self.btn2.config(font=("Gill Sans MT", 16))


        self.lb1=Label(self.root,text="FULL NAME :")
        self.lb1.place(x=550,y=150+70)
        self.lb1.config(fg="black",font=("Gill Sans MT", 16))

        self.box1=Entry(self.root)
        self.box1.place(x=700,y=150+70,width=200,height=30)
        self.box1.config(fg="black",font=("Gill Sans MT", 16))

        # self.box1.insert(0,'Lovepreet')

        self.lb2=Label(self.root,text="ROLLNO :")
        self.lb2.place(x=550,y=215+70)
        self.lb2.config(fg="black",font=("Gill Sans MT", 16))

        self.box2=Entry(self.root)
        self.box2.place(x=700,y=215+70,width=200,height=30)
        self.box2.config(fg="black",font=("Gill Sans MT", 16))

        # self.box2.insert(0,'3654')

        self.lb3=Label(self.root,text="CLASS :")
        self.lb3.place(x=550,y=280+70)
        self.lb3.config(fg="black",font=("Gill Sans MT", 16))

        self.box3=Entry(self.root)
        self.box3.place(x=700,y=280+70,width=200,height=30)
        self.box3.config(fg="black",font=("Gill Sans MT", 16))

        # self.box3.insert(0,'data science')

        self.lb4=Label(self.root,text="ADDRESS :")
        self.lb4.place(x=550,y=345+70)
        self.lb4.config(fg="black",font=("Gill Sans MT", 16))

        self.box4=Entry(self.root)
        self.box4.place(x=700,y=345+70,width=200,height=30)
        self.box4.config(fg="black",font=("Gill Sans MT", 16))

        # self.box4.insert(0,'shahkot')

        self.btn3=Button(self.root,text="SUBMIT",command=self.updt)
        self.btn3.place(x=650,y=400+70,width=100,height=50)
        self.btn3.config(fg="black",font=("Gill Sans MT", 16))
        
        self.var = StringVar()
        vals=db.getusr()
        print(vals)
        self.vals=vals
        self.data=[]
        for i in vals:
            self.data.append(i[1])
        self.values =self.data
        self.uid = ttk.Combobox(self.root, width = 27, textvariable = self.var, values=self.values) 
        self.uid.place(x=500,y=150)

        self.uid.current()
        # self.uid.bind("<<ComboboxSelected>>", callbackFunc(self,self.var))
        self.var.trace("w",self.callbackFunc)



        

        self.root.mainloop()
    def callbackFunc(self,*a):
        ca = self.var.get()
        for i in self.vals:
            if ca==i[1]:
                self.box1.delete(0,END)
                self.box2.delete(0,END)
                self.box3.delete(0,END)
                self.box4.delete(0,END)
                self.box1.insert(0,i[1])
                self.box2.insert(0,i[2])
                self.box3.insert(0,i[3])
                self.box4.insert(0,i[4])
                self.id=i[0]
    def updt(self):
        res=db.update((self.box1.get(),self.box2.get(),self.box3.get(),self.box4.get(),self.id))
        print(res)

    def bck(self):
        self.root.destroy()
        admin3.Frame1()
if __name__=='__main__':
    Frame1()