from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel, FilePath
from typing import List
import data
import json

app = FastAPI()

class Medicion(BaseModel):
    generador_id: int
    fecha_hora: str # datetime no está definido
    velocidad_viento: int
    direccion_viento: int
    temperatura: int
    humedad: int
    potencia_generada: int

# creo un endpoint 
@app.post("/mediciones/")
async def create_upload_file(mediciones: List[Medicion]):
    
    #file_path = "./archivo/data.json"
    #file_content = await FilePath.read(file_path)
    #file_data = json.loads(file_content)
    #print(file_data)

    for medicion in mediciones:
        print(medicion.dict())  # Simplemente imprime las mediciones recibidas
    
    return {"mediciones_count": len(mediciones)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

@app.get("/pepe/")
async def root(mediciones: List[Medicion], file: UploadFile = File(...)):

    file_path = "./archivo/data.json"
    file_content = await file.read(file_path)
    file_data = json.loads(file_content)

    return file_data