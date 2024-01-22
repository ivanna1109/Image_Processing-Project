import tkinter as tk
from PIL import Image, ImageTk

class Aplikacija:
    def __init__(self, prozor, originalna_slika):
        self.prozor = prozor
        self.prozor.title("Uvod u procesiranje slike - Projekat")
        self.prozor.geometry('600x700')
        self.tk_slika = ImageTk.PhotoImage(originalna_slika)

        self.slika_labela = tk.Label(prozor, image=self.tk_slika)
        self.slika_labela.pack()

        self.dugme = tk.Button(prozor, text="Apply filter", command=self.primeni_filter)
        self.dugme.pack()

    def primeni_filter(self):
        nova_slika = self.obradi_sliku()
        nova_tk_slika = ImageTk.PhotoImage(nova_slika)
        self.slika_labela.configure(image=nova_tk_slika)
        self.slika_labela.image = nova_tk_slika
        print("vlaDko")

    def obradi_sliku(self):
        print("Kliknuli smo na apply filter")
        pass


