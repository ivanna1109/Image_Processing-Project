import numpy as np

def zoom(image, factor):
    if factor < 1: factor = 1
    if factor > 10: factor = 10

    height, width = image.shape[:2]

    zoomed_width = int(width / factor)
    zoomed_height = int(height / factor)

    left = (width - zoomed_width) // 2
    top = (height - zoomed_height) // 2

    zoomed_image = image[top:top+zoomed_height, left:left+zoomed_width]

    return zoomed_image

if __name__ == '__main__':
    import matplotlib.pyplot as plt

    path = r'D:\_PMF\_IntroductionToImageProcessing\Project\Image_Processing-Project\Image_Processing-Project\ProjekatIIP\src\images\building.jpg' 
    img = plt.imread(path)
    img = np.array(img)
    res = zoom(img, 5)
    plt.imshow(res)
    # plt.imshow(img)
    plt.show()
    # print(res)