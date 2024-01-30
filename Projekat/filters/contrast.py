import numpy as np

def contrast(image, contrast_level):
    '''
    `contrast_level` \in [0, 100]
    '''
    factor = (259 * (contrast_level + 255)) / (255 * (259 - contrast_level))

    image = 128 + (factor * (image.astype(np.float32) - 128))
    image = np.clip(image, 0, 255)

    return image.astype(np.uint8)

if __name__ == '__main__':
    import matplotlib.pyplot as plt

    path = r'D:\_PMF\_IntroductionToImageProcessing\Project\Image_Processing-Project\Image_Processing-Project\ProjekatIIP\src\images\building.jpg' 
    img = plt.imread(path)
    img = np.array(img)
    res = contrast(img, 55)
    plt.imshow(res)
    # plt.imshow(img)
    plt.show()
    # print(res)