from tkinter import *
from PIL import Image, ImageTk
import numpy as np
from histogram import hist_to_image
from adjust import rotate_image_bilinear
from brightness import adjust_brightness
from contrast import adjust_contrast_correctly
from zoom import zoom_image

class Aplikacija:

    def __init__(self, root, o_image):
        self.prozor = root
        self.prozor.title("Uvod u procesiranje slike - Projekat")
        self.prozor.geometry('1380x650')
        self.left_frame = Frame(root, width=500, height=600, bg='grey')
        self.left_frame.grid(row=0, column=0, padx=10, pady=5)
        self.originalImage = o_image
        self.originalImageArray = np.array(o_image)
        self.originalRHistogram = hist_to_image(self.originalImageArray)
        self.originalGHistogram = hist_to_image(self.originalImageArray)
        self.originalBHistogram = hist_to_image(self.originalImageArray)
        self.filteredImage = None
        self.filteredHistogram  = None
        self.filteredImageArray = np.array(o_image)

        tool_bar = Frame(self.left_frame, width=250, height=500)
        tool_bar.grid(row=0, column=0, padx=5, pady=5)

        Label(tool_bar, text="Filters", relief=RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=50)

        #Adjust - Jako sporo radi
        self.adjustSlide = Scale(tool_bar, from_=-25, to=25, tickinterval=50, orient=HORIZONTAL, label='Adjust')
        self.adjustSlide.grid(row=2, column=0, padx=5, pady=5)
        self.clicked_adjust = False
        self.adjustSlide.bind("<ButtonPress-1>", self.slider_adjust_pressed)
        self.adjustSlide.bind("<ButtonRelease-1>", self.slider_adjust_released)
        self.adjustSlide.bind("<Motion>", self.primeni_adjust)

        #Brightness
        self.brightSlide = Scale(tool_bar, from_=-50, to=50, tickinterval=100, orient= HORIZONTAL, label='Brighteness')
        self.brightSlide.grid(row=3, column=0, padx=5, pady=5)
        self.clicked_bright = False
        self.brightSlide.bind("<ButtonPress-1>", self.slider_bright_pressed)
        self.brightSlide.bind("<ButtonRelease-1>", self.slider_bright_released)
        self.brightSlide.bind("<Motion>", self.primeni_brightness)

        #Contrast
        self.contrastSlide = Scale(tool_bar, from_=0, to=100, tickinterval=50, orient=   HORIZONTAL, label='Contrast')
        self.contrastSlide.grid(row=4, column=0, padx=5, pady=5)
        self.clicked_contrast = False
        self.contrastSlide.bind("<ButtonPress-1>", self.slider_contrast_pressed)
        self.contrastSlide.bind("<ButtonRelease-1>", self.slider_contrast_released)
        self.contrastSlide.bind("<Motion>", self.primeni_contrast)

        #Warmth
        self.warmthSlide = Scale(tool_bar, from_=0, to=100, tickinterval=50, orient=   HORIZONTAL, label='Warmth')
        self.warmthSlide.grid(row=5, column=0, padx=5, pady=5)
        self.warmthSlide.bind("<ButtonRelease-1>", self.obradi_promenu_vrednosti)

        #Saturation
        self.saturationSlide = Scale(tool_bar, from_=0, to=100, tickinterval=50, orient=   HORIZONTAL, label='Saturation')
        self.saturationSlide.grid(row=6, column=0, padx=5, pady=5)
        self.saturationSlide.bind("<ButtonRelease-1>", self.obradi_promenu_vrednosti)

        #Fade
        self.fadeSlide = Scale(tool_bar, from_=-25, to=25, tickinterval=50, orient=   HORIZONTAL, label='Fade')
        self.fadeSlide.grid(row=7, column=0, padx=5, pady=5)
        self.fadeSlide.bind("<ButtonRelease-1>", self.obradi_promenu_vrednosti)
        
        #Hightlights
        self.hightSlide = Scale(tool_bar, from_=0, to=100, tickinterval=50, orient=   HORIZONTAL, label='Hightlights')
        self.hightSlide.grid(row=2, column=1, padx=5, pady=5)
        self.hightSlide.bind("<ButtonRelease-1>", self.obradi_promenu_vrednosti)

        #Shadows
        self.shadowSlide = Scale(tool_bar, from_=0, to=100, tickinterval=50, orient=   HORIZONTAL, label='Shadows')
        self.shadowSlide.grid(row=3, column=1, padx=5, pady=5)
        self.shadowSlide.bind("<ButtonRelease-1>", self.obradi_promenu_vrednosti)

        #Zoom
        self.zoonSlide = Scale(tool_bar, from_=1, to=10, tickinterval=10, orient=HORIZONTAL, label='Zoom')
        self.zoonSlide.grid(row=4, column=1, padx=2, pady=2)
        self.clicked_zoom = False
        self.zoonSlide.bind("<ButtonPress-1>", self.slider_zoom_pressed)
        self.zoonSlide.bind("<ButtonRelease-1>", self.slider_zoom_released)
        self.zoonSlide.bind("<Motion>", self.primeni_zoom)

        #Vignette
        self.vignetteB = Button(tool_bar, text="Apply Vignette", width=6, height=1, borderwidth=5)
        self.vignetteB.grid(row=5, column=1, padx=2, pady=(0, 2), ipadx=20)
        self.vignetteB.bind("<Button-1>", self.obradi_promenu_vrednosti)
        
        #Tile Shift - Linear
        self.tileShihtLB = Button(tool_bar, text="Apply Linear TS",  width=6, height=1, borderwidth=5)
        self.tileShihtLB.grid(row=6, column=1, padx=2, pady=2, ipadx=20)
        self.tileShihtLB.bind("<Button-1>", self.obradi_promenu_vrednosti)

        #Tile Shift - Radial
        self.tileShihtRB = Button(tool_bar, text="Apply Radial TS",  width=6, height=1, borderwidth=5)
        self.tileShihtRB.grid(row=7, column=1, padx=2, pady=2, ipadx=20)
        self.tileShihtRB.bind("<Button-1>", self.obradi_promenu_vrednosti)

        #Sharpen
        self.sharpenB = Button(tool_bar, text="Apply Sharpen", width=6, height=1, borderwidth=5)
        self.sharpenB.grid(row=8, column=1, padx=2, pady=(2,0), ipadx=20)
        self.sharpenB.bind("<Button-1>", self.obradi_promenu_vrednosti)
        
        self.right_frame = Frame(root, width=650, height=400, bg='black')
        self.right_frame.grid(row=0, column=2, padx=10, pady=5)
        self.image = ImageTk.PhotoImage(o_image)
        self.histRImage = ImageTk.PhotoImage(self.originalRHistogram)
        self.histGImage = ImageTk.PhotoImage(self.originalGHistogram)
        self.histBImage = ImageTk.PhotoImage(self.originalBHistogram)
        #Right frame
        Label(self.right_frame, image=self.image).grid(row=0,column=0, padx=5, pady=5)
        Label(self.right_frame, image=self.histRImage).grid(row=0,column=2, padx=5, pady=5)
        Label(self.right_frame, image=self.histGImage).grid(row=0,column=4, padx=5, pady=5)
        Label(self.right_frame, image=self.histBImage).grid(row=0,column=6, padx=5, pady=5)
        """
        Label(self.right_frame, image=self.filteredImage).grid(row=2,column=0, padx=5, pady=5)
        Label(self.right_frame, image=self.filteredHistogram).grid(row=2,column=2, padx=5, pady=5)"""

    def obradi_promenu_vrednosti(self, event):
        pass

    #Adjust
    def slider_adjust_pressed(self, event):
        self.clicked_adjust = True       
            
    def slider_adjust_released(self, event):
        self.clicked_adjust = False

    def primeni_adjust(self, event):
        if self.clicked_adjust:
            tmp = rotate_image_bilinear(self.originalImageArray, self.adjustSlide.get())
            self.image = ImageTk.PhotoImage(image=Image.fromarray(tmp))
            self.filteredImageArray = tmp
            print("Adjust done.")
            Label(self.right_frame, image=self.image).grid(row=0,column=0, padx=5, pady=5)

    #Bright
    def slider_bright_pressed(self, event):
        self.clicked_bright = True       
            
    def slider_bright_released(self, event):
        self.clicked_bright = False   

    def primeni_brightness(self, event):
        if self.clicked_bright:
            tmp = adjust_brightness(self.filteredImageArray, self.brightSlide.get())
            self.image = ImageTk.PhotoImage(image=Image.fromarray(tmp))
            self.imageArray = tmp
            print("Brightness done.")
            Label(self.right_frame, image=self.image).grid(row=0,column=0, padx=5, pady=5)

    #Contrast
    def slider_contrast_pressed(self, event):
        self.clicked_contrast = True       
            
    def slider_contrast_released(self, event):
        self.clicked_contrast = False   
    
    def primeni_contrast(self, event):
        if self.clicked_contrast:
            tmp = adjust_contrast_correctly(self.filteredImageArray, self.contrastSlide.get())
            self.image = ImageTk.PhotoImage(image=Image.fromarray(tmp))
            self.imageArray = tmp
            print("Contrast done.")
            Label(self.right_frame, image=self.image).grid(row=0,column=0, padx=5, pady=5)

    #Zoom
    def slider_zoom_pressed(self, event):
        self.clicked_zoom = True       
            
    def slider_zoom_released(self, event):
        self.clicked_zoom = False
    
    def primeni_zoom(self, event):
        if self.clicked_zoom:
            tmp = zoom_image(self.originalImage, self.zoonSlide.get())
            self.image = ImageTk.PhotoImage(image=Image.fromarray(tmp))
            self.imageArray = tmp
            print("Zoom done.")
            Label(self.right_frame, image=self.image).grid(row=0,column=0, padx=5, pady=5)
        


