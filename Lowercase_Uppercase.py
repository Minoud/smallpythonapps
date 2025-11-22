from tkinter import *

class Fenetre(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Lower+Upper")
        self.geometry("400x400")
        self.maxsize(400,300)
        self.cree_interface()

    def uppercase(self):
        x = self.entree.get()
        self.zone.delete(0,len(self.zone.get()))
        self.zone.insert(0,x.upper())

    def lowercase(self):
        x = self.entree.get()
        self.zone.delete(0,len(self.zone.get()))
        self.zone.insert(0,x.lower())

    def cree_interface(self):
        self.label = Label(self, text="Enter your text", font=("Arial 14 bold underline"))
        self.label.place(x=125,y=10)

        self.entree = Entry(self, width=33, font="Arial 12")
        self.entree.place(x=50,y=80)
        self.entree.bind("<Return>", None)

        self.zone = Entry(self, width=33,  font="Arial 12")
        self.zone.place(x=50,y=110)

        self.uc = Button(self, text="Uppercase", bg="lightgrey", font=("Arial 12"), command=self.uppercase)
        self.uc.place(x=100, y=240)

        self.lc = Button(self, text="Lowercase", bg="lightgrey", font=("Arial 12"), command=self.lowercase)
        self.lc.place(x=220, y=240)

tm=Fenetre()
tm.mainloop()
