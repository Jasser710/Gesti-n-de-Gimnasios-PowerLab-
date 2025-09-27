class Sucursal:
    def __init__(self, codigo, provincia, canton, email, telefono):
        self.codigo = codigo
        self.provincia = provincia
        self.canton = canton
        self.email = email
        self.telefono = telefono
        self.instructores = []      # Lista de instructores de esta sucursal
        self.clientes = []          # Lista de clientes de esta sucursal
        self.clases_grupales = []   # Lista de clases grupales de esta sucursal
    
    def __str__(self):
        return f"Sucursal {self.codigo} - {self.canton}, {self.provincia}"
