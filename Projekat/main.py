from tkinter import *
from load_images import load_image
from aplikacija import Aplikacija


def main():
    root = Tk()
    app= Aplikacija(root, load_image('images/building.jpg'))
    root.mainloop()

if __name__ == '__main__':
    main()