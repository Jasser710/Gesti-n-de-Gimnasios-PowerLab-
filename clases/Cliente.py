class Cliente:
    def __init__(self, cedula, nombre, telefono, email, fecha_nacimiento, sexo, fecha_inscripcion, sucursal=None):
        self.cedula = cedula
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.fecha_inscripcion = fecha_inscripcion
        self.sucursal = sucursal  # ✅ NUEVO: Referencia a la sucursal
        self.instructor_asignado = None
        self.mediciones = []
        self.clases_inscritas = []
        self.rutina_actual = None
    
    def __str__(self):
        sucursal_info = f" - Sucursal: {self.sucursal.canton}" if self.sucursal else " - Sin sucursal"
        instructor_info = f" - Instructor: {self.instructor_asignado.nombre}" if self.instructor_asignado else " - Sin instructor"
        return f"{self.nombre} - Cédula: {self.cedula}{sucursal_info}{instructor_info}"
