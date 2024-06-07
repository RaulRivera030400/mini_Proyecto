from funciones import  bytes_to_image, getimage
from PyShapes import *
import cv2


class Reconoce_Figuras:
    def __init__(self, image):
        self.imagen = getimage(image)
        self.imagen1 = bytes_to_image(self.imagen)
        
    def reconocimiento(self):
        imagen_array = cv2.imwrite('imagen.jpg',self.imagen1)
        shapes = PyShape('imagen.jpg')
        shapes_dictionary = shapes.get_all_shapes()
        
        return shapes_dictionary

if __name__ == "__main__":
    objeto = Reconoce_Figuras('imagen.png')
    figuras = objeto.reconocimiento()
    print(figuras)
