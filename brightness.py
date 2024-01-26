import numpy as np
import matplotlib.pyplot as plt

def adjust_brightness(image, brightness):
    brightness_adjustment = (brightness / 100.0) * 255
    adjusted_image = image + brightness_adjustment
    adjusted_image = np.clip(adjusted_image, 0, 255)
    
    return adjusted_image.astype(np.uint8)

if __name__ == '__main__':
    path = r'D:\_PMF\_IntroductionToImageProcessing\Project\Image_Processing-Project\Image_Processing-Project\ProjekatIIP\src\images\building.jpg' 
    img = plt.imread(path)
    img = np.array(img)
    rotated_img = adjust_brightness(img, -55)
    plt.imshow(rotated_img)
    # plt.imshow(img)
    plt.show()
    # print(rotated_img)