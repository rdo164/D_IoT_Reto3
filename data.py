import numpy as np
import pandas as pd
import random
from datetime import datetime
import json
#importo mi clase generador
from classGenerador import Generador

def generar_data(generador):

    datos_incorrectos = False

    id = generador.generador_id 
    
    p_error = np.random.randint(1,100) 

    # timestamp
    timestamp = datetime.utcnow().isoformat()
    
    generador.set_fecha_hora(timestamp)
    
    # velocidad viento
    vv = np.random.normal(10, 2)
    generador.set_velocidad_viento(vv)

    # Dirección de viento
    direccion_viento = np.random.randint(0, 360)
    generador.set_direccion_viento(direccion_viento)

    # temperatura
    temperatura = np.random.normal(15, 2)

    # probabilidad de error
    if(p_error < 5):
        temperatura = -23342
        datos_incorrectos = True



    generador.set_temperatura(temperatura)
    
    # humedad
    humedad = np.random.randint(40, 80)
    generador.set_humedad(humedad)
    
    # potencia generada
    potencia_generada = np.random.randint(0, 1000)
    generador.set_potencia_generada(potencia_generada)



    medicion = {
        "generador_id": id,

        "fecha_hora": timestamp,
        
        "velocidad_viento": vv,
        
        "direccion_viento": direccion_viento,
        
        "temperatura": temperatura,
        
        "humedad": humedad,
        
        "potencia_generada": potencia_generada,
    }
    
    return medicion, datos_incorrectos


# creo la 
mediciones = []
output_file_path = './archivo/data.json'
n_generadores = 1

#with open(output_file_path, 'a') as output_file:

  #  for i in range(n_generadores):
   #     generador_id = i+1
        # Creo un objeto tipo generador 
    #    generador = Generador(generador_id) 
        
        
        #medicion = data(generador)

        # añado la medición creada 
       # mediciones.append(generador) 

        # guardar los registros en un archivo JSON 
        # json.dump(medicion, output_file)
        # output_file.write('\n')


            
