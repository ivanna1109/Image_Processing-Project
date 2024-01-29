from tkinter import *
from load_images import load_image_test, load_image_cv
from aplikacija import Aplikacija


def main():
    root = Tk()
    #image = load_image_cv('images/ivi.jpg') #slika cv
    #image = load_image_test('images/building.jpg') #building
    image = load_image_test('images/monalisa.jpg') #monaliza
    app= Aplikacija(root, image)
    root.mainloop()

if __name__ == '__main__':
    main()