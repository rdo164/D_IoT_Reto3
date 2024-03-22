class Generador:
    def __init__(self, generador_id, fecha_hora=-1,
                 velocidad_viento=-1, direccion_viento=-1, temperatura=-1,
                 humedad=-1, potencia_generada = None):
        self.fecha_hora = fecha_hora
        self.velocidad_viento = velocidad_viento
        self.direccion_viento = direccion_viento
        self.temperatura = temperatura
        self.humedad = humedad
        self.generador_id = generador_id
        self.potencia_generada = potencia_generada

    def set_fecha_hora(self, fecha_hora):
        self.fecha_hora = fecha_hora

    def get_fecha_hora(self):
        return self.fecha_hora

    def get_velocidad_viento(self):
        return self._velocidad_viento

    def set_velocidad_viento(self, velocidad_viento):
        self._velocidad_viento = velocidad_viento

    def get_direccion_viento(self):
        return self._direccion_viento

    def set_direccion_viento(self, direccion_viento):
        self._direccion_viento = direccion_viento

    def get_temperatura(self):
        return self._temperatura

    def set_temperatura(self, temperatura):
        self._temperatura = temperatura

    def get_humedad(self):
        return self._humedad

    def set_humedad(self, humedad):
        self._humedad = humedad

    def get_potencia_generada(self):
        return self.potencia_generada

    def set_potencia_generada(self, potencia_generada):
        self.potencia_generada = potencia_generada

