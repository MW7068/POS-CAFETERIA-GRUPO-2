from src.ejercicio_po import calcular_total


def test_total_de_tres_productos_de_cinco():
    assert calcular_total(5, 3) == 15
