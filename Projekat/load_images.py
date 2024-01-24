from PIL import Image

def load_image(filepath):
    original = Image.open(filepath)  # Postavite putanju do vaše slike
    x_shape = original.width // 2
    y_shape = original.height // 2
    smaller = original.resize((x_shape, y_shape), Image.ANTIALIAS)
    return smaller

