from fastapi import FastAPI
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from typing import List
#import data
#import json
app = FastAPI()

class Medicion(BaseModel):
    fecha_hora: str # datetime no está definido
    velocidad_viento: float
    direccion_viento: int
    temperatura: float
    humedad: int
    potencia_generada: int
    generador_id: int

@app.get("/pepe/")
async def root():
    mensaje = '../archivo/data.json'
    return mensaje