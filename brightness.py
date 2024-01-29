import numpy as np

def brightness(image, factor):
    '''
    `factor` \in [0, 100]
    '''
    per_pxl_adj = (factor / 100.0) * 255
    brighter_img = image + per_pxl_adj
    
    return np.clip(brighter_img, 0, 255).astype(np.uint8)

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    
    path = r'D:\_PMF\_IntroductionToImageProcessing\Project\Image_Processing-Project\Image_Processing-Project\ProjekatIIP\src\images\building.jpg' 
    img = plt.imread(path)
    img = np.array(img)
    res = brightness(img, 55)
    plt.imshow(res)
    plt.show()