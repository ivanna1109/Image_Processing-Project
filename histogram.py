import numpy as np

def hist(img):
    hist_img = np.zeros(256)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            hist_img[img[i,j]] += 1
    
    return hist_img


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    path = r'D:\_PMF\_IntroductionToImageProcessing\Project\Image_Processing-Project\Image_Processing-Project\ProjekatIIP\src\images\building.jpg' 
    img = plt.imread(path)
    img = np.array(img)
    hist_img = hist(img)

    plt.bar(range(256), hist_img)
    plt.show()