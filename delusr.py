from tkinter import ttk
import tkinter as tk
from tkinter import *
import  db
import admin3,sample2

class frame4:
    def __init__(self):
        self.root= tk.Tk()
        self.root.geometry("1000x600")
        self.root.resizable(False,False)

        self.frm=Frame(self.root)
        self.frm.place(x=0,y=0,width=1000,height=100)
        self.frm.config(bg="black")

        self.lbl=Label(self.frm,text="DELETE STUDENTS")
        self.lbl.place(x=320,y=25,width=350,height=50)
        self.lbl.config(bg="black",fg="white",font=("Times",22,"bold"))
        
        self.btn=Button(self.frm,text="BACK",command=self.bck)
        self.btn.place(x=25,y=25,width=100,height=40)
        self.btn.config(font=18)


        self.treev = ttk.Treeview(self.root, selectmode ='browse')

        self.treev.place(x=100,y=100,width=800,height=400)

        verscrlbar = ttk.Scrollbar(self.root,orient ="vertical",command = self.treev.yview)

        verscrlbar.pack(side ='right', fill ='x')

        self.treev.configure(xscrollcommand = verscrlbar.set)

        self.treev["columns"] = ("1", "2", "3","4","5")

        self.treev['show'] = 'headings'

        self.treev.column("1", width = 90, anchor ='c')
        self.treev.column("2", width = 90, anchor ='c')
        self.treev.column("3", width = 90, anchor ='c')
        self.treev.column("4", width = 90, anchor ='c')
        self.treev.column("5", width = 90, anchor ='c')


        self.treev.heading("1", text ="sid")
        self.treev.heading("2", text ="name")
        self.treev.heading("3", text ="rollno")
        self.treev.heading("4", text ="class")
        self.treev.heading("5", text ="address")

        self.del_btn=Button(self.root,text="DELETE",command=self.delete)
        self.del_btn.place(x=475,y=520,width=100,height=40)
        self.del_btn.config(bg="red")

        

        data=db.existing(self)
        for i in data:
             self.treev.insert("", 'end', text =i[0],values =(i[0],i[1],i[2],i[3],i[4]))
        
        self.root.mainloop()
    def bck(self):
        self.root.destroy()
        admin3.Frame1()

    def delete(self):
        self.sel= self.treev.selection()[0]
        self.d=self.treev.item(self.sel)
        data=self.d["values"][0]

        fcid=db.fcusr(data)
        # print(self.d)
        print((data,))
        res=db.delete((data,))
        # print(res)
        self.treev.delete(self.sel)
        sample2.dele(fcid[2])
        


if __name__=='__main__':
    frame4()
