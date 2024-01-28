from tkinter import *
from PIL import Image, ImageTk
import numpy as np
from histogram import hist_to_image
from adjust import rotate_image_bilinear
from brightness import adjust_brightness
from contrast import adjust_contrast_correctly
from warmth import warmth_filter
from saturation import saturation
from fade import fade_filter
from highlights import highlights_filter
from shadows import shadows_filter
from vignette import vignette_filter
from zoom import zoom_image
from sharpen import sharpen_image
from tiltShift import radial_tilt_shift, linear_tilt_shift

class Aplikacija:

    def __init__(self, root, o_image):
        self.prozor = root
        self.prozor.title("Uvod u procesiranje slike - Projekat")
        self.prozor.geometry('1450x650') #width x height
        self.left_frame = Frame(root, width=500, height=600, bg='grey')
        self.left_frame.grid(row=0, column=0, padx=10, pady=5)
        self.originalImage = o_image
        self.originalImageArray = np.array(o_image)
        print(self.originalImageArray.shape)
        self.histogramRoriginal, self.histogramGoriginal, self.histogramBoriginal = hist_to_image(self.originalImageArray)
        self.filteredImage = o_image
        self.filteredImageArray = np.array(o_image)

        tool_bar = Frame(self.left_frame, width=250, height=500)
        tool_bar.grid(row=0, column=0, padx=5, pady=5)

        Label(tool_bar, text="Filters", relief=RAISED, width=6, height=1, borderwidth=2).grid(row=0, column=0, padx=20, pady=3, ipadx=50)
        self.resetButton = Button(tool_bar, text="Reset", width=6, height=1, borderwidth=2)
        self.resetButton.grid(row = 0, column = 1, padx=20, pady=3, ipadx=50)
        self.resetButton.bind('<ButtonPress-1>', self.reset_defaults)

        #Adjust - Jako sporo radi
        self.adjustSlide = Scale(tool_bar, from_=-25, to=25, tickinterval=25, orient=HORIZONTAL, label='Adjust')
        self.adjustSlide.grid(row=2, column=0, padx=5, pady=5)
        self.clicked_adjust = False
        self.adjustSlide.bind("<ButtonRelease-1>", self.primeni_adjust)

        #Brightness
        self.brightSlide = Scale(tool_bar, from_=-50, to=50, tickinterval=50, orient= HORIZONTAL, label='Brighteness')
        self.brightSlide.grid(row=3, column=0, padx=5, pady=5)
        self.clicked_bright = False
        self.brightSlide.bind("<ButtonPress-1>", self.slider_bright_pressed)
        self.brightSlide.bind("<ButtonRelease-1>", self.slider_bright_released)
        self.brightSlide.bind("<Motion>", self.primeni_brightness)

        #Contrast
        self.contrastSlide = Scale(tool_bar, from_=0, to=100, tickinterval=50, orient =HORIZONTAL, label='Contrast')
        self.contrastSlide.grid(row=4, column=0, padx=5, pady=5)
        self.clicked_contrast = False
        self.contrastSlide.bind("<ButtonPress-1>", self.slider_contrast_pressed)
        self.contrastSlide.bind("<ButtonRelease-1>", self.slider_contrast_released)
        self.contrastSlide.bind("<Motion>", self.primeni_contrast)

        #Saturation
        self.saturationSlide = Scale(tool_bar, from_=-1, to=1,  resolution=0.1, tickinterval=2, orient=   HORIZONTAL, label='Saturation')
        self.saturationSlide.grid(row=5, column=0, padx=5, pady=5)
        self.clicked_saturation = False
        self.saturationSlide.bind("<ButtonPress-1>", self.slider_saturation_pressed)
        self.saturationSlide.bind("<ButtonRelease-1>", self.slider_saturation_released)
        self.saturationSlide.bind("<Motion>", self.primeni_saturation)

        #Warmth
        self.warmthSlideR = Scale(tool_bar, from_=0, to=255, tickinterval=128, orient=HORIZONTAL, label='Warmth Red')
        self.warmthSlideR.grid(row=6, column=0, padx=5, pady=5)
        self.warmthSlideB = Scale(tool_bar, from_=0, to=255, tickinterval=255, orient=   HORIZONTAL, label='Warmth Blue')
        self.warmthSlideB.grid(row=7, column=0, padx=5, pady=5)
        self.warmthButton = Button(tool_bar, text="Apply Warmth", width=6, height=1, borderwidth=5)
        self.warmthButton.grid(row=8, column=0, padx=2, pady=(0, 2), ipadx=20)
        self.warmthButton.bind("<Button-1>", self.primeni_warmth)

        #Fade
        self.fadeSlide = Scale(tool_bar, from_=0, to=1, tickinterval=0.5, resolution=0.1, orient= HORIZONTAL, label='Fade')
        self.fadeSlide.grid(row=2, column=1, padx=5, pady=5)
        self.clicked_fade = False
        self.fadeSlide.bind("<ButtonPress-1>", self.slider_fade_pressed)
        self.fadeSlide.bind("<ButtonRelease-1>", self.slider_fade_released)
        self.fadeSlide.bind("<Motion>", self.primeni_fade)
        
        #Hightlights
        self.hightSlide = Scale(tool_bar, from_=0, to=1, tickinterval=0.5, resolution=0.1, orient=   HORIZONTAL, label='Highlights')
        self.hightSlide.grid(row=3, column=1, padx=5, pady=5)
        self.clicked_highlight = False
        self.hightSlide.bind("<ButtonPress-1>", self.slider_highlight_pressed)
        self.hightSlide.bind("<ButtonRelease-1>", self.slider_highlight_released)
        self.hightSlide.bind("<Motion>", self.primeni_highlight)

        #Shadows
        self.shadowSlide = Scale(tool_bar, from_=0, to=255,  tickinterval=255, orient= HORIZONTAL, label='Shadows')
        self.shadowSlide.grid(row=4, column=1, padx=5, pady=5)
        self.clicked_shadows = False
        self.shadowSlide.bind("<ButtonPress-1>", self.slider_shadow_pressed)
        self.shadowSlide.bind("<ButtonRelease-1>", self.slider_shadow_released)
        self.shadowSlide.bind("<Motion>", self.primeni_shadows)


        #Zoom
        self.zoonSlide = Scale(tool_bar, from_=1, to=10, tickinterval=9, orient=HORIZONTAL, label='Zoom')
        self.zoonSlide.grid(row=5, column=1, padx=2, pady=2)
        self.clicked_zoom = False
        self.zoonSlide.bind("<ButtonPress-1>", self.slider_zoom_pressed)
        self.zoonSlide.bind("<ButtonRelease-1>", self.slider_zoom_released)
        self.zoonSlide.bind("<Motion>", self.primeni_zoom)

        #Vignette -u kom opsegu
        self.vignetteSlide = Scale(tool_bar, from_=0, to=1, tickinterval=0.5, resolution = 0.1, orient=HORIZONTAL, label='Vignette')
        self.vignetteSlide.grid(row=6, column=1, padx=2, pady=2)
        self.clicked_vignette = False
        self.vignetteSlide.bind("<ButtonPress-1>", self.slider_vignette_pressed)
        self.vignetteSlide.bind("<ButtonRelease-1>", self.slider_vignette_released)
        self.vignetteSlide.bind("<Motion>", self.primeni_vignette)
        
        #Tile Shift - Linear
        self.tileShihtLB = Button(tool_bar, text="Apply Linear TS",  width=6, height=1, borderwidth=5)
        self.tileShihtLB.grid(row=7, column=1, padx=2, pady=2, ipadx=20)
        self.tileShihtLB.bind("<Button-1>", self.primeni_linear_TS)

        #Tile Shift - Radial
        self.tileShihtRB = Button(tool_bar, text="Apply Radial TS",  width=6, height=1, borderwidth=5)
        self.tileShihtRB.grid(row=8, column=1, padx=2, pady=2, ipadx=20)
        self.tileShihtRB.bind("<Button-1>", self.primeni_radial_TS)

        #Sharpen
        self.sharpenB = Button(tool_bar, text="Apply Sharpen", width=6, height=1, borderwidth=5)
        self.sharpenB.grid(row=10, column=1, padx=2, pady=(2,0), ipadx=20)
        self.sharpenB.bind("<Button-1>", self.primeni_sharpen)
        
        #Right frame
        self.right_frame = Frame(root, width=650, height=400, bg='white')
        self.right_frame.grid(row=0, column=2, padx=10, pady=5)
        self.image = ImageTk.PhotoImage(o_image)
        
        self.histRImage = ImageTk.PhotoImage(self.histogramRoriginal)
        self.histGImage = ImageTk.PhotoImage(self.histogramGoriginal)
        self.histBImage = ImageTk.PhotoImage(self.histogramBoriginal)
        
        Label(self.right_frame, image=self.image).grid(row=0,column=0, padx=5, pady=5)
        Label(self.right_frame, image=self.histRImage).grid(row=0,column=2, padx=5, pady=5)
        Label(self.right_frame, image=self.histGImage).grid(row=0,column=4, padx=5, pady=5)
        Label(self.right_frame, image=self.histBImage).grid(row=0,column=6, padx=5, pady=5)

        Label(self.right_frame, image=self.image).grid(row=2,column=0, padx=5, pady=5)
        
        Label(self.right_frame, image=self.histRImage).grid(row=2,column=2, padx=5, pady=5)
        Label(self.right_frame, image=self.histGImage).grid(row=2,column=4, padx=5, pady=5)
        Label(self.right_frame, image=self.histBImage).grid(row=2,column=6, padx=5, pady=5)

    def reset_defaults(self, event):
        self.filteredImage = self.image
        self.filteredImageArray = self.originalImageArray
        self.adjustSlide.set(0)
        self.set_filtered_image()
        self.set_sliders()
        print("Reset to defaults.")

    def set_sliders(self):
        self.adjustSlide.set(0)
        self.brightSlide.set(0)
        self.contrastSlide.set(0)
        self.saturationSlide.set(0)
        self.warmthSlideB.set(0)
        self.warmthSlideR.set(0)
        self.fadeSlide.set(0)
        self.hightSlide.set(0)
        self.shadowSlide.set(0)
        self.zoonSlide.set(1)
        self.vignetteSlide.set(0)
        
    #-----------------------------------------------------------------------FILTERI--------------------------------------------------------------
    #Adjust
    def primeni_adjust(self, event):
        tmp = rotate_image_bilinear(self.originalImageArray, self.adjustSlide.get())
        self.filteredImage = ImageTk.PhotoImage(image=Image.fromarray(tmp))
        self.filteredImageArray = tmp
        print("Adjust done.")
        self.set_filtered_image()

    #Brighteness
    def slider_bright_pressed(self, event):
        self.clicked_bright = True       
            
    def slider_bright_released(self, event):
        self.clicked_bright = False   

    def primeni_brightness(self, event):
        if self.clicked_bright:
            tmp = adjust_brightness(self.originalImageArray, self.brightSlide.get())
            self.filteredImage = ImageTk.PhotoImage(image=Image.fromarray(tmp))
            self.filteredImageArray = tmp
            print("Brightness done.")
            self.set_filtered_image()

    #Contrast
    def slider_contrast_pressed(self, event):
        self.clicked_contrast = True       
            
    def slider_contrast_released(self, event):
        self.clicked_contrast = False   
    
    def primeni_contrast(self, event):
        if self.clicked_contrast:
            tmp = adjust_contrast_correctly(self.originalImageArray, self.contrastSlide.get())
            self.filteredImage = ImageTk.PhotoImage(image=Image.fromarray(tmp))
            self.filteredImageArray = tmp
            print("Contrast done.")
            self.set_filtered_image()

        #Saturation
    def slider_saturation_pressed(self, event):
        self.clicked_saturation = True       
            
    def slider_saturation_released(self, event):
        self.clicked_saturation = False

    def primeni_saturation(self, event):
        if self.clicked_saturation:
            tmp =  saturation(self.originalImageArray, self.saturationSlide.get())
            self.filteredImage = ImageTk.PhotoImage(image=Image.fromarray(tmp))
            self.filteredImageArray = tmp
            print("Saturation done.")
            self.set_filtered_image()
    #Zoom
    def slider_zoom_pressed(self, event):
        self.clicked_zoom = True       
            
    def slider_zoom_released(self, event):
        self.clicked_zoom = False
    
    def primeni_zoom(self, event):
        if self.clicked_zoom:
            tmp = zoom_image(self.originalImage, self.zoonSlide.get())
            self.filteredImage = ImageTk.PhotoImage(image=Image.fromarray(tmp))
            self.filteredImageArray = tmp
            print("Zoom done.")
            self.set_filtered_image()

    #Warmth
    def primeni_warmth(self, event):
        tmp =  warmth_filter(self.originalImageArray, self.warmthSlideR.get(), self.warmthSlideB.get())
        self.filteredImage = ImageTk.PhotoImage(image=Image.fromarray(tmp))
        self.filteredImageArray = tmp
        print("Warmth done.")
        self.set_filtered_image()

    #Fade
    def slider_fade_pressed(self, event):
        self.clicked_fade = True       
            
    def slider_fade_released(self, event):
        self.clicked_fade = False

    def primeni_fade(self, event):
        if self.clicked_fade:
            tmp =  fade_filter(self.originalImageArray, self.fadeSlide.get())
            self.filteredImage = ImageTk.PhotoImage(image=Image.fromarray(tmp))
            self.filteredImageArray = tmp
            print("Fade done.")
            self.set_filtered_image()

    #Hightlights
    def slider_highlight_pressed(self, event):
        self.clicked_highlight = True       
            
    def slider_highlight_released(self, event):
        self.clicked_highlight = False

    def primeni_highlight(self, event):
        if self.clicked_highlight:
            tmp =  highlights_filter(self.originalImageArray, self.hightSlide.get())
            self.filteredImage = ImageTk.PhotoImage(image=Image.fromarray(tmp))
            self.filteredImageArray = tmp
            print("Hightlights done.")
            self.set_filtered_image()

    #Shadows
    def slider_shadow_pressed(self, event):
        self.clicked_shadows = True       
            
    def slider_shadow_released(self, event):
        self.clicked_shadows = False

    def primeni_shadows(self, event):
        if self.clicked_shadows:
            tmp =  shadows_filter(self.originalImageArray, self.shadowSlide.get())
            self.filteredImage = ImageTk.PhotoImage(image=Image.fromarray(tmp))
            self.filteredImageArray = tmp
            print("Shadows done.")
            self.set_filtered_image()

    #Vignette
    def slider_vignette_pressed(self, event):
        self.clicked_vignette = True       
            
    def slider_vignette_released(self, event):
        self.clicked_vignette = False

    def primeni_vignette(self, event):
        if self.clicked_vignette:
            tmp =  vignette_filter(self.originalImageArray, self.vignetteSlide.get())
            self.filteredImage = ImageTk.PhotoImage(image=Image.fromarray(tmp))
            self.filteredImageArray = tmp
            print("Vignette done.")
            self.set_filtered_image()

    #Linear TS
    def primeni_linear_TS(self, event):
        tmp = linear_tilt_shift(self.originalImageArray)
        self.filteredImage = ImageTk.PhotoImage(image=Image.fromarray(tmp))
        self.filteredImageArray = tmp
        print("Linear TS done.")
        self.set_filtered_image()      

    #Radial TS
    def primeni_radial_TS(self, event):
        tmp = radial_tilt_shift(self.originalImageArray)
        self.filteredImage = ImageTk.PhotoImage(image=Image.fromarray(tmp))
        self.filteredImageArray = tmp
        print("Radial TS done.")
        self.set_filtered_image()       

    def primeni_sharpen(self, event):
        tmp =  sharpen_image(self.originalImageArray)
        self.filteredImage = ImageTk.PhotoImage(image=Image.fromarray(tmp))
        self.filteredImageArray = tmp
        print("Sharpen done.")
        self.set_filtered_image()
        
    def set_filtered_image(self):
        self.histogramRofiltered, self.histogramGfiltered, self.histogramBfiltered = hist_to_image(self.filteredImageArray)
        self.histRfiltered = ImageTk.PhotoImage(self.histogramRofiltered)
        self.histGfiltered = ImageTk.PhotoImage(self.histogramGfiltered)
        self.histBfiltered = ImageTk.PhotoImage(self.histogramBfiltered)
        Label(self.right_frame, image=self.filteredImage).grid(row=2,column=0, padx=5, pady=5)
        Label(self.right_frame, image=self.histRfiltered).grid(row=2,column=2, padx=5, pady=5)
        Label(self.right_frame, image=self.histGfiltered).grid(row=2,column=4, padx=5, pady=5)
        Label(self.right_frame, image=self.histBfiltered).grid(row=2,column=6, padx=5, pady=5)

