from fastapi import FastAPI, Request, UploadFile, Form, File
import uvicorn
from principal import Reconoce_Figuras
from funciones import bytes_to_image
from OCR_Raul  import OCR
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/figuras_path",status_code=200)
async def figuras_post(request: Request, path:str = Form(), nombre:str = Form()):
    figura = Reconoce_Figuras(path,nombre).reconocimiento_Path()
    return figura

@app.post("/figuras_binario",status_code=200)
async def figuras_post(request: Request, imagen:UploadFile = File(), nombre:str = Form()):
    imagen_bytes = await imagen.read()
    figura = Reconoce_Figuras(imagen_bytes,nombre).reconocimiento_Binarios()    
    return figura

@app.post("/OCR",status_code=200)
async def OCR_Post(request: Request, imagen:UploadFile = File()):
    imagen_bytes = await imagen.read()
    imagen =  bytes_to_image(imagen_bytes)
    objeto_OCR = OCR.OCR_Prueba(imagen)
    texto = objeto_OCR.to_text()    
    fecha = objeto_OCR.Reconocer_fecha2(texto)
    return {"OCR":texto,'FECHA':fecha}


@app.post("/OCR_year",status_code=200)
async def OCR_Post(request: Request, imagen:UploadFile = File()):
    imagen_bytes = await imagen.read()
    imagen =  bytes_to_image(imagen_bytes)
    objeto_OCR = OCR.OCR_Prueba(imagen)
    texto = objeto_OCR.to_text()    
    year = objeto_OCR.Reconocer_year(texto)
    return {"OCR":texto,'year':year}

@app.post("/OCR_API",status_code=200)
async def OCR_API(request: Request, imagen:UploadFile = File(), token:str = Form()):
    imagen_bytes = await imagen.read()
    objeto_OCR = OCR.OCR_Prueba(imagen_bytes)
    texto = objeto_OCR.peticiones(token)["document"]["text"]
    return {'texto':texto}

@app.post("/Procesador_API",status_code=200)
async def OCR_API(request: Request, imagen:UploadFile = File(), token:str = Form()):
    imagen_bytes = await imagen.read()
    objeto_OCR = OCR.OCR_Prueba(imagen_bytes)
    texto = objeto_OCR.peticiones(token)["document"]["entities"]
    return {'texto':texto}


if __name__ == "__main__":
    uvicorn.run("app:app", port=5001, host="0.0.0.0", log_level= "debug" ,reload=True)
