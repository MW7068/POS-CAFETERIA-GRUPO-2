class RepositorioProductos:
    """Almacena y consulta productos en memoria, sin base de datos."""

    def __init__(self) -> None:
        self.productos = {}

    def guardar(self, producto: dict) -> None:
        """Guarda el producto usando su identificador como clave."""
        self.productos[producto["id"]] = producto

    def obtener_por_id(self, id_producto: int) -> dict:
        """Devuelve el producto asociado al identificador."""
        return self.productos[id_producto]