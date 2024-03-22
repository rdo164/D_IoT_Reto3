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
 
    generador_id = 1
    generador = Generador(generador_id)

    medicion, datos_incorrectos = generar_data(generador)

    if datos_incorrectos == False:
        print("Los datos recibidos son:", medicion)
        return { "mensaje": "datos enviados correctamente" }
    
    else:
        raise HTTPException(status_code=400, detail="datos INCORRECTOS")
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



@app.get("/pepe/")
async def root(mediciones: List[Medicion], file: UploadFile = File(...)):

    file_path = "./archivo/data.json"
    file_content = await file.read(file_path)
    file_data = json.loads(file_content)

    return file_data