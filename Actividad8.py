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

    def moneda_operaciones():
    cotizaciones = cotizaciones_monedas()  # Obtener las cotizaciones

    print("Seleccionar moneda de origen:")
    print("1. USD")
    print("2. EUR")
    print("3. ARS")
    print("4. BRL")

    origen = input("Ingrese el número de la moneda de origen: ")

    # asignamos directamente el valor a moneda_origen
    if origen == "1":
        moneda_origen = "USD"
    elif origen == "2":
        moneda_origen = "EUR"
    elif origen == "3":
        moneda_origen = "ARS"
    elif origen == "4":
        moneda_origen = "BRL"
    else:
        print("Moneda de origen no válida.")
        return

    print("\nSeleccionar moneda de destino:")
    print("1. USD")
    print("2. EUR")
    print("3. ARS")
    print("4. BRL")

    destino = input("Ingrese el número de la moneda de destino: ")

    # Asignar directamente el valor a moneda_destino
    if destino == "1":
        moneda_destino = "USD"
    elif destino == "2":
        moneda_destino = "EUR"
    elif destino == "3":
        moneda_destino = "ARS"
    elif destino == "4":
        moneda_destino = "BRL"
    else:
        print("Moneda de destino no válida.")
        return

    print(f"\nMoneda de origen seleccionada: {moneda_origen}")
    print(f"Moneda de destino seleccionada: {moneda_destino}")

    # Solicitar el monto a convertir
    try:
        monto = float(input(f"Ingrese el monto en {moneda_origen}: "))
    except ValueError:
        print("Error: El monto ingresado no es válido.")
        return

    # Realizar la conversión
    resultado = convertir_monedas(monto, moneda_origen, moneda_destino, cotizaciones)

    if resultado is not None:
        print(f"\n{monto} {moneda_origen} equivalen a {resultado:.2f} {moneda_destino}")
        guardar_en_historial_txt(monto, moneda_origen, moneda_destino, resultado)

# Llamar a la función principal
moneda_operaciones()
