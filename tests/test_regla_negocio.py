from src.dominio.regla_negocio import calcular_monto_final


def test_calcular_monto_final_cliente_vip_aplica_descuento():
    monto_base = 100.0
    tipo_cliente = "VIP"
    resultado = calcular_monto_final(monto_base, tipo_cliente)
    assert resultado == 85.0