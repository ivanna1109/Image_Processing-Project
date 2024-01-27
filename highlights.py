import numpy as np

def highlights_filter(image, coef):
    image = np.array(image, dtype=np.float32)

    threshold = 180
    highlights = image > threshold

    image[highlights] += (255 - image[highlights]) * coef
    image = np.clip(image, 0, 255).astype(np.uint8)

    return image

if __name__ == '__main__':
    import matplotlib.pyplot as plt

    path = r'D:\_PMF\_IntroductionToImageProcessing\Project\Image_Processing-Project\Image_Processing-Project\ProjekatIIP\src\images\monalisa.jpg' 
    img = plt.imread(path)
    img = np.array(img)
    res = highlights_filter(img, .55)
    plt.imshow(res)
    plt.show()
    plt.imshow(img)
    plt.show()