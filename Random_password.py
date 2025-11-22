from tkinter import *
import random
import string

class Fenetre(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Password")
        self.geometry("400x400")
        self.maxsize(400,300)
        self.cree_interface()

    def generate(self):
      l = int(self.lg.get())
      liste = " "
      if self.varc.get() :
          liste+=string.punctuation
      if self.varl.get() :
          liste+=string.ascii_letters
      if self.varn.get() :
          liste+=string.digits
      password = ""
      for k in range(l):
        password+=random.choice(liste)
      self.txt.set(password)

    def cree_interface(self):
        self.label = Label(self, text="Enter your settings", font=("Arial 14 bold underline"))
        self.label.place(x=115,y=10)

        self.varl = IntVar()
        self.letters = Checkbutton(self, text="Letters", font="Arial 12", variable=self.varl, onvalue=1, offvalue=0)
        self.letters.place(x=160, y=75)

        self.varn = IntVar()
        self.numbers = Checkbutton(self, text="Numbers", font="Arial 12", variable=self.varn, onvalue=1, offvalue=0)
        self.numbers.place(x=160, y=100)

        self.varc = IntVar()
        self.chars = Checkbutton(self, text="Special characters", font="Arial 12", variable=self.varc, onvalue=1, offvalue=0)
        self.chars.place(x=160, y=125)

        self.lg = StringVar()
        self.txtnb = Label(self, text="Nb of characters :", font=("Arial 11"))
        self.txtnb.place(x=70, y=160)
        self.nombre = Entry(self, textvariable=self.lg, font="Arial 12", width=5)
        self.nombre.place(x=200,y=160)

        self.txt = StringVar()
        self.zone = Entry(self, width=33,  font="Arial 12", textvariable=self.txt)
        self.zone.place(x=50,y=200)

        self.gen = Button(self, text="Generate", bg="lightgrey", font=("Arial 12"), command=self.generate)
        self.gen.place(x=165, y=240)

tm=Fenetre()
tm.mainloop()
