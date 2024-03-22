from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel, FilePath
from typing import List
from datetime import datetime
from data import generar_data
from classGenerador import Generador
from fastapi import HTTPException

import json

app = FastAPI()

n_generadores = 10
mediciones = []

class Medicion(BaseModel):
    generador_id: int
    fecha_hora: datetime # datetime no está definido
    velocidad_viento: int
    direccion_viento: int
    temperatura: int
    humedad: int
    potencia_generada: int

# creo un endpoint 
@app.post("/mediciones/")
async def create_upload_file(medicion: Medicion):
 

    for i in range(n_generadores):
     generador_id = i + 1
     generador = Generador(generador_id)

     medicion, datos_incorrectos = generar_data(generador)
     mediciones.append(medicion)

    if datos_incorrectos == False:
        print("Los datos recibidos son:", medicion) 

    else:
        raise HTTPException(status_code=400, detail=f"datos del generador{generador.get_generador_id()} INCORRECTOS")

@app.get("/mediciones/")
async def get_mediciones():
    return mediciones


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

