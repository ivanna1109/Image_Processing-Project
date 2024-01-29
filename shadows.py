import numpy as np

def shadows(image, coef):
    '''
    `coef` \in [0, 1]
    '''
    image = np.array(image, dtype=np.float32)

    threshold = 80
    to_shadows = image < threshold

    image[to_shadows] -= image[to_shadows] * coef
    image = np.clip(image, 0, 255).astype(np.uint8)

    return image

if __name__ == '__main__':
    import matplotlib.pyplot as plt

    path = r'D:\_PMF\_IntroductionToImageProcessing\Project\Image_Processing-Project\Image_Processing-Project\ProjekatIIP\src\images\monalisa.jpg' 
    img = plt.imread(path)
    img = np.array(img)
    res = shadows(img, .55)
    plt.imshow(res)
    plt.show()
    # plt.imshow(img)
    # plt.show()