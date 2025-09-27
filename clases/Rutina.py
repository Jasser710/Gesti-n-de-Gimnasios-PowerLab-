class Rutina:
    def __init__(self, ejercicios_por_area):
        # ejercicios_por_area es un diccionario:
        # {
        #   "Pecho y tríceps": ["Press banca", "Fondos", etc.],
        #   "Bíceps": ["Curl con barra", "Curl martillo", etc.],
        #   "Piernas": ["Sentadillas", "Prensa", etc.],
        #   "Espalda": ["Dominadas", "Remo con barra", etc.]
        # }
        self.ejercicios_por_area = ejercicios_por_area
    
    def __str__(self):
        return f"Rutina con {len(self.ejercicios_por_area)} áreas de ejercicio"