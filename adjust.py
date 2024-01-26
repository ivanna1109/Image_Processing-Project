import numpy as np
import matplotlib.pyplot as plt

def rotate_image_bilinear(image, angle):
    angle_rad = np.radians(angle)
    cos_angle = np.cos(angle_rad)
    sin_angle = np.sin(angle_rad)
    
    h, w = image.shape[:2]
    
    new_w = int(abs(w * cos_angle) + abs(h * sin_angle))
    new_h = int(abs(h * cos_angle) + abs(w * sin_angle))
    
    rotated_image = np.zeros((new_h, new_w, image.shape[2]), dtype=np.uint8)
    
    cx, cy = w // 2, h // 2
    new_cx, new_cy = new_w // 2, new_h // 2
    
    for i in range(new_h):
        for j in range(new_w):
            x_orig = (j - new_cx) * cos_angle + (i - new_cy) * sin_angle + cx
            y_orig = -(j - new_cx) * sin_angle + (i - new_cy) * cos_angle + cy
            
            x0, y0 = int(x_orig), int(y_orig)
            x1, y1 = min(x0 + 1, w - 1), min(y0 + 1, h - 1)
            
            dx, dy = x_orig - x0, y_orig - y0
            weight_tl = (1 - dx) * (1 - dy)
            weight_tr = dx * (1 - dy)
            weight_bl = (1 - dx) * dy
            weight_br = dx * dy
            
            if 0 <= x0 < w and 0 <= y0 < h:
                for c in range(image.shape[2]):
                    tl = image[y0, x0, c]
                    tr = image[y0, x1, c]
                    bl = image[y1, x0, c]
                    br = image[y1, x1, c]
                    
                    pixel_value = (tl * weight_tl + tr * weight_tr +
                                   bl * weight_bl + br * weight_br)
                    rotated_image[i, j, c] = np.clip(pixel_value, 0, 255)
    
    start_x = (new_w - w) // 2
    start_y = (new_h - h) // 2
    cropped_image = rotated_image[start_y:start_y+h, start_x:start_x+w]
    
    return cropped_image

path = r'D:\_PMF\_IntroductionToImageProcessing\Project\Image_Processing-Project\Image_Processing-Project\ProjekatIIP\src\images\building.jpg' 
img = plt.imread(path)
img = np.array(img)
rotated_img = rotate_image_bilinear(img, -25)
plt.imshow(rotated_img)
# plt.imshow(img)
plt.show()
print(rotated_img)