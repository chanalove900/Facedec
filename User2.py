from tkinter import *
from tkinter import messagebox,filedialog
import User1 ,db
from PIL import Image, ImageTk
import datetime

class Frame1:
    data=''
    face=''
    def __init__(self):
        print(self.data,"user2data")
        self.root=Tk()
        self.root.geometry('1000x600')
        self.root.resizable(False,False)

        if self.data:
            self.frm1=Frame(self.root)
            self.frm1.place(x=0,y=0,width=1000,height=100)
            self.frm1.config(bg="green")

            self.frm2=Frame(self.root)
            self.frm2.place(x=0,y=500,width=1000,height=100)
            self.frm2.config(bg="green")

            self.frmpic=Frame(self.root)
            self.frmpic.place(x=100,y=150,width=300,height=300)
            self.frmpic.config(bg="black")

            # self.img = Image.open(self.face).resize((250, 250))
            self.face=self.face.resize((250, 250))
            self.imgTk = ImageTk.PhotoImage(self.face)
            self.imgLbl = Label(self.frmpic, image = self.imgTk,bg='black')
            self.imgLbl.place(x = 25, y = 25,height=250,width=250)

            self.lb1=Label(self.root,text=self.data[1])
            self.lb1.place(x=550,y=150)
            self.lb1.config(fg="black",font=("Gill Sans MT", 28,"bold"))

            self.lb2=Label(self.root,text=self.data[2])
            self.lb2.place(x=550,y=250)
            self.lb2.config(fg="black",font=("Gill Sans MT", 16))

            self.lb3=Label(self.root,text=self.data[3])
            self.lb3.place(x=550,y=300)
            self.lb3.config(fg="black",font=("Gill Sans MT", 16))

            self.lb4=Label(self.root,text=self.data[4])
            self.lb4.place(x=550,y=350)
            self.lb4.config(fg="black",font=("Gill Sans MT", 16))
        else:
            self.frm1=Frame(self.root)
            self.frm1.place(x=0,y=0,width=1000,height=100)
            self.frm1.config(bg="red")

            self.frm2=Frame(self.root)
            self.frm2.place(x=0,y=500,width=1000,height=100)
            self.frm2.config(bg="red")

            self.frmpic=Frame(self.root)
            self.frmpic.place(x=100,y=150,width=300,height=300)
            self.frmpic.config(bg="black")
            
            self.lb1=Label(self.root,text="Not Found")
            self.lb1.place(x=550,y=190)
            self.lb1.config(fg="black",font=("Gill Sans MT", 28,"bold"))

        # self.btn=Button(self.root,text="OK")
        # self.btn.place(x=650,y=400,width=80,height=40)
        # self.btn.config(font=("Gill Sans MT", 18),bg="#4f8fe8")

        # self.root.after(3000,self.back)
        self.run()
        self.root.mainloop()
    def back(self):
        self.root.destroy()
        User1.Frame1()

    def run(self):
        datag=self.data[0]
        self.at=db.getatt((datag,))
        dt=datetime.date.today()
        # print("at data-",self.at)
        print(self.at[3])

        if self.at[3] == dt:
            self.lb1=Label(self.root,text="Attendace Already registered")
            self.lb1.place(x=550,y=190)
            self.lb1.config(fg="black",font=("Gill Sans MT", 28,"bold"))
        else:
            attn=self.at[2]+1
            datau=(attn,dt, self.data[0])
            res=db.updattn(datau)
            print(res)
            if res:
                print("ATTENDANCE UPDATE!")
    

    

    
if __name__=='__main__':
    Frame1()