class RepositorioProductos:
    def __init__(self):
        self.productos = {}

    def guardar(self, producto):
        self.productos[producto["id"]] = producto

    def obtener_por_id(self, id_producto):
        return self.productos[id_producto]