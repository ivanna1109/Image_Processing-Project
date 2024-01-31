from PIL import Image

def load_image_2(filepath):
    original = Image.open(filepath) 
    x_shape = original.width //2
    y_shape = original.height //2
    smaller = original.resize((x_shape, y_shape), Image.ANTIALIAS)
    return smaller

def load_image_cv(filepath):
    original = Image.open(filepath) 
    x_shape = original.width // 10
    y_shape = original.height //10
    smaller = original.resize((x_shape, y_shape), Image.ANTIALIAS)
    return smaller


