# Funciones para hacer peticiones a las funciones de preprocesamiento
# Funciones para ocupar con la API
from funciones import  bytes_to_image, getimage
from PyShapes import *
import cv2


class Reconoce_Figuras:
    def __init__(self, image, nombre):
        self.imagen = image
        self.nombre = nombre
        
    def reconocimiento_Binarios(self): 
        self.imagen = bytes_to_image(self.imagen)    
        imagen_array = cv2.imwrite(self.nombre+".png",self.imagen)
        shapes = PyShape(self.nombre+".png")
        shapes_dictionary = shapes.get_all_shapes()   
        shapes_dictionary["nombre imagen"] = self.nombre
        return shapes_dictionary
        
    def reconocimiento_Path(self):         
        self.imagen = getimage(self.imagen)
        self.imagen = bytes_to_image(self.imagen)    
        imagen_array = cv2.imwrite(f"{self.nombre}.png" ,self.imagen)
        shapes = PyShape(f"{self.nombre}.png" )
        shapes_dictionary = shapes.get_all_shapes()    
        shapes_dictionary["nombre imagen"] = self.nombre
        return shapes_dictionary
    
if __name__ == "__main__":
    objeto = Reconoce_Figuras('imagen.png')
    figuras = objeto.reconocimiento()
    print(figuras)