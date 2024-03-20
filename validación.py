from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class Medicion(BaseModel):
    fecha_hora: datetime
    velocidad_viento: float
    direccion_viento: int
    temperatura: float
    humedad: int
    potencia_generada: int
    generador_id: int

@app.post("/mediciones")
async def crear_medicion(medicion: Medicion = Body(...)):
    # Validar datos
    # Almacenar medición
    # ...

