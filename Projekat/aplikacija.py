import tkinter as tk
from PIL import Image, ImageTk

class Aplikacija:
    def __init__(self, root, o_image):
        self.prozor = root
        self.prozor.title("Uvod u procesiranje slike - Projekat")
        self.prozor.geometry('950x700')
        left_frame = tk.Frame(root, width=500, height=600, bg='grey')
        left_frame.grid(row=0, column=0, padx=10, pady=5)

        tool_bar = tk.Frame(left_frame, width=250, height=500)
        tool_bar.grid(row=0, column=0, padx=5, pady=5)

        tk.Label(tool_bar, text="Filters", relief=tk.RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=50)

# Example labels that could be displayed under the "Tool" menu
        tk.Scale(tool_bar, from_=-25, to=25, tickinterval=50, orient=tk.HORIZONTAL, label='Adjust').grid(row=2, column=0, padx=5, pady=5)
        tk.Button(tool_bar, text="Apply filter").grid(row=3, column=0, padx=5, pady=5, ipadx=20)
        tk.Scale(tool_bar, from_=0, to=100, tickinterval=50, orient=tk.HORIZONTAL, label='Brighteness').grid(row=4, column=0, padx=5, pady=5)
        tk.Button(tool_bar, text="Apply filter").grid(row=5, column=0, padx=5, pady=5, ipadx=40)
        tk.Scale(tool_bar, from_=0, to=100, tickinterval=50, orient=tk.HORIZONTAL, label='Contrast').grid(row=6, column=0, padx=5, pady=5)
        tk.Button(tool_bar, text="Apply filter").grid(row=7, column=0, padx=5, pady=5, ipadx=40)
        tk.Scale(tool_bar, from_=0, to=100, tickinterval=50, orient=tk.HORIZONTAL, label='Warmth').grid(row=8, column=0, padx=5, pady=5)
        tk.Button(tool_bar, text="Apply filter").grid(row=9, column=0, padx=5, pady=5, ipadx=40)
        tk.Scale(tool_bar, from_=0, to=100, tickinterval=50, orient=tk.HORIZONTAL, label='Saturation').grid(row=10, column=0, padx=5, pady=5)
        tk.Button(tool_bar, text="Filter 5").grid(row=11, column=0, padx=5, pady=5, ipadx=40)

        tk.Scale(tool_bar, from_=-25, to=25, tickinterval=50, orient=tk.HORIZONTAL, label='Adjust').grid(row=2, column=1, padx=5, pady=5)
        tk.Button(tool_bar, text="Apply filter").grid(row=3, column=1, padx=5, pady=5, ipadx=20)
        tk.Scale(tool_bar, from_=0, to=100, tickinterval=50, orient=tk.HORIZONTAL, label='Brighteness').grid(row=4, column=1, padx=5, pady=5)
        tk.Button(tool_bar, text="Apply filter").grid(row=5, column=1, padx=5, pady=5, ipadx=40)
        tk.Scale(tool_bar, from_=0, to=100, tickinterval=50, orient=tk.HORIZONTAL, label='Contrast').grid(row=6, column=1, padx=5, pady=5)
        tk.Button(tool_bar, text="Apply filter").grid(row=7, column=1, padx=5, pady=5, ipadx=40)
        tk.Scale(tool_bar, from_=0, to=100, tickinterval=50, orient=tk.HORIZONTAL, label='Warmth').grid(row=8, column=1, padx=5, pady=5)
        tk.Button(tool_bar, text="Apply filter").grid(row=9, column=1, padx=5, pady=5, ipadx=40)
        tk.Scale(tool_bar, from_=0, to=100, tickinterval=50, orient=tk.HORIZONTAL, label='Saturation').grid(row=10, column=1, padx=5, pady=5)
        tk.Button(tool_bar, text="Filter 5").grid(row=11, column=1, padx=5, pady=5, ipadx=40)
        

        
        right_frame = tk.Frame(root, width=650, height=400, bg='black')
        right_frame.grid(row=0, column=2, padx=10, pady=5)
        self.image = ImageTk.PhotoImage(o_image)
        #Right frame
        tk.Label(right_frame, image=self.image).grid(row=0,column=0, padx=5, pady=5)
        tk.Label(right_frame, image=self.image).grid(row=0,column=2, padx=5, pady=5)
        tk.Label(right_frame, image=self.image).grid(row=2,column=0, padx=5, pady=5)
        tk.Label(right_frame, image=self.image).grid(row=2,column=2, padx=5, pady=5)

    def primeni_filter(self):
        nova_slika = self.obradi_sliku()
        nova_tk_slika = ImageTk.PhotoImage(nova_slika)
        self.slika_labela.configure(image=nova_tk_slika)
        self.slika_labela.image = nova_tk_slika
        print("vlaDkoNJina")

    def obradi_sliku(self):
        print("Kliknuli smo na apply filter")
        pass


