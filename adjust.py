import numpy as np
from zoom import zoom

def rotate(image, angle):
    angle_rad = np.radians(angle)
    cos = np.cos(angle_rad)
    sin = np.sin(angle_rad)
    
    h, w = image.shape[:2]
    
    new_w = int(abs(w * cos) + abs(h * sin))
    new_h = int(abs(h * cos) + abs(w * sin))
    
    rotated_img = np.zeros((new_h, new_w, image.shape[2]), dtype=np.uint8)
    
    cx, cy = w // 2, h // 2
    new_cx, new_cy = new_w // 2, new_h // 2
    
    for i in range(new_h):
        for j in range(new_w):
            x_orig = (j - new_cx) * cos + (i - new_cy) * sin + cx
            y_orig = -(j - new_cx) * sin + (i - new_cy) * cos + cy
            
            x0, y0 = int(x_orig), int(y_orig)
            x1, y1 = min(x0 + 1, w - 1), min(y0 + 1, h - 1)
            
            dx, dy = x_orig - x0, y_orig - y0
            w_tl = (1 - dx) * (1 - dy)
            w_tr = dx * (1 - dy)
            w_bl = (1 - dx) * dy
            w_br = dx * dy
            
            if 0 <= x0 < w and 0 <= y0 < h:
                for c in range(image.shape[2]):
                    tl = image[y0, x0, c]
                    tr = image[y0, x1, c]
                    bl = image[y1, x0, c]
                    br = image[y1, x1, c]
                    
                    pxl_val = (tl * w_tl + tr * w_tr +
                                   bl * w_bl + br * w_br)
                    rotated_img[i, j, c] = np.clip(pxl_val, 0, 255)
    
    from_x = (new_w - w) // 2
    from_y = (new_h - h) // 2
    cropped_image = rotated_img[from_y:from_y+h, from_x:from_x+w]
    
    return cropped_image

def adjust(image, angle):
    rotated = rotate(image, angle)

    return zoom(rotated, abs(.65/25*angle)+1)

if __name__ == '__main__':
    import matplotlib.pyplot as plt

    path = r'D:\_PMF\_IntroductionToImageProcessing\Project\Image_Processing-Project\Image_Processing-Project\ProjekatIIP\src\images\building.jpg' 
    img = plt.imread(path)
    img = np.array(img)
    angle = -25
    adjusted = adjust(img, angle)
    plt.imshow(adjusted)
    plt.show()