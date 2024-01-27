import numpy as np

def sharpen_image(image):
    height = image.shape[0]
    width = image.shape[1]
    matrix5x5 = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]]) 
    sharpened_image = np.zeros_like(image, dtype=np.float32) 
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            for k in range(3):
                neighborhood = image[i - 1 : i + 2, j - 1 : j + 2, k] 
                sharpened_image[i, j, k] = np.sum(neighborhood * matrix5x5)
    return np.clip(sharpened_image, 0, 255).astype(np.uint8)