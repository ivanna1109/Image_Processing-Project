import numpy as np

def vignette_filter(image, strength):
    image = np.array(image, dtype=np.float32)

    height, width = image.shape[:2]

    x = np.linspace(-1, 1, width)
    y = np.linspace(-1, 1, height)
    x, y = np.meshgrid(x, y)
    dist = np.sqrt(x**2 + y**2)

    max_dist = np.sqrt(2)
    norm_dist = dist / max_dist

    vignette_mask = 1 - norm_dist**2 * strength

    for i in range(image.shape[2]):
        image[:, :, i] *= vignette_mask

    image = np.clip(image, 0, 255).astype(np.uint8)

    return image

if __name__ == '__main__':
    import matplotlib.pyplot as plt

    path = r'D:\_PMF\_IntroductionToImageProcessing\Project\Image_Processing-Project\Image_Processing-Project\ProjekatIIP\src\images\monalisa.jpg' 
    img = plt.imread(path)
    img = np.array(img)
    res = vignette_filter(img, 1) # pokreni za strength = 12 (: | ako hoces da povracas, pokreni sa strength = 18 za sliku `waiting`
    plt.imshow(res)
    plt.show()
    plt.imshow(img)
    plt.show()