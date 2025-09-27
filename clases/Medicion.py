class Medicion:
    def __init__(self, fecha, peso, estatura, porcentaje_grasa, porcentaje_musculo, 
                 edad_metabolica, grasa_visceral, cintura, cadera, pecho, muslo,
                 imc, clasificacion_imc, proteina_recomendada, vasos_agua):
        self.fecha = fecha
        self.peso = peso
        self.estatura = estatura
        self.porcentaje_grasa = porcentaje_grasa
        self.porcentaje_musculo = porcentaje_musculo
        self.edad_metabolica = edad_metabolica
        self.grasa_visceral = grasa_visceral
        self.cintura = cintura
        self.cadera = cadera
        self.pecho = pecho
        self.muslo = muslo
        self.imc = imc
        self.clasificacion_imc = clasificacion_imc
        self.proteina_recomendada = proteina_recomendada
        self.vasos_agua = vasos_agua
    
    def __str__(self):
        return f"Medición {self.fecha} - IMC: {self.imc:.2f}"