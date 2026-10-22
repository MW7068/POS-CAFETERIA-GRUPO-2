from src.datos.repositorio_productos import RepositorioProductos


def test_guardar_producto_y_recuperarlo_por_id():
    # Dado un repositorio y un producto
    repositorio = RepositorioProductos()
    producto = {"id": 1, "nombre": "Cafe", "precio": "5.00"}

    # Cuando guardamos el producto
    repositorio.guardar(producto)

    # Entonces podemos recuperarlo con los mismos datos
    recuperado = repositorio.obtener_por_id(1)
    assert recuperado == producto