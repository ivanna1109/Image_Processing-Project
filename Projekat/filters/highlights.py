import numpy as np

def highlights(image, coef):
    '''
    `coef` \in [0, 1]
    '''
    image = np.array(image, dtype=np.float32)

    threshold = 180
    to_highlights = image > threshold

    image[to_highlights] += (255 - image[to_highlights]) * coef

    return np.clip(image, 0, 255).astype(np.uint8)

if __name__ == '__main__':
    import matplotlib.pyplot as plt

    path = r'D:\_PMF\_IntroductionToImageProcessing\Project\Image_Processing-Project\Image_Processing-Project\ProjekatIIP\src\images\monalisa.jpg' 
    img = plt.imread(path)
    img = np.array(img)
    res = highlights(img, .55)
    plt.imshow(res)
    plt.show()
    # plt.imshow(img)
    # plt.show()