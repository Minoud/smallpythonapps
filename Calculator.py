from tkinter import *

class Fenetre(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Calculator")
        self.geometry("420x520")
        self.maxsize(420,520)
        self.cree_interface()

    def ajoute(self,x):
        self.entree.insert(len(self.entree.get()),x)

    def retire(self):
        self.entree.delete(len(self.entree.get())-1,len(self.entree.get()))

    def calc(self):
      exp = self.entree.get()
      num1 = ""
      num2 = ""
      op = ""
      for char in exp:
        if char.isdigit():
          num1+=char
        else:
           op=char
           num2=num1
           num1=""
      if op=="+":
         res = int(num2)+int(num1)
      if op=="-":
         res = int(num2)-int(num1)
      if op=="*":
         res = int(num2)*int(num1)
      if op=="/":
         res = int(num2)/int(num1)
      self.entree.delete(0,len(self.entree.get()))
      self.entree.insert(0,res)

    def cree_interface(self):
        self.entree = Entry(self, width=41, font="Arial 12 bold")
        self.entree.place(x=22,y=20)
        self.entree.bind("<Return>", None)

        self.un = Button(self, text="1", width=9, height=4, bg="lightgrey", font=("Arial 12"), command=lambda : self.ajoute(1))
        self.un.place(x=20, y=60)

        self.deux = Button(self, text="2", width=9, height=4, bg="lightgrey", font=("Arial 12"), command=lambda : self.ajoute(2))
        self.deux.place(x=115, y=60)

        self.trois = Button(self, text="3", width=9, height=4, bg="lightgrey", font=("Arial 12"), command=lambda : self.ajoute(3))
        self.trois.place(x=210, y=60)

        self.quatre = Button(self, text="4", width=9, height=4, bg="lightgrey", font=("Arial 12"), command=lambda : self.ajoute(4))
        self.quatre.place(x=20, y=150)

        self.cinq = Button(self, text="5", width=9, height=4, bg="lightgrey", font=("Arial 12"), command=lambda : self.ajoute(5))
        self.cinq.place(x=115, y=150)

        self.six = Button(self, text="6", width=9, height=4, bg="lightgrey", font=("Arial 12"), command=lambda : self.ajoute(6))
        self.six.place(x=210, y=150)

        self.sept = Button(self, text="7", width=9, height=4, bg="lightgrey", font=("Arial 12"), command=lambda : self.ajoute(7))
        self.sept.place(x=20, y=240)

        self.huit = Button(self, text="8", width=9, height=4, bg="lightgrey", font=("Arial 12"), command=lambda : self.ajoute(8))
        self.huit.place(x=115, y=240)

        self.neuf = Button(self, text="9", width=9, height=4, bg="lightgrey", font=("Arial 12"), command=lambda : self.ajoute(9))
        self.neuf.place(x=210, y=240)

        self.zero = Button(self, text="0", width=30, height=4, bg="lightgrey", font=("Arial 12"), command=lambda : self.ajoute(0))
        self.zero.place(x=20, y=330)

        self.plus = Button(self, text="+", width=9, height=4, bg="lightgrey", font=("Arial 12"), command=lambda : self.ajoute("+"))
        self.plus.place(x=305, y=60)

        self.moins = Button(self, text="-", width=9, height=4, bg="lightgrey", font=("Arial 12"), command=lambda : self.ajoute("-"))
        self.moins.place(x=305, y=150)

        self.fois = Button(self, text="*", width=9, height=4, bg="lightgrey", font=("Arial 12"), command=lambda : self.ajoute("*"))
        self.fois.place(x=305, y=240)

        self.div = Button(self, text="/", width=9, height=4, bg="lightgrey", font=("Arial 12"), command=lambda : self.ajoute("/"))
        self.div.place(x=305, y=330)

        self.calculer = Button(self, text="Calculer", width=19, height=4, bg="lightgrey", font=("Arial 12"), command=self.calc)
        self.calculer.place(x=20, y=420)

        self.retour = Button(self, text="Retour", width=19, height=4, bg="lightgrey", font=("Arial 12"), command=self.retire)
        self.retour.place(x=215, y=420)


tm=Fenetre()
tm.mainloop()
