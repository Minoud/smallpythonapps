from tkinter import *
import random
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Fenetre(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Simulateur de Lancers de Deux Dés")
        self.geometry("700x550")
        self.resizable(False, False)
        
        self.lancers = []
        
        self.cree_interface()

    def lancer_des(self):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        total = d1 + d2
        self.lancers.append(total)
        
        self.zone_resultats.config(state="normal")
        self.zone_resultats.insert(END, f"{d1} + {d2} = {total}\n")
        self.zone_resultats.config(state="disabled")
        
        self.mettre_a_jour_graphique()

    def reset(self):
        self.lancers.clear()
        self.zone_resultats.config(state="normal")
        self.zone_resultats.delete("1.0", END)
        self.zone_resultats.config(state="disabled")
        self.mettre_a_jour_graphique()

    def cree_interface(self):
        Label(self, text="Simulateur de Lancers de Deux Dés", 
              font=("Arial", 16, "bold")).pack(pady=10)

        Label(self, text="Résultats :", font=("Arial", 12, "bold")).pack()
        self.zone_resultats = Text(self, height=6, width=60, font=("Arial", 12))
        self.zone_resultats.pack()
        self.zone_resultats.config(state="disabled")

        cadre_boutons = Frame(self)
        cadre_boutons.pack(pady=10)
        Button(cadre_boutons, text="Lancer les dés", font=("Arial", 12), bg="lightgreen",
               command=self.lancer_des).pack(side=LEFT, padx=10)
        Button(cadre_boutons, text="Réinitialiser", font=("Arial", 12), bg="lightcoral",
               command=self.reset).pack(side=LEFT, padx=10)

        self.figure = Figure(figsize=(6.5, 3.5), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title("Répartition des sommes (2 à 12)")
        self.ax.set_xlabel("Somme des deux dés")
        self.ax.set_ylabel("Nombre d’occurrences")
        self.ax.set_xticks(range(2, 13))
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().pack(pady=10)

        self.mettre_a_jour_graphique()

    def mettre_a_jour_graphique(self):
        self.ax.clear()
        self.ax.set_title("Répartition des sommes (2 à 12)")
        self.ax.set_xlabel("Somme des deux dés")
        self.ax.set_ylabel("Nombre d’occurrences")
        self.ax.set_xticks(range(2, 13))

        if self.lancers:
            counts = [self.lancers.count(i) for i in range(2, 13)]
            self.ax.bar(range(2, 13), counts)
        else:
            self.ax.bar(range(2, 13), [0]*11)

        self.canvas.draw()

app = Fenetre()
app.mainloop()
