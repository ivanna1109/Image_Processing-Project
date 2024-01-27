import numpy as np
from PIL import Image, ImageDraw

def hist(img):
    hist_red = np.zeros(256)
    hist_green = np.zeros(256)
    hist_blue = np.zeros(256)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            pxl = img[i,j]
            hist_red[pxl[0]] += 1
            hist_green[pxl[1]] += 1
            hist_blue[pxl[2]] += 1

    return hist_red, hist_green, hist_blue

def hist_to_image(image_array):
    histogramR, histogramG, histogramB = hist(image_array)
    max_countR = np.max(histogramR)
    max_countG = np.max(histogramG)
    max_countB = np.max(histogramB)
    height = histogramB.shape[0]
    width = len(histogramR)
    histogramR_image = Image.new("RGB", (width, height), "white")
    histogramG_image = Image.new("RGB", (width, height), "white")
    histogramB_image = Image.new("RGB", (width, height), "white")
    drawR = ImageDraw.Draw(histogramR_image)
    drawG = ImageDraw.Draw(histogramG_image)
    drawB = ImageDraw.Draw(histogramB_image)
    
    for i in range(width):
        bar_heightR = int(histogramR[i] / max_countR * height)
        bar_heightG = int(histogramG[i] / max_countG * height)
        bar_heightB = int(histogramB[i] / max_countB * height)
        drawR.line((i, height, i, height - bar_heightR), fill="red")
        drawG.line((i, height, i, height - bar_heightG), fill="green")
        drawB.line((i, height, i, height - bar_heightB), fill="blue")

    return histogramR_image, histogramG_image, histogramB_image

if __name__ == '__main__':
    import matplotlib.pyplot as plt

    #path = r'D:\_PMF\_IntroductionToImageProcessing\Project\Image_Processing-Project\Image_Processing-Project\ProjekatIIP\src\images\building.jpg' 
    img = plt.imread('images/test.JPG')
    img = np.array(img)
    #print(type(hist(img)))
    #print(type(hist_image = hist_to_image(hist(img))
    """
    plt.bar(range(256), hist_img)
    plt.show()
    """