class CRUD_Sucursal:

    def __init__(self):
        self.sucursales = []

    def agregar_sucursal(self, sucursal):
        if len(self.sucursales) >= 30:
            return False
        self.sucursales.append(sucursal)
        return True