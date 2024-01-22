import tkinter as tk
from PIL import Image
from aplikacija import Aplikacija


def main():
    root = tk.Tk()
    originalna_slika = Image.open('images/lena.tif')  # Postavite putanju do vaše slike
    app= Aplikacija(root, originalna_slika)
    root.mainloop()

if __name__ == '__main__':
    main()