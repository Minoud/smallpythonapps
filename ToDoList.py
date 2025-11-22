from tkinter import *

class Fenetre(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("To-Do List 📝")
        self.geometry("500x500")
        self.resizable(False, False)
        self.tasks = []
        self.cree_interface()

    def ajouter_tache(self):
        t = self.entree.get().strip()
        if t:
            self.tasks.append({"texte": t, "faite": False})
            self.liste.insert(END, t)
            self.entree.delete(0, END)

    def supprimer_tache(self):
        sel = self.liste.curselection()
        if sel:
            i = sel[0]
            del self.tasks[i]
            self.liste.delete(i)

    def valider_tache(self):
        sel = self.liste.curselection()
        if sel:
            i = sel[0]
            t = self.tasks[i]
            t["faite"] = not t["faite"]
            self.liste.delete(i)
            texte = "✅ " + t["texte"] if t["faite"] else t["texte"]
            self.liste.insert(i, texte)

    def cree_interface(self):
        self.label = Label(self, text="To-Do List", font=("Arial", 16, "bold"))
        self.label.place(x=160, y=10)

        self.entree = Entry(self, width=33, font="Arial 12")
        self.entree.place(x=60, y=60)

        self.liste = Listbox(self, width=45, height=15, font="Arial 12")
        self.liste.place(x=60, y=100)

        self.add_btn = Button(self, text="Ajouter", font=("Arial 12"), bg="lightgreen", command=self.ajouter_tache)
        self.add_btn.place(x=60, y=430)

        self.del_btn = Button(self, text="Supprimer", font=("Arial 12"), bg="lightcoral", command=self.supprimer_tache)
        self.del_btn.place(x=200, y=430)

        self.val_btn = Button(self, text="Valider", font=("Arial 12"), bg="lightblue", command=self.valider_tache)
        self.val_btn.place(x=340, y=430)

tm = Fenetre()
tm.mainloop()
