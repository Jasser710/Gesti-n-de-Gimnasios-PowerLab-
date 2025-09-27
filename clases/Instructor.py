class Instructor:
    def __init__(self, cedula, nombre, telefono, email, fecha_nacimiento, especialidades, sucursal=None):
        self.cedula = cedula
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.fecha_nacimiento = fecha_nacimiento
        self.especialidades = especialidades
        self.sucursal = sucursal  # ✅ NUEVO: Referencia a la sucursal
    
    def __str__(self):
        sucursal_info = f" - Sucursal: {self.sucursal.canton}" if self.sucursal else " - Sin sucursal"
        return f"{self.nombre} - {', '.join(self.especialidades)}{sucursal_info}"
        
