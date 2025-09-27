class ClaseGrupal:
    def __init__(self, codigo, capacidad, salon, horario, tipo, instructor):
        self.codigo = codigo
        self.capacidad = capacidad
        self.salon = salon
        self.horario = horario
        self.tipo = tipo  # "CrossFit", "HIIT", etc.
        self.instructor = instructor  # Objeto Instructor
        self.clientes_inscritos = []  # Lista de objetos Cliente
    
    def __str__(self):
        return f"{self.tipo} - {self.horario} - Cupos: {self.capacidad - len(self.clientes_inscritos)}/{self.capacidad}"