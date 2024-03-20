import numpy as np
import pandas as pd

# Definir variables
generador_id = 1
fecha_hora = pd.to_datetime("2023-03-08 12:00:00")
velocidad_viento = np.random.normal(10, 2)
direccion_viento = np.random.randint(0, 360)
temperatura = np.random.normal(15, 2)
humedad = np.random.randint(40, 80)
potencia_generada = np.random.randint(0, 1000)
mediciones = []
# Crear medición
medicion = {
    "fecha_hora": fecha_hora,
    "velocidad_viento": velocidad_viento,
    "direccion_viento": direccion_viento,
    "temperatura": temperatura,
    "humedad": humedad,
    "potencia_generada": potencia_generada,
    "generador_id": generador_id
}


mediciones.append(medicion)

print(medicion)