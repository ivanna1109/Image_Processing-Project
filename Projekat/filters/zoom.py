import numpy as np
from PIL import Image

def zoom(image, factor):
    print(type(image))
    if isinstance(image, np.ndarray):
        image = Image.fromarray(image)
    new_width = int(image.width * factor)
    new_height = int(image.height * factor)

    transformed_image = image.resize((new_width, new_height))
    left = (new_width - image.width) // 2
    top = (new_height - image.height) // 2
    right = (new_width + image.width) // 2
    bottom = (new_height + image.height) // 2
    zoomed_image = transformed_image.crop((left, top, right, bottom))

    return np.array(zoomed_image)




