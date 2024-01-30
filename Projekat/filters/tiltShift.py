import numpy as np
from math import sqrt

def linear_tilt_shift(image):
    height, width, _ = image.shape
    center = (height // 2, width // 2)
    max_distance = max(center[0], center[1])
    
    tilted_image = np.zeros_like(image, dtype=np.float32)
    blur_distance = height/10 #do koje distance nece biti blurovano
    print(blur_distance)
    blur_rate = 0.6 #faktor blurovanja, moze da se menja
    for k in range(3):  
        for i in range(height): 
            for j in range(width): 
                distance = np.abs(i - center[0]) #imam traku po sredini slike
                if distance <= blur_distance:
                    b_factor = 0.0
                else:
                    b_factor = min((distance - blur_distance) * blur_rate / max_distance, 1.0)
                b_factor = min(distance / max_distance, 1.0)             
                new_pixel = (1 - b_factor) * image[i, j, k] + b_factor * np.mean(image[max(i-1, 0):min(i+2, height), max(j-1, 0):min(j+2, width), k])
                tilted_image[i, j, k] = new_pixel

    return np.clip(tilted_image, 0, 255).astype(np.uint8)


def radial_tilt_shift(image):
    height, width, _ = image.shape
    center = (height // 2, width // 2)
    radius = min(center[0], center[1])
    
    tilted_image = np.zeros_like(image, dtype=np.float32)
    start_distance = height//15
    blur_rate = 0.6
    for k in range(3):  
        for i in range(height):  
            for j in range(width):  
                distance = np.sqrt((i - center[0])**2 + (j - center[1])**2)
                if distance <= start_distance:
                    blur_factor = 0.0
                else:
                    blur_factor = min((distance - start_distance) * blur_rate / radius, 1.0)
                blur_factor = min(distance / radius, 1.0)
                blurred_pixel = (1 - blur_factor) * image[i, j, k] + \
                                blur_factor * np.mean(image[max(i-1, 0):min(i+2, height), max(j-1, 0):min(j+2, width), k])
                tilted_image[i, j, k] = blurred_pixel
    return np.clip(tilted_image, 0, 255).astype(np.uint8)
