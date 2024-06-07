# Funciones para preprocesamiento de imagenes
from io import BytesIO
from PIL import Image
import numpy as np



def getimage(path): 
    with open(path, 'rb') as file_b:
        image_bytes = bytes(file_b.read())
    return image_bytes

def bytes_to_image(image_bytes):
    image_bytes = BytesIO(image_bytes)
    image_bytes = Image.open(image_bytes).convert('RGB')
    image_bytes = image_bytes.convert('RGB')
    image_bytes = np.array(image_bytes)
    return image_bytes

