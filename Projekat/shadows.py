import numpy as np

def shadows_filter(image, coef):
    image = np.array(image, dtype=np.float32)

    threshold = 80
    shadows = image < threshold

    image[shadows] -= image[shadows] * coef
    image = np.clip(image, 0, 255).astype(np.uint8)

    return image

if __name__ == '__main__':
    import matplotlib.pyplot as plt

    path = r'D:\_PMF\_IntroductionToImageProcessing\Project\Image_Processing-Project\Image_Processing-Project\ProjekatIIP\src\images\building.jpg' 
    img = plt.imread(path)
    img = np.array(img)
    res = shadows_filter(img, .55)
    plt.imshow(res)
    plt.show()
    plt.imshow(img)
    plt.show()