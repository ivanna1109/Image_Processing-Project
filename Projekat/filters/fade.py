import numpy as np

def fade_filter(image, coef):
    white_overlay = np.full_like(image, 255)
    faded_img = ((1 - coef) * image + coef * white_overlay).astype(np.uint8)

    return faded_img

if __name__ == '__main__':
    import matplotlib.pyplot as plt

    path = r'D:\_PMF\_IntroductionToImageProcessing\Project\Image_Processing-Project\Image_Processing-Project\ProjekatIIP\src\images\waiting.jpg' 
    img = plt.imread(path)
    img = np.array(img)
    res = fade_filter(img, .55)
    plt.imshow(res)
    plt.show()