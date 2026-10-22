def calcular_monto_final(monto_base: float, tipo_cliente: str) -> float:
    if tipo_cliente == "VIP":
        return monto_base * 0.85
    return monto_base