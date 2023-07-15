from tkinter import ttk
import tkinter as tk
from tkinter import *
import  db

class frame4:
    def __init__(self):
        self.root= tk.Tk()
        self.root.geometry("1000x600")
        self.root.resizable(False,False)

        self.frm=Frame(self.root)
        self.frm.place(x=0,y=0,width=1000,height=100)
        self.frm.config(bg="black")

        self.lbl=Label(self.frm,text="ATTENDACE!")
        self.lbl.place(x=320,y=25,width=350,height=50)
        self.lbl.config(bg="black",fg="white",font=("Times",22,"bold"))
        
        # self.btn=Button(self.frm,text="BACK",command=self.bck)
        # self.btn.place(x=25,y=25,width=100,height=40)
        # self.btn.config(font=18)

        self.treev = ttk.Treeview(self.root, selectmode ='browse')

        self.treev.place(x=100,y=100,width=800,height=400)

        verscrlbar = ttk.Scrollbar(self.root,orient ="vertical",command = self.treev.yview)

        verscrlbar.pack(side ='right', fill ='x')

        self.treev.configure(xscrollcommand = verscrlbar.set)

        self.treev["columns"] = ("1", "2", "3","4")

        self.treev['show'] = 'headings'

        self.treev.column("1", width = 200, anchor ='c')
        self.treev.column("2", width = 200, anchor ='c')
        self.treev.column("3", width = 200, anchor ='c')
        self.treev.column("4", width = 200, anchor ='c')
    
        self.treev.heading("1", text ="sid")
        self.treev.heading("2", text ="name")
        self.treev.heading("3", text ="atten")
        self.treev.heading("4", text ="date")

        data=db.attn(self)
        for i in data:
             self.treev.insert("", 'end', text =i[0],values =(i[0],i[1],i[2],i[3]))
        
        self.root.mainloop()
    

if __name__=='__main__':
    frame4()
