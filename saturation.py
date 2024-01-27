import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

def saturation(image, factor):
    """
    Za Zivanu: slider za `factor` \in [-1, 1] 
    """
    image_hsv = colors.rgb_to_hsv(image / 255)

    image_hsv[:, :, 1] += (1 - image_hsv[:, :, 1]) * factor
    image_hsv[:, :, 1] = np.clip(image_hsv[:, :, 1], 0, 1)
    
    return (colors.hsv_to_rgb(image_hsv)*255).astype(np.uint8)

if __name__ == '__main__':
    path = r'D:\_PMF\_IntroductionToImageProcessing\Project\Image_Processing-Project\Image_Processing-Project\ProjekatIIP\src\images\waiting.jpg' 
    img = plt.imread(path)
    img = np.array(img)
    rotated_img = saturation(img, 0)
    plt.imshow(rotated_img)
    plt.show()
