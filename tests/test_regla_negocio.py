from src.dominio.regla_negocio import calcular_monto_final


def test_calcular_monto_final_cliente_vip_aplica_descuento():
    # Dado un monto base de 100 soles y un cliente VIP
    monto_base = 100.0
    tipo_cliente = "VIP"

    # Cuando se calcula el monto final
    resultado = calcular_monto_final(monto_base, tipo_cliente)

    # Entonces se aplica un descuento del 15 %
    assert resultado == 85.0