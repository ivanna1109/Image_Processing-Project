import numpy as np
import matplotlib.pyplot as plt

def adjust_contrast_correctly(image, contrast_level):

    factor = (259 * (contrast_level + 255)) / (255 * (259 - contrast_level))

    adjusted_image = 128 + (factor * (image.astype(np.float32) - 128))
    adjusted_image = np.clip(adjusted_image, 0, 255)

    return adjusted_image.astype(np.uint8)

if __name__ == '__main__':
    path = r'D:\_PMF\_IntroductionToImageProcessing\Project\Image_Processing-Project\Image_Processing-Project\ProjekatIIP\src\images\building.jpg' 
    img = plt.imread(path)
    img = np.array(img)
    rotated_img = adjust_contrast_correctly(img, 120)
    plt.imshow(rotated_img)
    # plt.imshow(img)
    plt.show()
    # print(rotated_img)
    # tmp = img.copy()
    # print(tmp==img)
    # print(np.all(tmp==img))