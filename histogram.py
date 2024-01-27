import numpy as np

def hist(img):
    hist_red = np.zeros(256)
    hist_green = np.zeros(256)
    hist_blue = np.zeros(256)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            pxl = img[i,j]
            hist_red[pxl[0]] += 1
            hist_green[pxl[1]] += 1
            hist_blue[pxl[2]] += 1

    return hist_red, hist_green, hist_blue


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    path = r'D:\_PMF\_IntroductionToImageProcessing\Project\Image_Processing-Project\Image_Processing-Project\ProjekatIIP\src\images\building.jpg' 
    img = plt.imread(path)
    img = np.array(img)
    hist_img = hist(img)

    plt.bar(range(256), hist_img[0], color='r')
    plt.bar(range(256), hist_img[1], color='g')
    plt.bar(range(256), hist_img[2], color='b')
    plt.show()