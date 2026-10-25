def calcular_monto_final(monto_base: float, tipo_cliente: str) -> float:
    """Calcula el monto final según el tipo de cliente."""
    if monto_base < 0:
        raise ValueError("El monto base no puede ser negativo")

    if tipo_cliente == "VIP":
        return round(monto_base * 0.85, 2)

    return round(monto_base, 2)