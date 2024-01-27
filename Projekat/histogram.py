import numpy as np
from PIL import Image, ImageDraw

def hist(img):
    hist_img = np.zeros(256)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            hist_img[img[i,j]] += 1
    
    return hist_img

def hist_to_image(img_array):
    histogram = hist(img_array)
    max_count = np.max(histogram)
    height = img_array.shape[0]  
    width = len(histogram) 
    histogram_image = Image.new("RGB", (width, height), "white")

    draw = ImageDraw.Draw(histogram_image)
    for i, count in enumerate(histogram):
        bar_height = int(count / max_count * height)
        draw.line((i, height, i, height - bar_height), fill="blue")

    return histogram_image

if __name__ == '__main__':
    import matplotlib.pyplot as plt

    #path = r'D:\_PMF\_IntroductionToImageProcessing\Project\Image_Processing-Project\Image_Processing-Project\ProjekatIIP\src\images\building.jpg' 
    img = plt.imread('images/test.JPG')
    img = np.array(img)
    hist_array = hist(img)
    hist_image = hist_to_image(hist_array)
    """
    plt.bar(range(256), hist_img)
    plt.show()
    """