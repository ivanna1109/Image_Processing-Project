import numpy as np

def warmth(image, i, j):
    image = np.array(image, dtype=np.int16)

    image[:, :, 0] = np.clip(image[:, :, 0] + i, 0, 255)
    image[:, :, 2] = np.clip(image[:, :, 2] - j, 0, 255)

    return image.astype(np.uint8)

if __name__ == '__main__':
    import matplotlib.pyplot as plt

    path = r'D:\_PMF\_IntroductionToImageProcessing\Project\Image_Processing-Project\Image_Processing-Project\ProjekatIIP\src\images\building.jpg' 
    img = plt.imread(path)
    img = np.array(img)
    res = warmth(img, 50, 50)
    plt.imshow(res)
    # plt.imshow(img)
    plt.show()
    # print(rotated_img)