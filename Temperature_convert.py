from tkinter import *

def isfloat(x):
    l = ['0','1','2','3','4','5','6','7','8','9','+','-','.']
    if x.count('+')>1 or x.count('-')>1 or x.count('.')>1:
        return False
    if x=="+" or x=="-" or x=="." or x=="":
        return False
    for char in x:
        if char not in l:
            return False
        if char in ['+','-'] and x.find(char)>0:
            return False
    return True

class Fenetre(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Temperature convertor")
        self.geometry("400x400")
        self.maxsize(400,300)
        self.cree_floaterface()

    def modifie(self,event):
        wid = event.widget
        text = wid.get()
        if isfloat(text):
            if wid == self.c:
              val = self.txtc.get()
              self.txtk.set(str(float(val)-273.15))
              self.txtf.set(str(float(val)*(9/5)+32))
        
            elif wid == self.k:
                val = self.txtk.get()
                self.txtc.set(str(float(val)+273.15))
                self.txtf.set(str((float(val)+273.15)*(9/5)+32))
            
            elif wid == self.f:
                val = self.txtf.get()
                self.txtc.set(str((float(val)-32)*(5/9)))
                self.txtk.set(str((float(val)-32)*(5/9)-273.15))

    def cree_floaterface(self):
        self.txtc = StringVar()
        self.txtk = StringVar()
        self.txtf = StringVar()

        self.label = Label(self, text="Temperature convertor", font=("Arial 14 bold underline"))
        self.label.place(x=100,y=10)

        self.label_c = Label(self, text="°C", font=("Arial 14"))
        self.label_c.place(x=30,y=77)

        self.c = Entry(self, width=33, textvariable=self.txtc ,font="Arial 12")
        self.c.place(x=80,y=80)

        self.label_f = Label(self, text="°F", font=("Arial 14"))
        self.label_f.place(x=30,y=132)

        self.f = Entry(self, width=33,  textvariable=self.txtf ,font="Arial 12")
        self.f.place(x=80,y=135)

        self.label_k = Label(self, text="°K", font=("Arial 14"))
        self.label_k.place(x=30,y=187)

        self.k = Entry(self, width=33,  textvariable=self.txtk ,font="Arial 12")
        self.k.place(x=80,y=190)

        self.exit = Button(self, text="Exit", width=10, font=("Arial 14"), command=self.destroy)
        self.exit.place(x=150,y=230)

        self.bind("<KeyPress>",self.modifie)

tm=Fenetre()
tm.mainloop()
