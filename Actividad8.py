def cotizaciones_monedas():
    # diccionario con las tasas de cambio fijas respecto al USD
    cotizaciones = {
        "USD": 1.0,
        "EUR": 0.91,
        "ARS": 1185.0,
        "BRL": 5.0
    }
    return cotizaciones

"""AQUI SOLO PONEMOS LA COTIZACION DEL DOLAR, PARA PASAR UNA MONEDA A OTRA USAMOS LA COTIZACION DEL DOLAR DE POR MEDIO, POR EJ DE ARS A BR: CONVERTIMOS LOS ARS A USD Y LOS USD A BRL"""

def convertir_monedas(monto, moneda_origen, moneda_destino, cotizaciones):
    cotizacion_origen = cotizaciones.get(moneda_origen)
    cotizacion_destino = cotizaciones.get(moneda_destino)
    
    # Verifica si las cotizaciones son validas
    if cotizacion_origen is None or cotizacion_destino is None:
        print("Error: Una de las monedas no tiene cotización válida.")
        return None

    # Realizar la conversión
    valor_destino = (monto / cotizacion_origen) * cotizacion_destino
    return valor_destino

def guardar_en_historial_txt(monto, moneda_origen, moneda_destino, resultado):
    # Creamos una línea de texto con los datos de la conversion para leer mejor
    conversion = f"{monto} {moneda_origen} -> {resultado:.2f} {moneda_destino}\n"

    # Guardar archivo historial.txt
    with open("historial.txt", "a") as archivo:
        archivo.write(conversion)

    print("\nConversión guardada en el historial (historial.txt).")