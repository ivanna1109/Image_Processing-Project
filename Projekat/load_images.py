from PIL import Image

def load_image(filepath):
    original = Image.open(filepath) 
    x_shape = original.width //10
    y_shape = original.height //10
    smaller = original.resize((x_shape, y_shape), Image.ANTIALIAS)
    return smaller

