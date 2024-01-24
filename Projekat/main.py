import tkinter as tk
from load_images import load_image
from aplikacija import Aplikacija


def main():
    root = tk.Tk()
    app= Aplikacija(root, load_image('images/lena.tif'))
    root.mainloop()

if __name__ == '__main__':
    main()