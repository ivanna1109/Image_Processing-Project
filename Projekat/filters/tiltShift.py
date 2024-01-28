import numpy as np
from math import sqrt

def linear_tilt_shift(image):
    height, width, _ = image.shape
    center = (height // 2, width // 2)
    max_distance = max(center[0], center[1])
    
    tilted_image = np.zeros_like(image, dtype=np.float32)
    
    for k in range(3):  
        for i in range(height): 
            for j in range(width): 
                distance = np.abs(i - center[0]) + np.abs(j - center[1])
                b_factor = min(distance / max_distance, 1.0)             
                new_pixel = (1 - b_factor) * image[i, j, k] + b_factor * np.mean(image[max(i-1, 0):min(i+2, height), max(j-1, 0):min(j+2, width), k])
                tilted_image[i, j, k] = new_pixel

    return np.clip(tilted_image, 0, 255).astype(np.uint8)


def radial_tilt_shift(image):
    height, width, _ = image.shape
    center = (height // 2, width // 2)
    radius = min(center[0], center[1])
    
    tilted_image = np.zeros_like(image, dtype=np.float32)
    
    for k in range(3):  
        for i in range(height):  
            for j in range(width):  
                distance = np.sqrt((i - center[0])**2 + (j - center[1])**2)
                blur_factor = min(distance / radius, 1.0)
                blurred_pixel = (1 - blur_factor) * image[i, j, k] + \
                                blur_factor * np.mean(image[max(i-1, 0):min(i+2, height), max(j-1, 0):min(j+2, width), k])
                tilted_image[i, j, k] = blurred_pixel
    return np.clip(tilted_image, 0, 255).astype(np.uint8)
